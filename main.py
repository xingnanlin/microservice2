from fastapi import FastAPI, Response
import uvicorn
from resources.students import StudentsResource
from db.connectdb import connect

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
    return [{"subscription_id":row[0]} for row in result]

@app.get("/subscription/{subscription_id}/subscriber")
async def subscriber(subscription_id: str):
    return {"GET the subscriber specific to unique subscription id"}

@app.get("/subscription/{subscription_id}/analyst")
async def analyst(subscription_id: str):
    return {"GET the analyst specific to unique subscription id"}

@app.get("/subscription/{subscription_id}/report")
async def report(subscription_id: str):
    return {"GET the report specific to unique subscription id"}

@app.get("/subscription/{subscription_id}/report/feedback")
async def report_feedback(subscription_id: str):
    return {"GET feedbacks for reports specific to unique subscription id"}

@app.get("/subscription/{subscription_id}/notifications")
async def notification(subscription_id: str):
    return {"GET list of notification preferences specific to unique subscription id"}

@app.get("/subscription/{subscription_id}/activity")
async def activity(subscription_id: str):
    return {"GET activity logs or history specific to unique subscription id"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
