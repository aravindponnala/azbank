from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import Account, LedgerEntry
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by("-id")
    serializer_class = AccountSerializer

    @action(detail=True, methods=["post"])
    def deposit(self, request, pk=None):
        print(request.data)
        amount = int(request.data.get("amount_cents", 0))
        if amount <= 0:
            return Response({"error": "Amount must be > 0"}, status=400)
        with transaction.atomic():
            account = self.get_object()
            account.balance_cents += amount
            account.save()
            LedgerEntry.objects.create(
                account=account, amount_cents=amount, memo="deposit"
            )
        return Response(AccountSerializer(account).data)
