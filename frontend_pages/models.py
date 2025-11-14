from django.db import models
from django.utils.translation import gettext_lazy as _
from helpers.common.basemodel import BaseModel

class TeamMember(BaseModel):

    """
    Entity represents a team member
    """
    name = models.CharField(
        verbose_name=_("name"),
        max_length=20, 
        help_text='Enter field documentation'
        )
    
    designation = models.CharField(
        verbose_name=_("Designation"),
        max_length=50, 
        help_text=_("The position of the team member.")
        )
    
    linkedin = models.URLField(
        verbose_name=_("LinkedIn"),
        max_length=50,
        blank=True, null=True, 
        help_text=_("LinkedIn URL")
        )
    
    email = models.CharField(
        verbose_name=_("Email"),
        max_length=75,
        blank=True, null=True,
        help_text=_("team member's email") 
    )

    photo = models.ImageField(
            verbose_name=_("Photo"),
            upload_to='team',
            help_text=_("photo of the team member.") 
        )
    

    #Metadata
    class Meta :
        verbose_name =_(" Team member")
        verbose_name_plural =_("Team members")
        

    #Methods
    

    def __str__(self):
        return self.name
