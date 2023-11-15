import psycopg2

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
#command="""CREATE TABLE IF NOT EXISTS subscriptions (subscription_id VARCHAR(255) PRIMARY KEY, analyst_id VARCHAR(255), report_id VARCHAR(255), feedbacks VarChar(255), notifications VarChar(255), activity VarChar(255))"""
#cur.execute(command)
#conn.commit()

#insert data
#command="""INSERT INTO subscriptions (subscription_id, analyst_id, report_id, feedbacks, notifications, activity) VALUES (%s, %s, %s, %s, %s, %s)"""
#cur.execute(command,("4","4","4","feedbacks","notifications","activity"))
#conn.commit()

#fetch database
#command="""SELECT * FROM subscriptions"""
#cur.execute(command)
#result=cur.fetchall()
#print(result)