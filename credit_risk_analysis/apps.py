from django.apps import AppConfig


class CreditRiskAnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credit_risk_analysis'

    def ready(self):
        import credit_risk_analysis.signals
