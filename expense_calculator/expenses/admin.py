from django.contrib import admin

from .models import Expense

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    this is the admin interface for the Expense model
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    """
    list_display = ('name', 'amount', 'timestamp', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('timestamp',)