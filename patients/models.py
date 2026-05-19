from django.db import models
from users.models import User

class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    blood_group = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username