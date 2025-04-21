import sqlite3
from classes.item_class import Item
import os
from dotenv import load_dotenv

class DatabaseManager:

    def __init__(self):
        self.conn = None
        self.db = None

    def connect(self):
        if self.conn is None:
            try:
                load_dotenv()
                db_path = os.getenv("FILEPATH")
                if not db_path:
                    raise ValueError("FILEPATH not set in .env file")
                self.conn = sqlite3.connect(db_path)
                self.db = self.conn.cursor()
            except sqlite3.DatabaseError as e:
                print(f"Database connection failed: {e}")
        else:
            raise sqlite3.DatabaseError("Error: Database already connected.")

    def close(self):
        if self.conn and self.db:
            try:
                self.db.close()
                self.conn.close()
            except sqlite3.ProgrammingError as e:
                print(f"Error closing the database: {e}")
            except sqlite3.DatabaseError as e:
                print(f"Error with the database: {e}")
            except Exception as e:
                print(f"Error - Unexpected: {e}")
        else:
            raise sqlite3.ProgrammingError(
                "Error: Database not connected, closure failed."
            )

    # INVENTORY FUNCTIONS

    def fetch_inventory(self, amount):

        amounts = "all"

        if self.db and self.conn:
            if amount in amounts:
                match amount:
                    case "all":
                        return self.db.execute("SELECT * FROM inventory").fetchall()
            else:
                if isinstance(amount, int):
                    return self.db.execute(
                        "SELECT * FROM inventory LIMIT ?", (amount,)
                    ).fetchall()
                else:
                    raise ValueError(
                        f"Error: amount={amount} not in {amounts} or of type=int."
                    )
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_inventory_headings(self):
        if self.conn and self.db:
            try:
                return [
                    headings[0]
                    for headings in self.db.execute(
                        "SELECT * FROM inventory"
                    ).description
                ]
            except Exception as e:
                raise Exception(f"Error - Unexpected: {e}")

        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_inventory_item_search(self, column, value):
        return self.db.execute(
            f"SELECT * FROM inventory WHERE {column} = ?", (value,)
        ).fetchall()

    def add_item_to_inventory(
        self,
        date_purchased: str,
        item_desc: str,
        item_size: str,
        item_cost: int,
        status: str,
    ):
        if self.db and self.conn:
            self.db.execute(
                "INSERT INTO inventory (date_purchased, description, size, cost, status) VALUES (?, ?, ?, ?, ?)",
                (date_purchased, item_desc, item_size, item_cost, status),
            )
            self.conn.commit()
            return True
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def check_duplicate_item(self, date_purchased, item_desc, item_size, item_cost):
        duplicate_item = self.db.execute(
            "SELECT * FROM inventory WHERE date_purchased = ? and description = ? and size = ? and cost = ?",
            (date_purchased, item_desc, item_size, item_cost),
        ).fetchall()

        if duplicate_item:
            return duplicate_item
        else:
            return False

    def check_item_status(self, item_id):

        item_status = self.db.execute(
            "SELECT status FROM inventory WHERE id = ?", (item_id,)
        ).fetchall()
        if item_status:
            return item_status
        else:
            raise ValueError(f"item_id={item_id} has no status!")

    # EXPENSES FUNCTIONS

    def fetch_expenses_expense_search(self, column, value):
        return self.db.execute(
            f"SELECT * FROM expenses WHERE {column} = ?", (value,)
        ).fetchall()

    def fetch_expenses(self, amount):

        amounts = "all"

        if self.db and self.conn:
            if amount in amounts:
                match amount:
                    case "all":
                        return self.db.execute("SELECT * FROM expenses").fetchall()
            else:
                if isinstance(amount, int):
                    return self.db.execute(
                        "SELECT * FROM expenses LIMIT ?", (amount,)
                    ).fetchall()
                else:
                    raise ValueError(
                        f"Error: amount={amount} not in {amounts} or of type=int."
                    )
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_expenses_headings(self):
        if self.conn and self.db:
            try:
                return [
                    headings[0]
                    for headings in self.db.execute(
                        "SELECT * FROM expenses"
                    ).description
                ]
            except Exception as e:
                raise Exception(f"Error - Unexpected: {e}")

        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def check_duplicate_expense(
        self, date: str, description: str, cost: int, category: str, method: str
    ):
        duplicate_expense = self.db.execute(
            "SELECT * FROM expenses WHERE date = ? and description = ? and cost = ? and category = ? and method = ?",
            (date, description, cost, category, method),
        ).fetchall()

        if duplicate_expense:
            return duplicate_expense
        else:
            return False

    def add_expense_to_expenses(
        self,
        date: str,
        description: str,
        cost: int,
        category: str,
        method: str,
        note: str,
    ):
        if self.db and self.conn:
            self.db.execute(
                "INSERT INTO expenses (date, description, cost, category, method, note) VALUES (?, ?, ?, ?, ?, ?)",
                (date, description, cost, category, method, note),
            )
            self.conn.commit()
            return True
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    # TRANSACTION FUNCTIONS

    def add_transaction_to_transactons(
        self,
        type,
        date,
        item_id,
        item_amount,
        sale_platform,
        transportation_method,
        transportation_charge,
        fee,
        discount,
        note,
    ):

        if self.db and self.conn:
            self.db.execute(
                "INSERT INTO transactions (type, date, item_id, item_amount, sale_platform, transportation, transportation_charge, fee, discount, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (   
                    type, 
                    date,
                    item_id,
                    item_amount,
                    sale_platform,
                    transportation_method,
                    transportation_charge,
                    fee,
                    discount,
                    note,
                ),
            )
            self.conn.commit()
            return True
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_transactions(self, amount):

        amounts = "all"

        if self.db and self.conn:
            if amount in amounts:
                match amount:
                    case "all":
                        return self.db.execute("SELECT * FROM transactions").fetchall()
            else:
                if isinstance(amount, int):
                    return self.db.execute(
                        "SELECT * FROM transactions LIMIT ?", (amount,)
                    ).fetchall()
                else:
                    raise ValueError(
                        f"Error: amount={amount} not in {amounts} or of type=int."
                    )
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_transactions_headings(self):

        if self.conn and self.db:
            try:
                return [
                    headings[0]
                    for headings in self.db.execute(
                        "SELECT * FROM transactions"
                    ).description
                ]
            except Exception as e:
                raise Exception(f"Error - Unexpected: {e}")

        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def check_item_id(self, item_id):

        found_item = self.db.execute(
            "SELECT * FROM inventory WHERE id = ?", (item_id,)
        ).fetchone()

        if not found_item:
            raise ValueError(f"Invalid item_id={item_id}")
        return item_id

    def check_duplicate_transaction(self, item_id: str):

        duplicate_transaction = self.db.execute(
            "SELECT * FROM transactions WHERE  item_id = ?", (item_id,)
        ).fetchall()

        if duplicate_transaction:
            return duplicate_transaction
        return None

    def convert_item_status_sold(self, item_id: str):

        if self.db and self.conn:
            self.db.execute(
                "UPDATE inventory SET status = 'sold' WHERE id = ?", (item_id,)
            )
            self.conn.commit()
            return True
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")
        
    def convert_item_status_inventory(self, item_id: str):

        if self.db and self.conn:
            self.db.execute(
                "UPDATE inventory SET status = 'inventory' WHERE id = ?", (item_id,)
            )
            self.conn.commit()
            return True
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_transactions_transaction_search(self, column, value):
        return self.db.execute(
            f"SELECT * FROM transactions WHERE {column} = ?", (value,)
        ).fetchall()

    # INCOME STATEMENT FUNCTIONS

    def fetch_income_statement_headings(self):
        if self.conn and self.db:
            try:
                return [
                    headings[0]
                    for headings in self.db.execute(
                        "SELECT * FROM income_statement"
                    ).description
                ]
            except Exception as e:
                raise Exception(f"Error - Unexpected: {e}")

        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def fetch_income_statements(self, amount):
        amounts = "all"

        if self.db and self.conn:
            if amount in amounts:
                match amount:
                    case "all":
                        return self.db.execute(
                            "SELECT * FROM income_statement"
                        ).fetchall()
            else:
                if isinstance(amount, int):
                    return self.db.execute(
                        "SELECT * FROM income_statement LIMIT ?", (amount,)
                    ).fetchall()
                else:
                    raise ValueError(
                        f"Error: amount={amount} not in {amounts} or of type=int."
                    )
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def create_income_statement(self, years: list):

        years = list(set(years))

        current_income_statement_years = self.db.execute(
            "SELECT year FROM income_statement"
        ).fetchall()
        years_ = [int(row[0]) for row in current_income_statement_years]
        

        for year in years:
            gross_sales = self.fetch_gross_sales(year)
            sales_transport = self.fetch_sales_transport(year)
            allowances = self.fetch_allowances(year)
            fees = self.fetch_fees(year)
            discounts = self.fetch_discounts(year)

            # net_sales auto GEN via SQLITE

            cost_of_goods_sold = self.fetch_cost_of_goods_sold(year)

            # gross_margin auto GEN via SQLITE

            expenses = self.fetch_income_statement_expenses(year)

            # net_income auto GEN via SQLITE

            if year in years_:
                self.db.execute(
                    "UPDATE income_statement SET gross_sales = ?, sales_transport = ?, allowances = ?, fees = ?, discounts = ?, cost_of_goods_sold = ?, expenses = ? WHERE year = ?",
                    (
                        gross_sales,
                        sales_transport,
                        allowances,
                        fees,
                        discounts,
                        cost_of_goods_sold,
                        expenses,
                        year,
                    ),
                )

            else:
                self.db.execute(
                    "INSERT INTO income_statement (year, gross_sales, sales_transport, allowances, fees, discounts, cost_of_goods_sold, expenses) VALUES (?,?,?,?,?,?,?,?)",
                    (
                        year,
                        gross_sales,
                        sales_transport,
                        allowances,
                        fees,
                        discounts,
                        cost_of_goods_sold,
                        expenses,
                    ),
                )
        self.conn.commit()

    def fetch_gross_sales(self, year):
        gross_sales_in_year = self.db.execute(
            "SELECT SUM(item_amount) FROM transactions WHERE date LIKE ? AND type = ?", (f"{year}%", "sale")
        ).fetchone()[0]
        return gross_sales_in_year if gross_sales_in_year else 0

    def fetch_sales_transport(self, year):
        sales_transport_in_year = self.db.execute(
            "SELECT SUM(transportation_charge) FROM transactions WHERE date LIKE ?",
            (f"{year}%",),
        ).fetchone()[0]
        return sales_transport_in_year if sales_transport_in_year else 0

    def fetch_allowances(self, year):
        gross_allowances_in_year = self.db.execute(
            "SELECT SUM(item_amount) FROM transactions WHERE date LIKE ? AND type = ?", (f"{year}%", "return")
        ).fetchone()[0]
        return gross_allowances_in_year if gross_allowances_in_year else 0

    def fetch_fees(self, year):
        fees_in_year = self.db.execute(
            "SELECT SUM(fee) FROM transactions WHERE date LIKE ?", (f"{year}%",)
        ).fetchone()[0]
        return fees_in_year if fees_in_year else 0

    def fetch_discounts(self, year):
        discounts_in_year = self.db.execute(
            "SELECT SUM(discount) FROM transactions WHERE date LIKE ?", (f"{year}%",)
        ).fetchone()[0]
        return discounts_in_year if discounts_in_year else 0

    def fetch_cost_of_goods_sold(self, year):
        # Get cost of goods sold from sale transactions
        sale_rows = self.db.execute(
            """
            SELECT inventory.cost
            FROM transactions
            JOIN inventory ON transactions.item_id = inventory.id
            WHERE transactions.date LIKE ? AND transactions.type = 'sale'
            """, (f"{year}%",)
        ).fetchall()

        cost_of_goods_sold = sum(row[0] for row in sale_rows if row[0] is not None)

        # Get cost of goods returned from return transactions
        return_rows = self.db.execute(
            """
            SELECT inventory.cost
            FROM transactions
            JOIN inventory ON transactions.item_id = inventory.id
            WHERE transactions.date LIKE ? AND transactions.type = 'return'
            """, (f"{year}%",)
        ).fetchall()

        cost_of_goods_returned = sum(row[0] for row in return_rows if row[0] is not None)

        return cost_of_goods_sold - cost_of_goods_returned 

    def fetch_income_statement_expenses(self, year):

        expenses_in_year = self.db.execute(
            "SELECT SUM(cost) FROM expenses WHERE date LIKE ?", (f"{year}%",)
        ).fetchone()[0]
        return expenses_in_year if expenses_in_year else 0

    # BALANCE SHEET FUNCTIONS

    def fetch_balance_sheet_headings(self):
        if self.conn and self.db:
            try:
                return [
                    headings[0]
                    for headings in self.db.execute(
                        "SELECT * FROM balance_sheet"
                    ).description
                ]
            except Exception as e:
                raise Exception(f"Error - Unexpected: {e}")

        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")

    def create_balance_sheet(self, current_year):
        
        # if the current_year is in the BUSINESS_years then we should have assets created for
        item_cogs_in_current_year_unsold = self.db.execute("SELECT SUM(cost) FROM inventory WHERE status = 'inventory' AND date_purchased LIKE ?", (f"{current_year}%",)).fetchone()[0] or 0

        previous_balance_sheet_years = self.db.execute("SELECT year FROM balance_sheet").fetchall()

        years_ = [int(row[0]) for row in previous_balance_sheet_years]

        if int(current_year) in years_:
            self.db.execute("UPDATE balance_sheet SET unsold_inventory = ? WHERE year = ?", (item_cogs_in_current_year_unsold, current_year))
        else:
            self.db.execute("INSERT INTO balance_sheet (year, unsold_inventory) VALUES (?, ?)", (current_year, item_cogs_in_current_year_unsold))
        self.conn.commit()
            
    def fetch_balance_sheet(self, amount):
        
        amounts = "all"

        if self.db and self.conn:
            if amount in amounts:
                match amount:
                    case "all":
                        return self.db.execute("SELECT * FROM balance_sheet").fetchall()

            else:
                if isinstance(amount, int):
                    return self.db.execute(
                        "SELECT * FROM balance_sheet LIMIT ?", (amount,)
                    ).fetchall()
                else:
                    raise ValueError(
                        f"Error: amount={amount} not in {amounts} or of type=int."
                    )
        else:
            raise sqlite3.ProgrammingError(f"Error: Database not connected.")


            

