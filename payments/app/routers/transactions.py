from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from db import db
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix="/transactions", tags=["transactions"])


class TxnIn(BaseModel):
    account_number: str
    amount_cents: int = Field(..., description="> 0 for debit, < 0 for credit")
    memo: str | None = None


@router.post("/", status_code=201)
async def create_txn(txn: TxnIn):
    doc = txn.model_dump()
    res = await db.transactions.insert_one(doc)
    # out = {"id": str(res.inserted_id), **doc}
    created_doc = await db.transactions.find_one({"_id": res.inserted_id})
    created_doc["_id"] = str(created_doc["_id"])
    return created_doc


@router.get("/")
async def list_txns():
    txns = await db.transactions.find().to_list(100)
    for t in txns:
        t["_id"] = str(t["_id"])
    return txns
