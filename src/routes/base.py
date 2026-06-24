from fastapi import APIRouter ,FastAPI,Depends
import os
from helpers.config import get_settings,settings


base_router = APIRouter(
    prefix="/api/v1",
    tags=["/api_v1"]
)
@base_router.get("/")

async def welcome(app_settings:settings =Depends(get_settings)):
    app_name = app_settings.app_name
    app_version = app_settings.app_version
    return {
        "message" : "Welcome to PDF RAG ya maioio",
        "app_name" : app_name,
        "app_version" : app_version
    }   