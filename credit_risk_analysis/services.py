
import requests
from .economic_data import EconomicDataFetcher
from decimal import Decimal, InvalidOperation

def calculate_credit_risk(project):
    from projects.models import Project
    if not isinstance(project, Project):
        raise TypeError("The 'project' argument must be an instance of Project.")
    
    try:
        # Example calculations
        financial_health_score = calculate_financial_health(project)
        credit_history_score = calculate_credit_history(project)
        business_viability_score = calculate_business_viability(project)
        macroeconomic_factors_score = calculate_macroeconomic_factors()

        overall_score = (financial_health_score * 0.4 +
                         credit_history_score * 0.3 +
                         business_viability_score * 0.2 +
                         macroeconomic_factors_score * 0.1)
        
        if overall_score < 50:
            risk_level = 'High Risk'
            suggested_interest_rate = 12.0
        elif 50 <= overall_score < 75:
            risk_level = 'Medium Risk'
            suggested_interest_rate = 8.5
        else:
            risk_level = 'Low Risk'
            suggested_interest_rate = 5.0
        
        # Fetch economic data
        economic_data = fetch_economic_data()
        
        # Update or create CreditRiskAssessment
        CreditRiskAssessment.objects.update_or_create(
            project=project,
            defaults={
                'financial_health_score': Decimal(financial_health_score),
                'credit_history_score': Decimal(credit_history_score),
                'business_viability_score': Decimal(business_viability_score),
                'macroeconomic_factors_score': Decimal(macroeconomic_factors_score),
                'overall_score': Decimal(overall_score),
                'risk_level': risk_level,
                'suggested_interest_rate': Decimal(suggested_interest_rate),
                'interest_rate': Decimal(economic_data['interest_rate']),
                'inflation_rate': Decimal(economic_data['inflation_rate']),
                'gdp_growth_rate': Decimal(economic_data['gdp_growth_rate']),
                'unemployment_rate': Decimal(economic_data['unemployment_rate']),
                'bond_yield': Decimal(economic_data['bond_yield']),
            }
        )
        
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_economic_data():
    fetcher = EconomicDataFetcher()
    return fetcher.get_latest_economic_data()

# Add your calculation functions here
def calculate_financial_health(project):
    data = {
        'current_assets': project.current_assets or 0,
        'current_liabilities': project.current_liabilities or 0,
        'total_liabilities': project.total_liabilities or 0,
        'shareholders_equity': project.shareholders_equity or 0,
        'revenue': project.revenue or 0,
        'cost_of_goods_sold': project.cost_of_goods_sold or 0,
        'net_income': project.net_income or 0
    }
    
    try:
        current_ratio = data['current_assets'] / data['current_liabilities'] if data['current_liabilities'] != 0 else 0
        debt_to_equity_ratio = data['total_liabilities'] / data['shareholders_equity'] if data['shareholders_equity'] != 0 else 0
        gross_profit_margin = (data['revenue'] - data['cost_of_goods_sold']) / data['revenue'] if data['revenue'] != 0 else 0
        net_profit_margin = data['net_income'] / data['revenue'] if data['revenue'] != 0 else 0
        
        current_ratio_score = min(current_ratio / 2.0 * 100, 100)
        debt_to_equity_score = max(100 - (debt_to_equity_ratio * 50), 0)
        gross_profit_margin_score = gross_profit_margin * 100
        net_profit_margin_score = net_profit_margin * 100
        
        score = (current_ratio_score * 0.25 +
                 debt_to_equity_score * 0.25 +
                 gross_profit_margin_score * 0.25 +
                 net_profit_margin_score * 0.25)
        
        return round(score, 2)
    
    except (ZeroDivisionError, InvalidOperation) as e:
        print(f"An error occurred in financial health calculation: {e}")
        return 0

def calculate_credit_history(project):
    try:
        credit_score = fetch_credit_score_from_bureau(project)
        return min(max((credit_score - 300) / (850 - 300) * 100, 0), 100)
    
    except Exception as e:
        print(f"An error occurred in credit history calculation: {e}")
        return 0

def fetch_credit_score_from_bureau(project):
    try:
        credit_bureau_api_url = "https://api.creditbureau.com/credit_score"
        response = requests.get(credit_bureau_api_url, params={"project_id": project.id})
        response.raise_for_status()
        data = response.json()
        return data.get('credit_score', 0)
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching credit score: {e}")
        return 0

def calculate_business_viability(project):
    try:
        business_plan_quality_score = assess_business_plan_quality(project.business_plan)
        market_conditions_score = assess_market_conditions(project.business_plan)
        
        score = (business_plan_quality_score * 0.5 +
                 market_conditions_score * 0.5)
        
        return round(score, 2)
    
    except Exception as e:
        print(f"An error occurred in business viability calculation: {e}")
        return 0

def assess_business_plan_quality(business_plan):
    return 75  # Placeholder

def assess_market_conditions(business_plan):
    return 75  # Placeholder

def calculate_macroeconomic_factors():
    try:
        fetcher = EconomicDataFetcher()
        economic_data = fetcher.get_latest_economic_data()

        interest_rate = economic_data.get('interest_rate', 0)
        inflation_rate = economic_data.get('inflation_rate', 0)
        gdp_growth_rate = economic_data.get('gdp_growth_rate', 0)
        unemployment_rate = economic_data.get('unemployment_rate', 0)
        bond_yield = economic_data.get('bond_yield', 0)

        macroeconomic_factors_score = (
            (100 - interest_rate * 10) +
            (100 - inflation_rate * 5) +
            (gdp_growth_rate * 10) +
            (100 - unemployment_rate * 5) +
            (100 - bond_yield * 10)
        ) / 5

        return min(max(macroeconomic_factors_score, 0), 100)
    
    except Exception as e:
        print(f"An error occurred in macroeconomic factors calculation: {e}")
        return 0
