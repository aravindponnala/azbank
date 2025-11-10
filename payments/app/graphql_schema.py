import strawberry
from strawberry.types import Info
from bson import ObjectId
from db import db


@strawberry.type
class Transaction:
    id: str
    account_number: str
    amount_cents: int


memo: str | None


@strawberry.type
class Query:
    @strawberry.field
    async def transactions(self, info: Info, account_number: str) -> list[Transaction]:
        cursor = db.transactions.find({"account_number": account_number}).sort(
            "_id", -1
        )
        items = []
        async for d in cursor:
            items.append(
                Transaction(
                    id=str(d["_id"]),
                    account_number=d["account_number"],
                    amount_cents=d["amount_cents"],
                    memo=d.get("memo"),
                )
            )
        return items


schema = strawberry.Schema(query=Query)
