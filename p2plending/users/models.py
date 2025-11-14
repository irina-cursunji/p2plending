
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from locations.models import Country

from .managers import UserManager
from django.db import models
import uuid

from django.utils import timezone

class Useraddress (models.Model):
   #CHOICES
   ADDRESS_TYPE = (
       ('current', _("Current Address")),
       ('permanet', _("Permanent Address"))
   )
   id = models .UUIDField(
       default=uuid.uuid4,
       editable=False,
       primary_key=True,
       help_text=_("The unique identifier of the customer.")
   )

   type = models.CharField(
       choices=ADDRESS_TYPE,
       max_length=9,
       help_text=_("The type of adress"),
       default='current',
       verbose_name=_("Address type"),
   )


   user = models.ForeignKey(
       'User',
       verbose_name=_("User Profile"),
       on_delete=models.PROTECT,
       help_text=_("The user for whome address belongs to")

   )
   address_line_1 = models.CharField(
       max_length=50,
       verbose_name=_("Address line 1"),
       help_text=_('Adress line 1 of the user'))
   
   address_line_2 = models.CharField(
       max_length=50,
       verbose_name=_("Address line 2"),
       blank=True, null=True,
       help_text=_('Adress line 2 of the user'))
   
   state = models.CharField(
       max_length=50,
       verbose_name=_("State or Region"),
       help_text=_('Adress line 1 of the user'))
   
   city = models.CharField(
       max_length=50,
       verbose_name=_("City"),
       help_text=_('The city of the address of the user'))
   
   zip_post_code = models.CharField(
       verbose_name=_("Zip Code"),
       max_length=20,
       help_text=_('The zip or postal code of the address of the user'))
   
   country = models.ForeignKey(
       Country,
       max_length=50,
       verbose_name=_("Country"),
       on_delete=models.PROTECT,
       help_text=_('Adress line 1 of the user'))

   
   #Metadata
   class Meta :
        verbose_name = _("User address")
        verbose_name_plural = ("User addresses")


   #Methods
   def get_absolute_url(self):
       return reverse('url', args=[args])

   def __str__(self):
       return self.user.first_name


class User(AbstractUser):
    """
    Default custom user model for p2plending.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #objects = UserManager()

    #USER CHOICES
    KYC_STATUS = ( #should it be KYC_STATUS ?
        ('unverified', _ ('Unverified')),
        ('pending', _ ('Pending')),
        ('verified', _ ('Verified')),
        ('action_required', _ ('Action Required')),
        ('cancelled', _ ('Cancelled')),
        ('rejected', _ ('Rejected/Refused')),
    )

    ACCOUNT_TYPE = (
        ('borrower', _('Borrower')),
        ('investor', _('Investor'))
    )
    # First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifer of the customer.")
    )

    account_type = CharField(
        _("Account Type"),
        choices=ACCOUNT_TYPE,
        max_length=8,
        default='investor',
        blank=True, null=True,
        help_text=_("The account type of the user.")
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(
        max_length=150,
        verbose_name=_("Email Address"),
        help_text=_("The email adreess of the customer"),
        unique=True
    )
    
    first_name = models.CharField(
        max_length=225,
        verbose_name=_("First names"), 
        blank=True, 
        null=True, 
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=225,
        verbose_name=_("Last name"),
        blank=True, 
        null=True, 
        help_text=_("The last name of the customer.")
    )

    current_address = models.ForeignKey(
        Useraddress,
        on_delete=models.PROTECT,
        verbose_name=_("Current address"),
        blank=True, 
        null=True, 
        related_name='+',
        help_text=_("The current living address of the customer.")
    )

    permanent_address = models.ForeignKey(
        Useraddress,
        on_delete=models.PROTECT,
        verbose_name=_("Permanent address"),
        blank=True, 
        null=True, 
        related_name='+',
        help_text=_("The permanent address of the customer.")
    )

    contact_number = models.CharField(
        max_length=50,
        verbose_name=_("Contact Number"),
        blank=True, 
        null=True, 
        help_text=_("The contact number of the customer.")
    )

    date_of_birth = models.DateTimeField(
        verbose_name=_("Date of Birth"),
        blank=True, 
        null=True, 
        help_text=_("The birth date of  customer.")
    )

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC Complete"),
        default=False,
        help_text=_("Flag to determine if customer has completed KYC verification"),
    )

   
    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC Complete Date"), 
        blank=True, null=True,
        help_text=_("Timestamp when customer completed KYC verification process"),
    )
    #later on add highest qualification in terms of education 

    kyc_status = models.CharField(
        verbose_name=_("KYC Status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True, null=True,
        max_length=15,
        help_text=_("The KYC Status of the customer"),
    )

    on_boarding_complete = models.BooleanField(
        verbose_name=_("Completed Onboarding"),
        default=False,   
        help_text=_("Flag to determine if the customer has completed onboarding process.")
    )

    on_boarding_complete_date = models.DateTimeField(
        verbose_name=("Onboarding  Complete Date"),
        blank=True, null=True,
        help_text=("Timestamp when customer completed onboarding process.")
    )

    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC Submitted"),
        default=False,
        help_text=_("Flag to determine if customer has submitted a KYC verification process.") 
    )
    #is social security number also relevant in the netherlands and if not what is the dutch equivalent? 
    social_security_number = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name=_("Social Security Number"),
        help_text=_("The social security number of the customer. This helps to determine the credit score and also validates tge identity of the custoomer.")
    )

    place_of_birth = models.CharField(
        max_length=150,
        verbose_name=_("Place of Birth"),
        blank=True, null=True,
        help_text=_("The place of birth of the customer. This must match the place of birth as indicated in the customers photo identification.")
    )

    verification_date = models.CharField(
        default=timezone.now,
        verbose_name=_("Verification Date"),
        blank=True, null=True,
        editable=False,
        help_text=_("Timestamp when customers profile was verified.")
    )

    registered_ip_address = models.GenericIPAddressField(
        verbose_name=_("Registered IP Address"),
        blank=True, null=True,
        editable=False,
        help_text=_("The IP address recorder at the time of registration.")
    )

    country_of_residence = models.ForeignKey(
        Country,
        verbose_name=_("Country of Residence"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text=_("The country of residence of the customer. KYC verification will be applied to this country and customer must provide proof of such residence as relevant in the ocuntry of jurisdiction.")
    )
    default_currency = models.CharField(
        max_length=3,
        verbose_name=_("Default Currency"),
        default='EUR',
        blank=True, null=True,
        help_text=_("The default currency of the borrower. Currency will be sent against country of residence.")
    )

    job_title = models.CharField(
        max_length=150,
        verbose_name=_("Job Title"),
        blank=True, null=True,
        help_text=_("The job title of the customer.")
    )

    # fields to implement later on: 

    # pending_cash_balance
    # time_zone
    # salutation
    # higest_qualification
    # passport_year

    # investment_limit
    # fund_committed
    # escrow_account_number
    # tax_id

    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Registered Users")

    def __str__(self):
        return self.email
     #email = EmailField(_("email address"), unique=True)
     #username = None  # type: ignore[assignment]

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name' , 'last_name']

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
         """Get URL for user's detail view.

         Returns:
             str: URL for user detail.

         """
         return reverse("users:detail", kwargs={"pk": self.id})
    
    
