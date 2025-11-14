from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'goal_amount',
            'funding_start_date',
            'funding_end_date',
            'location',
            'business_plan',
            'video_presentation',
            'contact_email',
            'contact_phone',
            'current_assets',
            'current_liabilities',
            'total_liabilities',
            'shareholders_equity',
            'revenue',
            'cost_of_goods_sold',
            'net_income',
            # New fields
            'risk_description',
            'kiis_document',
            'fees_description',
            'use_of_proceeds',
            'image',  # New field for image
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your project'}),
            'goal_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter the funding goal'}),
            'funding_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'funding_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of the project'}),
            'business_plan': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'video_presentation': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +123456789'}),
            'current_assets': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter current assets'}),
            'current_liabilities': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter current liabilities'}),
            'total_liabilities': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter total liabilities'}),
            'shareholders_equity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter shareholders equity'}),
            'revenue': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter revenue'}),
            'cost_of_goods_sold': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter cost of goods sold'}),
            'net_income': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter net income'}),
            # Widgets for new fields
            'risk_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe project risks'}),
            'kiis_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'fees_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe fees and costs'}),
            'use_of_proceeds': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Explain the use of funds'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Widget for image upload
        }

    # Existing clean methods for validation
    def clean_goal_amount(self):
        goal_amount = self.cleaned_data.get('goal_amount')

        if goal_amount is None or goal_amount == '':
            raise forms.ValidationError('Goal amount is required.')

        if goal_amount <= 0:
            raise forms.ValidationError('Goal amount must be greater than zero.')

        return goal_amount   

    def clean_funding_end_date(self):
        funding_end_date = self.cleaned_data.get('funding_end_date')
        funding_start_date = self.cleaned_data.get('funding_start_date')

        if funding_end_date and funding_start_date:
            if funding_end_date <= funding_start_date:
                raise forms.ValidationError("Funding end date must be after the funding start date.")
        return funding_end_date

    def clean_current_assets(self):
        current_assets = self.cleaned_data.get('current_assets')
        if current_assets is None or current_assets < 0:
            raise forms.ValidationError('Current assets must be a non-negative number.')
        return current_assets

    def clean_current_liabilities(self):
        current_liabilities = self.cleaned_data.get('current_liabilities')
        if current_liabilities is None or current_liabilities < 0:
            raise forms.ValidationError('Current liabilities must be a non-negative number.')
        return current_liabilities

    def clean_total_liabilities(self):
        total_liabilities = self.cleaned_data.get('total_liabilities')
        if total_liabilities is None or total_liabilities < 0:
            raise forms.ValidationError('Total liabilities must be a non-negative number.')
        return total_liabilities

    def clean_shareholders_equity(self):
        shareholders_equity = self.cleaned_data.get('shareholders_equity')
        if shareholders_equity is None or shareholders_equity < 0:
            raise forms.ValidationError('Shareholders equity must be a non-negative number.')
        return shareholders_equity

    def clean_revenue(self):
        revenue = self.cleaned_data.get('revenue')
        if revenue is None or revenue <= 0:
            raise forms.ValidationError('Revenue must be greater than zero.')
        return revenue

    def clean_cost_of_goods_sold(self):
        cost_of_goods_sold = self.cleaned_data.get('cost_of_goods_sold')
        if cost_of_goods_sold is None or cost_of_goods_sold < 0:
            raise forms.ValidationError('Cost of goods sold must be a non-negative number.')
        return cost_of_goods_sold

    def clean_net_income(self):
        net_income = self.cleaned_data.get('net_income')
        if net_income is None or net_income < 0:
            raise forms.ValidationError('Net income must be a non-negative number.')
        return net_income
