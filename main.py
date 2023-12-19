from fastapi import FastAPI, Response, Body, status
import uvicorn
from resources.students import StudentsResource
from db.connectdb import connect
from strawberry.fastapi import GraphQLRouter
import strawberry
from query import Query
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello SkyCastle Team"}

# add graphql endpoint
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

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
async def all_subscription():
    command="SELECT * FROM subscriptions" 
    conn,cur=connect()
    cur.execute(command)
    result=cur.fetchall()
    return [{row} for row in result]

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

#create new subscription
@app.post("/subscription/{user_id}/{report_id}")
async def create_subscription(user_id: str, report_id: str):
    command="SELECT subscription_id FROM subscriptions" 
    conn,cur=connect()
    cur.execute(command)
    result=cur.fetchall()
    result=[row[0] for row in result]

    while True:
        subscription_id=random.randint(1,50)
        if subscription_id not in result:
            break

    user_id=user_id
    analyst_id="1"
    report_id=report_id
    subscription_date="Dec 18, 2023"
    feedbacks="feedbacks"
    notifications="notifications"
    activity="activity"

    command="""INSERT INTO subscriptions (subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    conn,cur=connect()
    cur.execute(command,(subscription_id, user_id, analyst_id, report_id, subscription_date, feedbacks, notifications, activity))
    conn.commit()
    return {"Created subscription": subscription_id}

@app.delete("/subscription/{report_id}")
async def delete_subscription_(report_id: str):
    command="""SELECT * FROM subscriptions WHERE report_id=%s"""
    conn,cur=connect()
    cur.execute(command,(report_id,))
    result=cur.fetchall()
    command="""DELETE FROM subscriptions WHERE report_id=%s"""
    conn,cur=connect()
    cur.execute(command,(report_id,))
    conn.commit()
    return [{"Deleted subscription_id":row[0],"user_id":row[1]} for row in result]


@app.delete("/subscription/{user_id}/{report_id}")
async def delete_subscription_(user_id: str, report_id: str):
    command="""SELECT * FROM subscriptions WHERE user_id=%s and report_id=%s"""
    conn,cur=connect()
    cur.execute(command,(user_id,report_id,))
    result=cur.fetchall()
    command="""DELETE FROM subscriptions WHERE user_id=%s and report_id=%s"""
    conn,cur=connect()
    cur.execute(command,(user_id,report_id,))
    conn.commit()
    return {"Deleted subscription": result[0][0]}

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

@app.get("/subscription/user/{user_id}")
async def get_user_subscription(user_id: str):
    command="SELECT * FROM subscriptions WHERE user_id=%s" 
    conn,cur=connect()
    cur.execute(command,(user_id,))
    result=cur.fetchall()
    print(result)
    return "report id: ",[{row[3]} for row in result]


@app.get("/subscription/report/{report_id}")
async def get_report_users(report_id: str):
    command="SELECT * FROM subscriptions WHERE report_id=%s" 
    conn,cur=connect()
    cur.execute(command,(report_id,))
    result=cur.fetchall()
    return "user id: ",[{row[1]} for row in result]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)

