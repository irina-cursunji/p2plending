import requests
from datetime import datetime

class EconomicDataFetcher:
    ECB_BASE_URL = "https://sdw-wsrest.ecb.europa.eu/service/data"
    TRADING_ECONOMICS_BASE_URL = "https://api.tradingeconomics.com"
    EUROSTAT_BASE_URL = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"

    def fetch_interest_rate(self):
        # Fetch ECB base interest rate (e.g., refinancing rate)
        response = requests.get(f"{self.ECB_BASE_URL}/EXR/D.NL.EUR.SP00.A")
        data = response.json()
        # Extract the most recent value
        rate = data['dataSets'][0]['observations'][list(data['dataSets'][0]['observations'].keys())[0]][0]
        return rate

    def fetch_inflation_rate(self):
        # Fetch inflation rate (HICP)
        response = requests.get(f"{self.ECB_BASE_URL}/ICP/M.U2.N.000000.4.ANR")
        data = response.json()
        inflation_rate = data['dataSets'][0]['observations'][list(data['dataSets'][0]['observations'].keys())[0]][0]
        return inflation_rate

    def fetch_gdp_growth_rate(self):
        # Fetch GDP growth rate (Quarterly)
        response = requests.get(f"{self.TRADING_ECONOMICS_BASE_URL}/gdp?country=Netherlands&c=e869b28205264f0:l7yo64h9or8uy0s")
        data = response.json()
        gdp_growth_rate = data[0]['qoq']
        return gdp_growth_rate

    def fetch_unemployment_rate(self):
        # Fetch unemployment rate
        response = requests.get(f"{self.EUROSTAT_BASE_URL}/une_rt_m?geo=NL")
        data = response.json()
        unemployment_rate = data['value']
        return unemployment_rate

    def fetch_government_bond_yield(self):
        # Fetch 10-year government bond yield
        response = requests.get(f"{self.TRADING_ECONOMICS_BASE_URL}/bond?country=Netherlands&c=e869b28205264f0:l7yo64h9or8uy0s")
        data = response.json()
        bond_yield = data[0]['y10']
        return bond_yield

    def get_latest_economic_data(self):
        return {
            'interest_rate': self.fetch_interest_rate(),
            'inflation_rate': self.fetch_inflation_rate(),
            'gdp_growth_rate': self.fetch_gdp_growth_rate(),
            'unemployment_rate': self.fetch_unemployment_rate(),
            'bond_yield': self.fetch_government_bond_yield(),
            'date': datetime.now()
        }
