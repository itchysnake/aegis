from macro.gdp import GDP

def gdp(country):
    nominal = GDP.gdp(country)
    real = GDP.gdp(country, "real")
    
    return [nominal,real]

def is_inflation_high():
    pass

def inflation_cause():
    pass
