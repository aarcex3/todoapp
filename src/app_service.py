class AppService:
    """
    App service
    """

    def __init__(self):
        self.app_name = "Todo App"
        self.app_version = "1.0.0"

    def get_app_info(self):
        """Get app info"""
        return {"app_name": self.app_name, "app_version": self.app_version}


app_service = AppService()
