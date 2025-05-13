from django.db import models

# Create your models here.
from django.db import models

class Paste(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title or "Untitled"
