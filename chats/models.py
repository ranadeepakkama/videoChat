from django.db import models
from datetime import datetime 

# Create your models here.
class NewMember(models.Model):
    name = models.CharField(max_length=100)
    uid = models.CharField(max_length = 200)
    room_name = models.CharField(max_length=100)
    modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
