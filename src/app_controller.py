from fastapi import APIRouter

from src.app_service import app_service


class AppController:
    """
    App controller
    """

    def __init__(self):
        self.service = app_service
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/")
        async def get_app_info():
            """Root endpoint"""
            return self.service.get_app_info()


app_controller = AppController()
