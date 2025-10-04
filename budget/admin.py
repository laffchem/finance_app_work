from django.contrib import admin
from .models import Account, ProjectCode, Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(ProjectCode)
admin.site.register(Transaction)
