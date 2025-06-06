from rest_framework.test import APITestCase
from .models import Expense

# Create your tests here.
"""
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # category choice field
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.amount}"
"""
class ExpenseAPITestCase(APITestCase):
    def setUp(self):
        Expense.objects.bulk_create([
            Expense(name='Food', amount=10.00, category='Food'),
            Expense(name='Transport', amount=20.00, category='Transport'),
            Expense(name='Entertainment', amount=30.00, category='Entertainment'),
        ])

    def test_expense_list(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_expense_detail(self):
        expense = Expense.objects.first()
        response = self.client.get(f'/api/expenses/{expense.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], expense.name)
        self.assertEqual(response.data['amount'], str(expense.amount))
        self.assertEqual(response.data['category'], expense.category)
        
    def test_expense_create(self):
        data = {
            'name': 'Test Expense',
            'amount': '50.00',
            'category': 'Food'
        }
        response = self.client.post('/api/expenses/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test Expense')
    
    def test_expense_update(self):
        expense = Expense.objects.first()
        data = {
            'name': 'Updated Expense',
            'amount': '75.00',
            'category': 'Food'
        }
        response = self.client.put(f'/api/expenses/{expense.pk}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Expense')
        self.assertEqual(response.data['amount'], '75.00')

    def test_expense_delete(self):
        expense = Expense.objects.first()
        response = self.client.delete(f'/api/expenses/{expense.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Expense.objects.filter(pk=expense.pk).exists())

    def tearDown(self):
        Expense.objects.all().delete()