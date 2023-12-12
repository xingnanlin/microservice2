import strawberry


@strawberry.type
class DataType:
    subscription_id: int
    subscriber_id: int
    analyst_id: int
    report_id: int
    subscription_date: str
    feedback: str
    notification: str
    activity: str
