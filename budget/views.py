from django.shortcuts import render
from .forms import TransactionForm


# Create your views here.
def list_accounts(request):
    return render(request, "budget/accounts.html", {})


def list_transactions(request):
    return render(request, "budget/transactions.html", {})


def transfer_funds(request):
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            form = TransactionForm()  # Reset the form after saving
    return render(request, "budget/transfers.html", {"form": form})
