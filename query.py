from typing import List
import strawberry
from db.connectdb import connect
from schema import DataType


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello SkyCastle Team"
    
    @strawberry.field
    def filter_through_subscription(self, subscription_id: int) -> List[DataType]:
        command="SELECT * FROM subscriptions WHERE subscription_id=%s"
        conn,cur=connect()
        cur.execute(command,(subscription_id,))
        result=cur.fetchall()
        return [DataType(subscription_id=row[0], subscriber_id=row[1], analyst_id=row[2], report_id=row[3], subscription_date=row[4], feedback=row[5], notification=row[6], activity=row[7]) for row in result]
    
    @strawberry.field
    def filter_through_user(self, user_id: int) -> List[DataType]:
        command="SELECT * FROM subscriptions WHERE user_id=%s"
        conn,cur=connect()
        cur.execute(command,(user_id,))
        result=cur.fetchall()
        return [DataType(subscription_id=row[0], subscriber_id=row[1], analyst_id=row[2], report_id=row[3], subscription_date=row[4], feedback=row[5], notification=row[6], activity=row[7]) for row in result]
    
    @strawberry.field
    def filter_through_report(self, report_id: int) -> List[DataType]:
        command="SELECT * FROM subscriptions WHERE report_id=%s"
        conn,cur=connect()
        cur.execute(command,(report_id,))
        result=cur.fetchall()
        return [DataType(subscription_id=row[0], subscriber_id=row[1], analyst_id=row[2], report_id=row[3], subscription_date=row[4], feedback=row[5], notification=row[6], activity=row[7]) for row in result]
    