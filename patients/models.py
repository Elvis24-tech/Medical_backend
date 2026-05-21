from django.db import models
from users.models import User


class Patient(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    age = models.IntegerField(
        default=0
    )

    gender = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    blood_group = models.CharField(
        max_length=10,
        blank=True
    )

    emergency_contact = models.CharField(
        max_length=15,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.user.username