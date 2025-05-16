import datetime


def check_cost(cost: str):
    if cost is None:
        return cost
    if "." in cost:
        dollars, cents = cost.split(".")
        if dollars:
            dollars = int(dollars)
            if dollars < 0:
                raise ValueError("Invalid Dollar Amount")
            dollars_in_cents = dollars_to_cents(dollars)
        else:
            dollars_in_cents = 0
        if cents:
            cents = int(cents)
            if cents not in range(0, 100):
                raise ValueError("Invalid Cents")
        else:
            cents = 0
    
        cost_in_cents = dollars_in_cents + cents
        return cost_in_cents
    else:
        try:
            cost = int(cost)
        except ValueError:
            raise ValueError("Invalid Cost")
        cost_in_cents = dollars_to_cents(cost)
        if cost_in_cents < 0:
            raise ValueError("Invalid Cost")

        return cost_in_cents

def check_date(date):
    current_date = datetime.date.today()
    try:
        checked_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid Date Format (YYYY-MM-DD)")
    if checked_date > current_date:
        raise ValueError("Invalid Future Date")
    if int(str(checked_date)[:4]) < int(str(current_date)[:4]):
        raise ValueError("Invalid Past Date (Year)")
    return str(checked_date)
    

def check_size(size: str, BUSINESS):
    available_sizing = BUSINESS.item_sizes
    if size.upper() not in available_sizing:
        raise ValueError("Invalid Size")
    if isinstance(size, str):
        item_size = size.upper()
    return item_size


    
# currency conversions
def dollars_to_cents(dollars: int):
    dollars_in_cents = dollars * 100
    return dollars_in_cents


def cents_to_dollars(cents: int):
    cents = int(cents)
    cents_in_dollars = cents / 100
    return cents_in_dollars
