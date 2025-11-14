

from django.db import models
from p2plending.users.models import User
from projects.models import Project
from django.conf import settings
from django.db import models

class Investment(models.Model):
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_invested = models.DateTimeField(auto_now_add=True)
    invested_at = models.DateTimeField(auto_now_add=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Interest rate for the investment


    def __str__(self):
        return f'{self.investor.username} invested in {self.project.title}'



class Repayment(models.Model):
    investment = models.ForeignKey(Investment, related_name='repayments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Repayment of {self.amount} for {self.investment.project.title}"

