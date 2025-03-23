from django.db import models


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Expense Categories"

class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Income Categories"
      
class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    description = models.TextField(default=None, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.ImageField(upload_to='receipts/', default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    

class Income(models.Model):
    date = models.DateField()
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    description = models.TextField(default=None, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    receipt = models.ImageField(upload_to='receipts/', default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
