from django.db import models

# Create your models here.
class Payment(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('not-paid', 'Not-Paid'),
    ]
    eid=models.CharField(max_length=100,unique=True)
    totalAmount=models.FloatField(default=0)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Not-Paid'
    )
    utr=models.CharField(max_length=200,default="")
