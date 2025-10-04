from django.db import models


# Create your models here.
class Account(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.name} ({self.type}) - Balance: {self.balance}"


class ProjectCode(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.description}"


class Transaction(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    account = models.JSONField()  # Storing account details as JSON
    project_code = models.ForeignKey(
        ProjectCode, on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description}: {self.amount} (Account: {self.account.name})"
