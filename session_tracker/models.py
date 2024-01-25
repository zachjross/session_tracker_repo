from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    """The name of the client."""
    client_name = models.CharField(max_length=100)
    sessions = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name