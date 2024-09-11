from django.db import models

class ContentCreaterModel(models.Model):
    platform = models.CharField(max_length=100)
    description = models.TextField()
    min_word_length = models.IntegerField(max_length=5)
    max_word_length = models.IntegerField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
