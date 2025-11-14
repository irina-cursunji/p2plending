from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('borrow', views.borrow, name='borrow'),
    path('invest', views.invest, name='invest'),
    path('about-us/', views.about_us, name= 'about_us'),
    path('our-team', views.teams, name= 'teams'),
    path('home', views.home, name= 'home'),
    path('contact/', views.contact, name= 'contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('loan-types/', views.loan_types, name='loan_types'),
    path('check-rates/', views.check_rates, name='check_rates'),
    path('get_started', views.get_started, name = 'get_started'),
    path('team', views.team, name = 'team'),
    path('sign_up', views.sign_up, name = 'sign_up'),
    path('apply_business_loan', views.apply_business_loan, name = 'apply_business_loan'),
    path('apply_personal_loan', views.apply_personal_loan, name = 'apply_personal_loan'),
    path ('benefits_borrowers', views.benefits_borrowers, name = 'benefits_borrowers'),
    path ('benefits_investors', views.benefits_investors, name = 'benefits_investors'),
]
