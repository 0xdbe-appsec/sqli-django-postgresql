from django.db import models

class Task(models.Model):
  description = models.TextField()
  owner = models.TextField(max_length = 40)