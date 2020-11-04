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
