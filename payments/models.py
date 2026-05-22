from django.db import models
from billing.models import Bill
class Payment(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    )
    bill = models.OneToOneField(
        Bill,
        on_delete=models.CASCADE,
        related_name="payment"
    )
    phone_number = models.CharField(
        max_length=15
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return (
            self.transaction_id
            or
            f"Payment {self.id}"
        )