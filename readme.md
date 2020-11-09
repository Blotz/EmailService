This is a school programming project
------------------------------------
This is a email service/website which notifies users when ever they receive homework on an application called ClassCharts.  


Programming notes
-----------------
#### adding a user to the database

- [ ] add user to database
	- verify = 0

- [x] generate rand 32 char ID
- [x] generate 32 byte salt
- [x] hash ID + salt

- [x] id , hash

- [ ] send email containing verification info
- [x] del id

- [x] if userCode, purpose exists: del userCode Purpose
	- store userCode, Hash, purpose, Time 1d from now

#### verify user
- [x] userCode, ID, Purpose

- [x] select hash from db where userCode and Purpose
- [x] extract salt and hash
- [x] hash ID + salt

- [x] this
```python
if hash = hash: 
	del from db where userCode and Purpose
	return True 
else: 
	return False
```


## whiteboard notes

### External flask server
>> Email Verification?id=int 
> Add HWs to database
> Charges verification of email
>> DeleteAccount?id=int
> Removes HW from database
> removes Account
>> EmailVerified
>> AccountDeleted

### Users
#### Me
> triggers Add_user_code()
>> add user to db
>> send email
>> store email code
#### url/verify/code
> checks cords and verified
>> checks code
>> verify
>> add HW 

### Python Program

functions|Purpose
---------|-------
/|add user to db
Add Account|- veridy = 0
\|send verify email
/|remove homework from homeowkr
Remove Account|- remove account details


|Bugs|
|----|
|- icloud blocks email|
|- hw due same day breaks email format|
