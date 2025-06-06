from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    """
    expose Expense model fields
    """
    class Meta:
        model = Expense
        fields = ['pk', 'name', 'amount', 'timestamp', 'category']