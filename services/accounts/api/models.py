from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=32, unique=True)
    balance_cents = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=3, default="USD")
    created_at = models.DateTimeField(auto_now_add=True)


class LedgerEntry(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="entries"
    )
    amount_cents = models.BigIntegerField()  # + or - values
    memo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
