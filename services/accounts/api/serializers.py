from rest_framework import serializers
from .models import Account, LedgerEntry


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "number", "balance_cents", "currency", "created_at"]


class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerEntry
        fields = ["id", "account", "amount_cents", "memo", "created_at"]
