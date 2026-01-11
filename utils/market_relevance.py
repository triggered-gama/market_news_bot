# utils/market_relevance.py

INDIAN_MARKET_KEYWORDS = [
    # Indices & exchanges
    "nifty", "sensex", "bank nifty", "midcap", "smallcap",
    "bse", "nse", "mcx", "ncdex",

    # Regulators & policy
    "sebi", "rbi", "finance ministry", "budget",
    "monetary policy", "interest rate", "repo rate",
    "liquidity", "inflation", "cpi", "wpi",

    # Corporate actions
    "results", "earnings", "quarter", "q1", "q2", "q3", "q4",
    "dividend", "bonus", "buyback", "rights issue",
    "split", "demerger", "merger", "amalgamation",

    # Capital markets & deals
    "ipo", "listing", "anchor investor", "gmp",
    "fpo", "qip", "placement",
    "funding", "fund raise", "capital raise",
    "stake sale", "stake buy", "investment",
    "acquisition", "acquires", "deal",

    # Analyst actions
    "buy call", "sell call", "target price", "price target",
    "upgrade", "downgrade", "overweight", "underweight",
    "accumulate", "hold", "outperform", "initiates coverage",
    "reiterates", "maintains", "cuts target", "hikes target",

    # Trading activity
    "block deal", "bulk deal", "large trade",
    "insider buying", "insider selling",

    # IPO & funding
    "sme ipo", "mainboard ipo", "sebi approval",
    "equity raise", "debt raise",

    # Market participants
    "fii", "dii", "foreign investor", "institutional investor",
    "mutual fund", "hedge fund", "private equity",

    # Brokers
    "jefferies", "clsa", "motilal oswal", "kotak", "emkay",
    "hsbc", "morgan stanley", "goldman sachs", "bernstein",

    # Orders & guidance
    "order book", "contract win", "order inflow",
    "capex plan", "guidance raised", "beat estimates",

    # Events & risks
    "signs mou", "divestment", "promoter buying",
    "probe", "investigation", "notice", "ban",
    "penalty", "fine", "fraud", "default",
    "insolvency", "ibc", "nclt",

    # Sectors
    "banking", "nbfc", "psu", "infra", "infrastructure",
    "it stocks", "pharma", "metal stocks", "auto stocks",
    "energy", "power", "oil", "gas", "renewable",
    "real estate", "cement",

    # Macro & commodities
    "rupee", "usd inr", "forex",
    "gold", "silver", "crude", "brent", "commodity",
    "trade deficit", "current account",
]


def is_market_relevant(text: str) -> bool:
    if not text:
        return False

    text = text.lower()
    return any(keyword in text for keyword in INDIAN_MARKET_KEYWORDS)
