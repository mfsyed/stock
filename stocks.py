import requests
import math
import pprint

#global tools
tech_industries = {"Internet Retail","Consumer Electronics","SoftwareInfrastructure","Internet Content & Information","SoftwareApplication","Information Technology Services"}
api_key = "&apikey=TTQMPP44X9LLAY7Z"
overview_url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="
income_statement_url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol="
cash_flow_url = "https://www.alphavantage.co/query?function=CASH_FLOW&symbol="

def EvaluateTechStock(overview_info,income_statement_info,cash_flow_info):
    #current ratio
    #cash ratio
    #debt to equity ratio
    #SG&A Expenses To Revenue
    #R&D Expense Growth
    # free cash flow
    # Free Cash Flow Growth\
    total = 5
    count = 0
    assessment = dict()

    market_cap = int(overview_info["MarketCapitalization"])
    if market_cap > 10000000000:
         assessment["Market Cap"] = "Good"
    else:
         assessment["Market Cap"] = ":("

    # beta= float(overview_info["Beta"])
    # if beta > 1.0:
    #     assessment["beta"] = "Higher Risk"
    # else:
    #     assessment["beta"] = "Low Risk"


    price_to_sales = float(overview_info["PriceToSalesRatioTTM"])
    if price_to_sales <= 2.0 and price_to_sales >= 1.0:
        assessment["Price-To-Sales"] = "Ideal"
    else:
        assessment["Price-To-Sales"] = "Less Ideal"

    quarter_revenue_growth = float(overview_info["QuarterlyRevenueGrowthYOY"])
    assessment["Quarterly Revenue Growth (YOY)"] = quarter_revenue_growth

    gross_profit_margin = int(overview_info["GrossProfitTTM"])
    assessment["Gross Profit Margin (TTM)"] = gross_profit_margin


    return assessment


def get_stats(symbol):

    #doing get requests
    overview_link = overview_url+symbol+api_key
    overview_site = requests.get(overview_link)
    overview_info = overview_site.json()

    income_statement_link = income_statement_url+symbol+api_key
    income_statement_site = requests.get(income_statement_link)
    income_statement_info = income_statement_site.json()

    cash_flow_link = cash_flow_url+symbol+api_key
    cash_flow_site = requests.get(cash_flow_link)
    cash_flow_info = cash_flow_site.json()


    #initiating evaluation based on industry
    industry = overview_info["Industry"]
    if industry in tech_industries:
        return EvaluateTechStock(overview_info,income_statement_info,cash_flow_info)



    #peratios
    tpe = info["TrailingPE"]
    fpe = info["ForwardPE"]
    pe = info["PERatio"]
    #earningspershare
    eps = info["EPS"]
    #price to book
    ptb = info["PriceToBookRatio"]
    #pegratio
    peg = info["PEGRatio"]
    #volitatility



print(get_stats("AAPL"))



#look up for how to calculate profitability using thesefigures
#make a class, functions, something that will create story
