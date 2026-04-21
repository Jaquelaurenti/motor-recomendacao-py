class GetRecommendations:

    def __init__(self, service):
        self.service = service

    def execute(self, user_id: int, n: int = 5):
        return self.service.recommend(user_id, n)