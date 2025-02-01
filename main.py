import yfinance as yf
import pandas as pd
from webencodings.mklabels import generate

def generate_csv(balance_sheet, cash_flow, financials, file_name):
    # 提取财务数据
    revenue = financials.loc['Total Revenue']
    gross_profit = financials.loc['Gross Profit']
    operating_profit = financials.loc['Operating Income']
    pretax_profit = financials.loc['Pretax Income']
    net_profit = financials.loc['Net Income']
    asset = balance_sheet.loc['Total Assets']

    free_cash_flow = cash_flow.loc['Free Cash Flow']
    operating_cash_flow = cash_flow.loc['Operating Cash Flow']
    investing_cash_flow = cash_flow.loc['Investing Cash Flow']
    capital_expenditure = cash_flow.loc['Capital Expenditure']

    # 计算各项财务比率（百分比格式）
    gross_profit_margin = (gross_profit / revenue) * 100
    operating_profit_margin = (operating_profit / revenue) * 100
    pretax_profit_margin = (pretax_profit / revenue) * 100
    net_profit_margin = (net_profit / revenue) * 100

    # 为百分比列添加 '%' 符号
    gross_profit_margin = gross_profit_margin.apply(lambda x: f"{round(x, 2)}%")
    operating_profit_margin = operating_profit_margin.apply(lambda x: f"{round(x, 2)}%")
    pretax_profit_margin = pretax_profit_margin.apply(lambda x: f"{round(x, 2)}%")
    net_profit_margin = net_profit_margin.apply(lambda x: f"{round(x, 2)}%")

    # 构建DataFrame
    df = pd.DataFrame({
        'Revenue (亿美元)': revenue / 100000000,
        'Gross Profit (亿美元)': gross_profit / 100000000,
        'Gross Profit Margin': gross_profit_margin,
        'Operating Profit (亿美元)': operating_profit / 100000000,
        'Operating Profit Margin': operating_profit_margin,
        'Pretax Profit (亿美元)': pretax_profit / 100000000,
        'Pretax Profit Margin': pretax_profit_margin,
        'Net Profit (亿美元)': net_profit / 100000000,
        'Net Profit Margin': net_profit_margin,
        'Asset (亿美元)': asset / 100000000,
        'Asset Turnover': revenue / asset,
        'Free Cash Flow (亿美元)': free_cash_flow / 100000000,
        'Invest Cash Flow (亿美元)': investing_cash_flow / 100000000,
        'Operating Cash Flow (亿美元)': operating_cash_flow / 100000000,
        'Capital Expenditure (亿美元)': capital_expenditure / 100000000
    })

    # 转置数据使年份为横轴
    df = df.T

    # 保存到CSV文件
    df.to_csv(f'{file_name}.csv', encoding='utf-8')

    print("数据已保存")


if __name__ == '__main__':
    symbol = "ASML"

    # 获取微软（MSFT）的财务数据
    stock = yf.Ticker(symbol)

    # print(cash_flow)
    generate_csv(stock.balance_sheet, stock.cashflow, stock.financials, f"{symbol}_annual_year.csv")
    generate_csv(stock.quarterly_balance_sheet, stock.quarterly_cashflow, stock.quarterly_financials, f"{symbol}_quarter_year.csv")