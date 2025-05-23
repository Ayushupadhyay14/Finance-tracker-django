from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# It is used to create a database for a data model and create a table in the database.
# Database name: SQLite-3


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('Income', 'Income'),
        ('Expence', 'Expence'),
        ('Transfer', 'Transfer'),
        ('Investment', 'Investment'),
        ('Loan Payment', 'Loan Payment')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=15,
                                        choices=TRANSACTION_TYPE)
    date = models.DateField()
    category = models.CharField(max_length=355)
