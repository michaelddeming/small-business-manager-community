
class IncomeStatement:

    def __init__(
            self, 
            year: str, 
            gross_sales: int, 
            sales_transport: int,
            allowances: int,
            fees: int,
            discounts: int,
            cost_of_goods_sold: int,
            expenses: int,
            ):

        self.year = year
        self.gross_sales = gross_sales
        self.sales_transport = sales_transport
        self.allowances = allowances
        self.fees = fees
        self.discounts = discounts
        self.cost_of_goods_sold = cost_of_goods_sold
        self.expenses = expenses

        self.net_sales = (self.gross_sales + self.sales_transport) - (self.allowances + self.fees + self.discounts)

        self.gross_margin = self.net_sales - self.cost_of_goods_sold

        self.net_income = self.gross_margin - self.expenses




