from django.db import models
from content_agent.models import StrategyRequest

class PostDraft(models.Model):
    strategy = models.ForeignKey(StrategyRequest, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d')})"
