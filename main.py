from fastapi import FastAPI, Response, Body, status
import uvicorn
from resources.students import StudentsResource
from db.connectdb import connect
import uuid

app = FastAPI()

students_resource = StudentsResource()


@app.get("/")
async def root():
    return {"message": "Hello SkyCastle Team"}

@app.get("/subscription/")
async def get_all_subscription():
    command="SELECT * FROM subscriptions"
    conn,cur=connect()
    cur.execute(command)
    result=cur.fetchall()
    return [{"subscription_id":row[0]} for row in result]

@app.get("/subscription/{subscription_id}")
async def get_subscription_id(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s" 
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{row} for row in result]

@app.get("/subscription/{subscription_id}/subscriber")
async def subscriber(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[1]} for row in result]

@app.get("/subscription/{subscription_id}/analyst")
async def analyst(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[2]} for row in result]

@app.get("/subscription/{subscription_id}/report")
async def report(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[3]} for row in result]

@app.get("/subscription/{subscription_id}/feedback")
async def report_feedback(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[4]} for row in result]

@app.get("/subscription/{subscription_id}/notifications")
async def notification(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[5]} for row in result]

@app.get("/subscription/{subscription_id}/activity")
async def activity(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    result=cur.fetchall()
    return [{"subscriber_id":row[6]} for row in result]

#create new subscription
@app.post("/subscription/")
async def create_subscription(body=Body(...)):
    subscription_id=body["subscription_id"]
    subscriber_id=body["subscriber_id"]
    analyst_id=body["analyst_id"]
    report_id=body["report_id"]
    feedbacks=body["feedbacks"]
    notifications=body["notifications"]
    activity=body["activity"]

    command="""INSERT INTO subscriptions (subscription_id, subscriber_id, analyst_id, report_id, feedbacks, notifications, activity) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    conn,cur=connect()
    cur.execute(command,(subscription_id, subscriber_id, analyst_id, report_id, feedbacks, notifications, activity))
    conn.commit()
    return {"Updated": body}

#delete subscription basted on subscription id
@app.delete("/subscription/{subscription_id}")
async def delete_subscription(subscription_id: str):
    command="""DELETE FROM subscriptions WHERE subscription_id=%s"""
    conn,cur=connect()
    cur.execute(command,(subscription_id))
    conn.commit()
    return {"message": "subscription deleted"}

#update database based on subscription id
@app.put("/subscription/")
async def update_subscription(body=Body(...)):
    subscription_id=body["subscription_id"]
    subscriber_id=body["subscriber_id"]
    analyst_id=body["analyst_id"]
    report_id=body["report_id"]
    feedbacks=body["feedbacks"]
    notifications=body["notifications"]
    activity=body["activity"]

    command="""UPDATE subscriptions SET subscriber_id=%s, analyst_id=%s, report_id=%s, feedbacks=%s, notifications=%s, activity=%s WHERE subscription_id=%s"""
    conn,cur=connect()
    cur.execute(command,(subscriber_id, analyst_id, report_id, feedbacks, notifications, activity, subscription_id))
    conn.commit()
    return {"Updated": body}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
