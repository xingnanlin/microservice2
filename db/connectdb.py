import psycopg2
import uuid

def connect():
    conn=psycopg2.connect(
        host="microservice.cyzurhix8mmm.us-east-1.rds.amazonaws.com",
        port="5432",
        user="postgres",
        password="microservice2"
    )
    cur=conn.cursor()
    return conn,cur

conn,cur=connect()

#create a table
# command="""CREATE TABLE IF NOT EXISTS subscriptions (subscription_id INT PRIMARY KEY, user_id INT, analyst_id INT, report_id INT, subscription_date VarChar(255), feedbacks VarChar(255), notifications VarChar(255), activity VarChar(255))"""
# cur.execute(command)
# conn.commit()

#insert data
# subscription_id=1
# user_id=0
# report_id=8
# analyst_id=1
# subscription_date="Nov 22, 2023"
# feedbacks="feedbacks: None"
# notifications="notifications: None"
# activity="activity: None"

# command="""INSERT INTO subscriptions (subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
# cur.execute(command,(subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity))
# conn.commit()

#fetch database
# command="""SELECT * FROM subscriptions"""
# cur.execute(command)
# result=cur.fetchall()
# print(result)

#delete data
# command="""DELETE FROM subscriptions WHERE subscription_id=%s"""
# cur.execute(command,("1"))
# conn.commit()

#delete table
# command="""DROP TABLE subscriptions"""
# cur.execute(command)
# conn.commit()

