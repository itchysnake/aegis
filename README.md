# GENEX
<p align="center">
    <a href="https://genex.app/" target="_blank">
        <img src="https://genex.app/wp-content/uploads/2021/09/white_gnx_name-1.gif" alt="logo" width="400"/>
    </a>
    <h4 align="center">An asset valuation engine for capital market securities.</h4>
</p>

<div align="center">
    <a href="https://github.com/itchysnake/aegis/blob/master/LICENSE" target="blank">
        <img src="https://img.shields.io/github/license/itchysnake/aegis" alt="aegis licence"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/fork" target="blank">
        <img src="https://img.shields.io/github/forks/itchysnake/aegis" alt="aegis forks"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/issues" target="blank">
        <img src="https://img.shields.io/github/issues/itchysnake/aegis" alt="aegis issues"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/pulls" target="blank">
        <img src="https://img.shields.io/github/issues-pr/itchysnake/aegis" alt="aegis pull-requests"/>
    </a>
    <img src="https://img.shields.io/github/last-commit/itchysnake/aegis" alt="aegis last-commit"/>
</div>

<p align="center">
    <a href="https://github.com/itchysnake/aegis/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/itchysnake/aegis/issues/new/choose">Request Feature</a>
</p>

# What is Aegis?

`Aegis` is an asset valuation and recommendation engine that uses many dimensions to create a price profile for an asset, or assets in bulk. Dimensions are broken down into components:
* Charts
    * Boundaries
    * Indicators
    * Shapes
    * Trend
* Debt (incomplete)
    * Utilities
* Equity
    * Accounting
    * Growth
    * Risk
    * Statistics
    * Valuation
* Macroeconomic
    * GDP
    * Labour
    * Price
    * Trade
* Rates (incomplete)
* Sentiment (incomplete)

These dimensions and their relevant components allow `Aegis` to create a hollistic picture not only of an asset according to their book value, but also in accordance with the market, competing products, the macro outlook, and more.

# Getting Started
`Aegis` uses common data science libraries such as `pandas` for most of its needs.

### Installation
1. To get started with `aegis`:
```bash
pip install git+ttps://github.com/itchysnake/aegis
```

If this is giving you errors you can alternatively try:

```bash
python -m pip install git+ttps://github.com/itchysnake/aegis
```

2. Check your installation directory

### Usage
Once installed you can get started by calling the package:

```
import aegis

# Using 'charts' dimension
amzn_ath = aegis.charts.bounds.Bounds.ath("AMZN","6mo")
nflx_rsi = aegis.charts.indicators.Indicators.rsi(
    ticker = "NFLX", 
    period =" 6mo",
    window = 14
)

# Using 'equity' dimension
aapl_roe = aegis.equity.growth.Growth.roe("AAPL")
msft_risk = aegis.equity.risk.Risk.sharpe("MSFT")

# Using 'macro' dimension
spain_labour = aegis.macro.labour.Labour.unemployment("Spain")
jpn_gdp = aegis.macro.gdp.GDP.gdp("Japan", type = "real")

```

Feel free to experiment and combine indicators to create valuable insights into the markets.

### Data Procurement
Data procurement is not included in Aegis naturally. I am currently building a package to integrate Aegis with the existing (Alpaca Markets API)[https://github.com/alpacahq/alpaca-trade-api-python].

Use whatever is comfortable for you.

### License
Aegis is released under (XYZ License)[https://github.com/itchysnake/aegis/blob/master/LICENSE]