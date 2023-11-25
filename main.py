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
async def get_all_subscription(page_num: int = 1, page_size: int = 2):
    start = (page_num - 1) * page_size
    end = start + page_size

    command="SELECT * FROM subscriptions"
    conn,cur=connect()
    cur.execute(command)
    result=cur.fetchall()
    response = {
        "data": result[start:end],
        "page_num": page_num,
        "page_size": page_size,
        "pagination": {}
    }

    if end >= len(result):
        response["pagination"]["next"] = None
        if page_num > 1:
            response["pagination"]["previous"] = f"/subscription?page_num={page_num - 1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/subscription?page_num={page_num - 1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"/subscription?page_num={page_num + 1}&page_size={page_size}"
    
    return response

@app.get("/subscription/full")
async def get_full():
    command="SELECT * FROM subscriptions" 
    conn,cur=connect()
    cur.execute(command)
    result=cur.fetchall()
    return result

@app.get("/subscription/{subscription_id}")
async def get_subscription_id(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s" 
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{row} for row in result]

@app.get("/subscription/{subscription_id}/subscriber")
async def subscriber(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"user_id":row[1]} for row in result]

@app.get("/subscription/{subscription_id}/analyst")
async def analyst(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"analyst_id":row[2]} for row in result]

@app.get("/subscription/{subscription_id}/report")
async def report(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"report_id":row[3]} for row in result]

@app.get("/subscription/{subscription_id}/subscription_date")
async def report(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"subscription_date":row[4]} for row in result]

@app.get("/subscription/{subscription_id}/feedback")
async def report_feedback(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"feedback":row[5]} for row in result]

@app.get("/subscription/{subscription_id}/notifications")
async def notification(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"notification":row[6]} for row in result]

@app.get("/subscription/{subscription_id}/activity")
async def activity(subscription_id: str):
    command="SELECT * FROM subscriptions WHERE subscription_id=%s"
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    result=cur.fetchall()
    return [{"activity":row[7]} for row in result]

#create new subscription
@app.post("/subscription/")
async def create_subscription(body=Body(...)):
    subscription_id=body["subscription_id"]
    user_id=body["user_id"]
    analyst_id=body["analyst_id"]
    report_id=body["report_id"]
    subscription_date=body["subscription_date"]
    feedbacks=body["feedbacks"]
    notifications=body["notifications"]
    activity=body["activity"]

    command="""INSERT INTO subscriptions (subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    conn,cur=connect()
    cur.execute(command,(subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity))
    conn.commit()
    return {"Created": body}

#delete subscription basted on subscription id
@app.delete("/subscription/{subscription_id}")
async def delete_subscription(subscription_id: str):
    command="""DELETE FROM subscriptions WHERE subscription_id=%s"""
    conn,cur=connect()
    cur.execute(command,(subscription_id,))
    conn.commit()
    return {"message": "subscription deleted"}

#update database based on subscription id
@app.put("/subscription/")
async def update_subscription(body=Body(...)):
    subscription_id=body["subscription_id"]
    user_id=body["user_id"]
    analyst_id=body["analyst_id"]
    report_id=body["report_id"]
    subscription_date=body["subscription_date"]
    feedbacks=body["feedbacks"]
    notifications=body["notifications"]
    activity=body["activity"]

    command="""UPDATE subscriptions SET user_id=%s, analyst_id=%s, report_id=%s, subscription_date=%s, feedbacks=%s, notifications=%s, activity=%s WHERE subscription_id=%s"""
    conn,cur=connect()
    cur.execute(command,(user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity, subscription_id))
    conn.commit()
    return {"Updated": body}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)

