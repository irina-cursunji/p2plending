from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from frontend_pages.models import TeamMember

def index(request):
    """
    View function for rendering homepage
    """
    return render(
        request, 'pages/home.html'
    )

def borrow(request):
    """
    View function for rendering Borrower page
    """
    return render(
        request, 'pages/borrow.html'
    )

def invest(request):
    """
    View function for rendering Invest page
    """
    return render(
        request, 'pages/invest.html'
    )

def about_us(request):
    """
    View function for rendering about us page 
    """

    team_members = TeamMember.objects.all()

    context = {'team_id' : team_members}
    
    return render(
        request, 'pages/about.html', context    
    )

def teams(request):
    """
    View function for rendering our teams page
    """
    return render(
        request, 'pages/index.html'
    )

def home(request):
    """
    View function for rendering our home page
    """
    return render(
        request, 'pages/home.html'
    )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Ensure all fields are filled out
        if name and email and message:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=['maxwell.koulen@outlook.com'],  # Replace with p2plending's email later
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill out all fields.')
        
        return redirect('contact')

    return render(request, 'pages/contact.html')

def privacy_policy(request):
    return render(
        request, 'pages/privacy_policy.html')
def terms_of_service(request):
    return render(
        request, 'pages/terms_of_service.html'
    )
def how_it_works(request):
    return render(
        request, 'pages/how_it_works.html'
    )
def loan_types(request):
    return render(
        request, 'pages/loan_types.html'
    )
def check_rates(request):
    return render(
        request, 'pages/check_rates.html'
    )

def benefits_investors(request):
    return render(
        request, 'pages/benefits-investors.html'
    )

def benefits_borrowers(request):
    return render(
        request, 'pages/benefits-borrowers.html'
    )

def get_started(request):
    return render(
        request, 'pages/get_started.html'
    )

def team(request):
    return render(
        request, 'pages/team.html'
    )

def sign_up(request):
    return render(
        request, 'pages/sign-up.html'
    )

def apply_business_loan(request):
    return render(
        request, 'pages/apply_business_loan.html'
    )

def apply_personal_loan(request):
    return render(
        request, 'pages/apply_personal_loan.html'
    )
