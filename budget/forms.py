from .models import Account, ProjectCode, Transaction
from django import forms


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
