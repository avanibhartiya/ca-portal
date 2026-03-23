

CII = {
    "2001-02": 100, "2002-03": 105, "2003-04": 109, "2004-05": 113,
    "2005-06": 117, "2006-07": 122, "2007-08": 129, "2008-09": 137,
    "2009-10": 148, "2010-11": 167, "2011-12": 184, "2012-13": 200,
    "2013-14": 220, "2014-15": 240, "2015-16": 254, "2016-17": 264,
    "2017-18": 272, "2018-19": 280, "2019-20": 289, "2020-21": 301,
    "2021-22": 317, "2022-23": 331, "2023-24": 348,
    "2024-25": 363, "2025-26": 376
}

def calculate_capital_gain(data):
    
    purchase_cost = float(data.get("purchase_cost", 0))
    purchase_year = data.get("purchase_year")

    sale_value = float(data.get("sale_value", 0))
    stamp_duty_value = float(data.get("stamp_duty_value", 0))
    sale_year = data.get("sale_year")

    improvement_cost = float(data.get("improvement_cost", 0))
    improvement_year = data.get("improvement_year")

    expenses = float(data.get("expenses", 0))

    # Section 50C
    effective_sale_value = max(sale_value, stamp_duty_value)

    # CII values
    cii_purchase = CII.get(purchase_year, 0)
    cii_sale = CII.get(sale_year, 0)

    indexed_purchase = purchase_cost * (cii_sale / cii_purchase) if cii_purchase else 0

    if improvement_cost > 0 and improvement_year:
        cii_improvement = CII.get(improvement_year, 0)
        indexed_improvement = improvement_cost * (cii_sale / cii_improvement) if cii_improvement else 0
    else:
        cii_improvement = 0
        indexed_improvement = 0

    # Old method
    ltcg_old = effective_sale_value - indexed_purchase - indexed_improvement - expenses
    tax_old = ltcg_old * 0.20

    # New method
    ltcg_new = effective_sale_value - purchase_cost - improvement_cost - expenses
    tax_new = ltcg_new * 0.125

    # Best option
    if tax_old < tax_new:
        better_option = "Old Method (20% with Indexation)"
    else:
        better_option = "New Method (12.5% without Indexation)"

    # Return result as JSON
    return {
        "effective_sale_value": round(effective_sale_value, 2),
        "indexed_purchase": round(indexed_purchase, 2),
        "indexed_improvement": round(indexed_improvement, 2),
        "cii_purchase": cii_purchase,
        "cii_sale": cii_sale,
        "cii_improvement": cii_improvement,
        "ltcg_old": round(ltcg_old, 2),
        "tax_old": round(tax_old, 2),
        "ltcg_new": round(ltcg_new, 2),
        "tax_new": round(tax_new, 2),
        "better_option": better_option
    }