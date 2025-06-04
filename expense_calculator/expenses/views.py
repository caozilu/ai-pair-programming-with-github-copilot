from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer

# Create your views here.
class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
