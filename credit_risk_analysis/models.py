# from django.db import models
# from projects.models import Project
# from decimal import Decimal
# from credit_risk_analysis.services import calculate_credit_risk

# class CreditRiskAssessment(models.Model):
#     project = models.OneToOneField(Project, on_delete=models.CASCADE)
#     financial_health_score = models.DecimalField(max_digits=5, decimal_places=2)
#     credit_history_score = models.DecimalField(max_digits=5, decimal_places=2)
#     business_viability_score = models.DecimalField(max_digits=5, decimal_places=2)
#     macroeconomic_factors_score = models.DecimalField(max_digits=5, decimal_places=2)
#     overall_score = models.DecimalField(max_digits=5, decimal_places=2)
#     risk_level = models.CharField(max_length=50)
#     suggested_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

#     # Macroeconomic factors
#     interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     inflation_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     gdp_growth_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     bond_yield = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"Credit Risk Assessment for {self.project.title}"

#     @classmethod
#     def create_or_update_assessment(cls, project):
#         # Calculate and fetch data
#         try:
#             calculate_credit_risk(project)
#         except Exception as e:
#             print(f"An error occurred while creating/updating assessment: {e}")
