import math
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_top_customers(cls):
        six_months_ago_date = timezone.now() - timedelta(
            days=180
        )  # 6 months = 180 days so, present day - 180 days
        return (
            cls.objects.filter(order_date__gte=six_months_ago_date)
            .values("customer")
            .annotate(total_spent=models.Sum("total_amount"))
            .order_by("-total_spent")[:5]
        )

    def __str__(self):
        return self.customer.username
