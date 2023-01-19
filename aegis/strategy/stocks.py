"""
How do we know which shares are going to do well?

Macroeconomic determinants:
    Growth:
        High beta firms

    Recession:
        Low beta will outperform
        
    Growing incomes:
        Luxury consumer discretionary, and holiday firms

    Lower consumer sentiment:
        They're saving! Banks have larger deposits
        Luxury consumer discretionary down

    Rising rates:
        Banks do better
        "Growth stocks" do worse since PV's drawn out into distance

    Falling rates:
        Debt does better

    Inflation is high:
        Equity which can pass that cost onto consumers
        C o m m o d i t i e s
        If it's cost-push then commodities because they are typically
            what causes the rising CPI

    Low unemployment:
        Economy heating up, inflation should be coming up soon     
"""
import equity

def run():
    ticker = input("Ticker: ")
    investment_horizon = input("Investment horizon: ")

    print("-- Risk -- ")
    cost_of_equity = equity.risk.Risk.cost_of_equity(ticker)
    wacc = equity.risk.Risk.wacc(ticker)
    print("Cost of equity: ",cost_of_equity)
    print("WACC: ",wacc)

    print("-- Growth --")
    expected_growth = equity.growth.Growth.growth(ticker)
    div_yield = equity.valuation.Valuation.div_yield(ticker)
    roe = equity.growth.Growth.roe(ticker)
    print("Expected growth: ",expected_growth)
    print("Dividend yield: ",div_yield)
    print("ROE: ",roe)

    print("-- Price --")
    price = equity.stats.Stats.price(ticker)
    pvgo = equity.valuation.Valuation.pvgo(ticker)
    print("Price: ",price)
    print("PVGO: ",pvgo)

    print("-- Valuation --")
    book_val = equity.valuation.Valuation.book_val(ticker)
    future_price = equity.valuation.Valuation.future_price(ticker, investment_horizon)
    gordons = equity.valuation.Valuation.gordons_model(ticker)
    ddm = equity.valuation.Valuation.ddm(ticker, investment_horizon)
    pe = equity.valuation.Valuation.pe(ticker)
    print("Book value: ",book_val)
    print("Future price ({} yr): {}".format(investment_horizon, future_price))
    print("Gordons model: ",gordons)
    print("Dividend Discount Model ({} yr): {}".format(investment_horizon,ddm))
    print("PE: ",pe)