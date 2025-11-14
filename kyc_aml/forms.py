# System Libraries
from datetime import datetime
 
# Third Party Modules
from ipware import get_client_ip
from crispy_forms.helper import FormHelper
 
# Django Modules
from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
 
# Django Apps
from kyc_aml.models import KycApplication
from locations.models import Country
 
User = settings.AUTH_USER_MODEL
 
 
class DateInput(forms.DateInput):
    input_type = 'date'
 
 
class KycAmlApplicationForm(forms.ModelForm):
    citizenship = forms.ModelChoiceField(
        queryset=Country.objects.filter(accept_signup=True),
        label=_('Citizenship'),
        required=True,
    )
 
    class Meta:
        model = KycApplication
        exclude = (
            'kyc_status', 'created_date', 'modified_date', 'reviewer', 'kyc_submitted_ip_address',
            'selfie_with_id', 'user', 'reference', 'deleted_date', 'kyc_tries', 'birth_date'
        )
 
    def __init__(self, *args, **kwargs):
        # Retrieve the user object from the keyword arguments
        user = kwargs.pop('user', None)
        super(KycAmlApplicationForm, self).__init__(*args, **kwargs)

        # Set the citizenship field's initial value to the user's citizenship
        if user and user.citizenship:
            self.fields['citizenship'].initial = user.citizenship

        # Other fields and their configurations
        self.fields['legal_first_names'].help_text = _("As shown in your documents")
        self.fields['legal_last_names'].help_text = _("As shown in your documents")
        # self.fields['email'].help_text = _("This is the email used during registration. You can change this later")
        # self.fields['birth_date'].help_text = _("Format (dd-mm-yyyy)")
        self.fields['politically_exposed_person'].help_text = _(
            "A politically exposed person (PEP) is one who has been entrusted with a prominent public function"
        )
        self.fields['country_residence'].help_text = _("Proof of residence will be requested")
        self.fields['citizenship'].help_text = _(
            "Proof of nationality/citizenship will be requested for selected country"
        )
        # Disable some fields
        self.fields['country_residence'].disabled = True
        self.fields['legal_first_names'].disabled = True
        self.fields['legal_last_names'].disabled = True

        # FormHelper settings
        self.helper = FormHelper()
        self.helper.form_show_labels = False
