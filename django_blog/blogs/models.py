from django.db import models


class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
