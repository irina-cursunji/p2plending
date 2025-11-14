from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Project
from .services import calculate_credit_risk

@receiver(post_save, sender=Project)
def analyze_credit_risk(sender, instance, created, **kwargs):
    if created:
        # Call your function to perform the credit risk analysis
        calculate_credit_risk(instance)