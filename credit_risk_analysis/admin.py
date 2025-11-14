from django.contrib import admin
from projects.models import CreditRiskAssessment
from django.utils.html import format_html
import matplotlib.pyplot as plt
import io
import base64

@admin.register(CreditRiskAssessment)
class CreditRiskAssessmentAdmin(admin.ModelAdmin):

   
    def view_macroeconomic_chart(self, obj):
        # Generate a chart of macroeconomic factors
        return format_html('<img src="data:image/png;base64,{}" />', self.generate_macroeconomic_chart(obj))

    def generate_macroeconomic_chart(self, obj):
        # Create a bar chart of macroeconomic factors
        fig, ax = plt.subplots()
        factors = {
            'Interest Rate': obj.interest_rate,
            'Inflation Rate': obj.inflation_rate,
            'GDP Growth Rate': obj.gdp_growth_rate,
            'Unemployment Rate': obj.unemployment_rate,
            'Bond Yield': obj.bond_yield
        }
        ax.bar(factors.keys(), factors.values())
        ax.set_title(f'Macroeconomic Factors for {obj.project.title}')
        ax.set_ylabel('Value')
        
        # Convert the plot to a PNG image and encode it as base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close(fig)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64

    view_macroeconomic_chart.short_description = 'Macroeconomic Factors Chart'
