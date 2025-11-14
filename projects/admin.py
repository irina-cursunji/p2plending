from django.contrib import admin
from .models import Project, Investment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Raw ID fields for foreign key relationships
    raw_id_fields = ['borrower']
    
    # Display fields in the list view
    list_display = (
        'title', 
        'borrower', 
        'goal_amount', 
        'funding_start_date', 
        'funding_end_date', 
        'project_status',
        'is_approved'  # Display approval status
    )
    
    # Searchable fields
    search_fields = ['title', 'description', 'location']
    
    # Filters in the sidebar
    list_filter = [
        'project_status', 
        'risk_level', 
        'created_at', 
        'is_approved'  # Filter by approval status
    ]
    
    # Default ordering of list view
    ordering = ['created_at']
    
    # Add a custom field to the form view
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Make `is_approved` field readonly in admin form
        if obj and obj.is_approved:
            form.base_fields['is_approved'].disabled = True
        return form

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    # Raw ID fields for foreign key relationships
    raw_id_fields = ['investor', 'project']
    
    # Display fields in the list view
    list_display = ('investor', 'project', 'amount', 'date_invested')
    
    # Searchable fields
    search_fields = ['project__title', 'investor__username']
    
    # Filters in the sidebar
    list_filter = ['date_invested']
    
    # Default ordering of list view
    ordering = ['date_invested']
