from django import forms
from .models import Investment

class InvestmentForm(forms.ModelForm):
    # Remove PSP-specific fields
    # For example, we previously had stripeToken specific to Stripe, but now we use a generic approach.
    # stripeToken = forms.CharField(widget=forms.HiddenInput())  # Remove this line

    class Meta:
        model = Investment
        fields = ['amount']  # Only include fields related to the investment itself

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        # Add any additional validation needed for the amount or other fields
        if amount <= 0:
            self.add_error('amount', 'The investment amount must be greater than zero.')
        return cleaned_data
