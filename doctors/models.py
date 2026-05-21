from django.db import models
from users.models import User


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(
        max_length=100,
        default="General"
    )

    department = models.CharField(
        max_length=100,
        default="General"
    )

    experience_years = models.IntegerField(
        default=0
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    available = models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.user.username