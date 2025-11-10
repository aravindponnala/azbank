from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from graphql_schema import schema
from routers.transactions import router as txn_router


app = FastAPI(title="Payments Service")
app.include_router(txn_router)
app.include_router(GraphQLRouter(schema), prefix="/graphql")
