from django.db import models
from users.models import User

class Doctor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username