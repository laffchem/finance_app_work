from django.urls import path
import budget.views as views

urlpatterns = [
    path("accounts/", views.list_accounts, name="list_accounts"),
    path("transactions/", views.list_transactions, name="transactions"),
    path("transfer/", views.transfer_funds, name="transfer_funds"),
]
