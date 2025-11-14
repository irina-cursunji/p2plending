from django.shortcuts import render, get_object_or_404, redirect
from .models import Investment, Repayment
from projects.models import Project
from .forms import InvestmentForm
from django.conf import settings
from datetime import datetime, timedelta

# Abstract payment processing class
class PaymentProcessor:
    @staticmethod
    def process_payment(amount, token, description):
        """
        Process the payment using the payment service provider.
        This method should be overridden by the actual PSP integration.
        """
        raise NotImplementedError("You need to implement the payment processing method.")

# Example PSP integration (e.g., Stripe)
class StripePaymentProcessor(PaymentProcessor):
    @staticmethod
    def process_payment(amount, token, description):
        import stripe
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        
        try:
            stripe.Charge.create(
                amount=int(amount * 100),  # Amount in cents
                currency='usd',
                description=description,
                source=token
            )
        except stripe.error.StripeError as e:
            # Handle Stripe error (e.g., log error, notify user)
            raise e

def invest_in_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            token = form.cleaned_data.get('stripeToken')  # Payment token (generic)

            # Process payment using the selected PSP
            try:
                # Use StripePaymentProcessor or any other PSP processor
                PaymentProcessor.process_payment(amount, token, f'Investment in {project.title}')
            except Exception as e:
                # Handle payment processing errors
                return render(request, 'investments/investment_form.html', {
                    'form': form,
                    'project': project,
                    'error': str(e)
                })

            # Save the investment
            investment = form.save(commit=False)
            investment.project = project
            investment.investor = request.user
            investment.save()

            # Update project amount
            project.current_amount += investment.amount
            project.save()

            # Calculate and create repayment schedule
            repayment_start_date = datetime.now() + timedelta(days=30)  # Assuming monthly repayments start after 1 month
            frequency_days = {'monthly': 30, 'quarterly': 90}.get(project.repayment_frequency, 30)
            
            for i in range(project.repayment_period):
                repayment_date = repayment_start_date + timedelta(days=i * frequency_days)
                repayment_amount = (investment.amount * (1 + investment.interest_rate / 100)) / project.repayment_period
                Repayment.objects.create(
                    investment=investment,
                    amount=repayment_amount,
                    repayment_date=repayment_date
                )

            return redirect('projects:project_detail', pk=pk)
    else:
        form = InvestmentForm()

    return render(request, 'investments/investment_form.html', {'project': project, 'form': form})

def investment_details(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    return render(request, 'investments/investment_details.html', {'investment': investment})

def user_investments(request):
    investments = Investment.objects.filter(investor=request.user)
    return render(request, 'investments/user_investments.html', {'investments': investments})
