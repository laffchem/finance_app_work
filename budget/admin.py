from django.contrib import admin
from .models import Account, ProjectCode, Transaction
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'balance', 'department']
    list_filter = ['type', 'department']
    search_fields = ['id', 'name', 'type']


@admin.register(ProjectCode)
class ProjectCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'description']
    search_fields = ['code', 'description']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_account_name', 'date', 'amount', 'description', 'category', 'project_code']
    list_filter = ['date', 'category', 'project_code']
    search_fields = ['id', 'description']
    date_hierarchy = 'date'
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    def get_account_name(self, obj):
        if isinstance(obj.account, dict):
            return obj.account.get('name', 'Unknown Account')
        return str(obj.account)
    get_account_name.short_description = 'Account'
