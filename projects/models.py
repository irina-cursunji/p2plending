import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from p2plending.users.models import User

from decimal import Decimal


class Project(models.Model):
    # Unique identifier for the project, automatically generated and not editable
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Choices for the risk level of the project
    RISK_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    # Choices for the status of the project
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ]

    # Foreign key linking to the user who is borrowing or presenting the project
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Title of the project
    title = models.CharField(max_length=255)
    
    # Detailed description of the project
    description = models.TextField()
    
    # Target amount needed for the project
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    
    # Dates for the funding period
    funding_start_date = models.DateField(blank=True, null=True)
    funding_end_date = models.DateField(blank=True, null=True)
    
    # Location where the project will take place
    location = models.CharField(max_length=255, blank=True, null=True)
    
    # Risk level associated with the project
    risk_level = models.CharField(max_length=50, choices=RISK_LEVEL_CHOICES, blank=True, null=True)
    
    # Detailed description of the risks involved in the project
    risk_description = models.TextField(blank=True, null=True)  # New field for detailed risk information
    
    # Current status of the project
    project_status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    
    # File field to upload the business plan
    business_plan = models.FileField(upload_to='business_plans/', blank=True, null=True)
    
    # URL of a video presentation for the project
    video_presentation = models.URLField(max_length=200, blank=True, null=True)
    
    # Contact email for inquiries
    contact_email = models.EmailField(blank=True, null=True)
    
    # Contact phone number for inquiries
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Timestamps for when the project was created and last updated
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Financial fields
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    repayment_frequency = models.CharField(max_length=50, blank=True, null=True)
    repayment_period = models.PositiveIntegerField(blank=True, null=True)
    
    # Image associated with the project
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    # KIIS (Key Information Summary) document for the project
    kiis_document = models.FileField(upload_to='kiis_documents/', blank=True, null=True)  # New field for KIIS document
    
    # Description of any fees associated with the project
    fees_description = models.TextField(blank=True, null=True)  # New field for fees and costs
    
    # Explanation of how the funds will be used
    use_of_proceeds = models.TextField(blank=True, null=True)  # New field for use of proceeds

    # Every project needs to be approved before getting on the official project list
    is_approved = models.BooleanField(default=False)

    # Financial data fields for detailed financial information
    current_assets = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    current_liabilities = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_liabilities = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    shareholders_equity = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cost_of_goods_sold = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    net_income = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically set contact email to the borrower's email if not provided
        if not self.contact_email and self.borrower:
            self.contact_email = self.borrower.email
        super().save(*args, **kwargs)


class Investment(models.Model):
    # Foreign key linking to the user who is investing in the project
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='investment_set_projects')
    
    # Foreign key linking to the project in which the investment is made
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='investments_in_projects')
    
    # Amount invested in the project
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Timestamp for when the investment was made
    date_invested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.investor.username} invested in {self.project.title}'
    

class CreditRiskAssessment(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    financial_health_score = models.DecimalField(max_digits=5, decimal_places=2)
    credit_history_score = models.DecimalField(max_digits=5, decimal_places=2)
    business_viability_score = models.DecimalField(max_digits=5, decimal_places=2)
    macroeconomic_factors_score = models.DecimalField(max_digits=5, decimal_places=2)
    overall_score = models.DecimalField(max_digits=5, decimal_places=2)
    risk_level = models.CharField(max_length=50)
    suggested_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    # Macroeconomic factors
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    inflation_rate = models.DecimalField(max_digits=5, decimal_places=2)
    gdp_growth_rate = models.DecimalField(max_digits=5, decimal_places=2)
    unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    bond_yield = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Credit Risk Assessment for {self.project.title}"

    @classmethod
    def create_or_update_assessment(cls, project):
        from credit_risk_analysis.services import calculate_credit_risk  # Local import to avoid circular dependency
        # Calculate and fetch data
        try:
            calculate_credit_risk(project)
        except Exception as e:
            print(f"An error occurred while creating/updating assessment: {e}")

