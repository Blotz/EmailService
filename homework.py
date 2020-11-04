'''
import this code to the main flask server
use functions in this to update the homework table
'''
import classcharts
import datetime
import sqlConnections
import time
import asyncio

async def get_homework(sc):
    await sc.login()

    now = datetime.datetime.now()
    before = now + datetime.timedelta(days=+30)
    after = now + datetime.timedelta(days=-14)

    homework = await sc.homeworks(before=before, after=after)

    await sc.logout()
    time.sleep(0.1)#sleeps for a secound to stop noisy exit on windows
    return homework

def update_database(code):

    sql = sqlConnections.dataConnection()
    date = sql.get_date(code)

    sc = classcharts.StudentClient(code, date)
    homeworks = asyncio.run(get_homework(sc))

    for homework in homeworks:
        sql.add_homework(code, homework.id, homework.issue_date, homework.due_date, homework.status.ticked)
