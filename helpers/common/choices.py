
from django.utils.translation import gettext_lazy as _ 



class ModelChoices:
    
    BANK_STATEMENT = "BANK_STATEMENT"
    CREDIT_CARD_STATEMENT = "CREDIT_CARD_STATEMENT"
    UTILITY = "UTILITY"

    PROOF_OF_ADDRESS_TYPE = (
        (BANK_STATEMENT, _("Bank Statement")),
        (CREDIT_CARD_STATEMENT, _("Credit Card Statement")),
        (UTILITY, _(" Utility Bill"))
    )

    NATIONAL_ID = "NATIONAL_ID"
    PASSPORT = "PASSPORT"

    PHOTO_INDENTIFICATION_TYPE = (
        (NATIONAL_ID, _("National ID")),
        (PASSPORT, _("Passport"))
    )

    KYC_STATUS = (
        ("verified", _("Verified")),
        ("unverified", _("Unverified")),
        ("pending", _("Pending")),
        ("rejected", _("Rejected")),
        ("cancelled", _("Cancelled"))
    )

    PEP_CHOICES = (
        ("pep", _("Yes, I am politically exposed")),
        ("non_pep", _("No, I'm not politically exposed"))
    )

    KYC_REFUSE_REASON_CODE = (
        ("EXPIRED_DOCUMENT", _("Document Expired")),
        ("DOCUMENT_DOES_NOT_MATCH_USER_DATA", _("Document does not match user data"))

    )
