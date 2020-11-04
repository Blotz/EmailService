import os
import hashlib
import random
import string
import sqlConnections
import datetime

def get_random_string(length):
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def add_user():
    userCode = input('enter user code: ')
    #####################################
    # i need to add users to the users table
    # needs email, birthday and code input
    # verify will be 0
    #####################################

    #selects the purpose for the email token 
    purpose = 'verify'
    #generates a date until the token is nolonger valid
    date = datetime.datetime.now()
    date = date + datetime.timedelta(days=+1)

    #generates a random string of id
    code = get_random_string(64)

    #generates salt + hash and combines
    salt = os.urandom(32)
    newhash = hashlib.pbkdf2_hmac('sha256',code.encode('utf-8'),salt,100000)
    datahash = newhash + salt

    #############
    # send verification email
    # lol
    #############
    
    sql = sqlConnections.dataConnection()
    data = sql.mail_get_request(userCode, purpose)

    if data:
        sql.mail_remove_request(userCode, purpose)

    sql.mail_add_request(userCode, purpose, datahash.hex(), date)

    print('code :', code)
    
def del_user():
    pass

while True:
    ans = input()
    if ans == '1':
        add_user()
    else:
        del_user()
