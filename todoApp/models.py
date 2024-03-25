from django.db import models
from users.models import Profile 

import uuid

# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank= True)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True )

    def __str__(self):
        return self.title
    