from flask import Flask
from flask import request
from flask import render_template
import hashlib, os
import sqlConnections
import homework

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/')
def hello():
    return 'Hello, World!'

#verification of account
#########################################################################################################

@app.route('/verify',defaults={'code':None})
@app.route('/verify/<code>')
def verify(code):#verifies the code was added correctly
    if code == None:
        return render_template('nocode.html')
    else:
        return render_template('verify/verify.html',code=str(code))#redirects to code input webpage

@app.route('/verify/<code>/',methods=['get','post'])
def verify_confirmation(code):
    ###########################
    # add redirects for different errors
    # eg this account has already been verified
    # eg incorrect code
    ###########################
    #checks whether anything was inputted before submitting
    userCode = None
    if request.method == 'POST':
        userCode = request.form.get('code')

    #if nothinng was submited, redirects back to webpage
    if not userCode:
        return render_template('verify/verify.html',code=str(code))
    
    #checks verification
    print('checks verification')

    # tries to get the email token of that user
    purpose = 'verify'
    sql = sqlConnections.dataConnection()
    IDhash = sql.get_hash(userCode, purpose)

    #if it didnt return anything, it will redirect the user back to the pagee
    if not IDhash:
        print('person doesnt exist')
        return render_template('verify/verify.html',code=str(code))
    
    #now it starts to split up the hash and work with it
    IDhash = bytes.fromhex(IDhash)

    salt = IDhash[32:]
    idhash = IDhash[:32]

    #uses the new code provided in the url and the hash extracted from the db to calcuelate the hash
    newhash = hashlib.pbkdf2_hmac('sha256',code.encode('utf-8'),salt,100000)

    #if these hashes are the same, it starts the code for verifying
    if newhash == idhash:
        sql.verify_user(userCode) #updating the user database
        sql.mail_remove_request(userCode, purpose) #removing the old verification token to prevent it from being reused
        homework.update_database(userCode) #runs code to update the database with all the known homework
        print('success')
        return render_template('success.html',action='verified')
    else:
        print('wrong code in url')
        return render_template('verify/verify.html',code=str(code))

#########################################################################################################
@app.route('/delete',defaults={'code':None})
@app.route('/delete/<code>')
def delete(code):#verifies the code was added correctly
    if code == None:
        return render_template('nocode.html')#redirects to code input webpage
    else:
        return render_template('delete/delete.html',code=str(code))#redirects to code input webpage

@app.route('/delete/<code>/',methods=['get','post'])
def delete_confirmation(code):
    #checks whether anything was inputted before submitting
    userCode = None
    if request.method == 'POST':
        userCode = request.form.get('code')

    #if nothing was submited, redirects back to webpage
    if not userCode:
        return render_template('delete/delete.html',code=str(code))
    
    #checks deletion
    print('checks deletion')
    deleted = True
    if deleted == True:
        return render_template('success.html',action='deleted')
    else:
        return render_template('delete/delete.html',code=str(code))
#########################################################################################################


if __name__ == "__main__":
    app.run(debug=True)