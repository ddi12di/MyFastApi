from fastapi import FastAPI

from conroller.routes import controller_user_router
from View.routes import view_user_router

app = FastAPI()

app.include_router(controller_user_router)
app.include_router(view_user_router)