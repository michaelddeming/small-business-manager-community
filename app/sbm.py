import tkinter as tk
from tkinter import ttk

# /-------------------------/ #
from app.tabs.balance_sheet_tab import BalanceSheetTab
from app.tabs.expenses_tab import ExpenseTab
from app.tabs.income_statement_tab import IncomeStatementTab
from app.tabs.inventory_tab import InventoryTab
from app.tabs.settings_tab import SettingsTab
from app.tabs.transactions_tab import TransactionsTab

from app.classes.dbmanager_class import DatabaseManager
from app.classes.business_class import Business


# /-------------------------------------------------/ #


def main():


    app = SmallBusinessManager()
    app.geometry("1200x800")
    app.resizable(width=False, height=False)

    # ---------------------------------------------------------- #
    # ----------------------- #
    #   Database Connection   #
    # ----------------------- #

    database = DatabaseManager()
    database.connect()

    # ---------------------------------------------------------- #
    # ---------------------- #
    #   Notebook For Tabs    #
    # ---------------------- #

    # Notebook Widget for Tabs
    tabControl = ttk.Notebook(app)
    tabControl.pack(fill="both", expand=True)

    # ---------------------------------------------------------- #
    # --------- #
    #   Tabs    #
    # --------- #

    # Income Statement Tab
    income_statement_tab = IncomeStatementTab(
        parent=tabControl,
        text="Income Statement",
        database=database,
        BUSINESS=app.BUSINESS,
    )

    # Expense Tab
    expense_tab = ExpenseTab(
        tabControl,
        "Expenses",
        database=database,
        BUSINESS=app.BUSINESS,
        income_statement_tab=income_statement_tab,
    )

    # Balance Sheet Tab
    balance_sheet_tab = BalanceSheetTab(
        tabControl,
        database=database,
        BUSINESS=app.BUSINESS,
        income_statement_tab=income_statement_tab,
    )

    # Inventory Tab
    inventory_tab = InventoryTab(
        tabControl,
        "Inventory",
        database=database,
        BUSINESS=app.BUSINESS,
        income_statement_tab=income_statement_tab,
        balance_sheet_tab=balance_sheet_tab,
    )
    # Transactions Tab
    transactions_tab = TransactionsTab(
        tabControl,
        database=database,
        BUSINESS=app.BUSINESS,
        inventory_tab=inventory_tab,
        income_statement_tab=income_statement_tab,
        balance_sheet_tab=balance_sheet_tab,
    )

    # Settings Tab
    settings_tab = SettingsTab(
        tabControl,
        BUSINESS=app.BUSINESS,
        app=app,
        inventory_tab=inventory_tab,
        expense_tab=expense_tab,
        transactions_tab=transactions_tab,
    )

    tabControl.add(inventory_tab, text="Inventory")
    tabControl.add(expense_tab, text="Expenses")
    tabControl.add(transactions_tab, text="Transactions")
    tabControl.add(income_statement_tab, text="Income Statement")
    tabControl.add(balance_sheet_tab, text="Balance Sheet")
    tabControl.add(settings_tab, text="Settings")
    # ---------------------------------------------------------- #
    # Main Loop
    app.mainloop()


# ---------------------------------------------------------------- #


class SmallBusinessManager(tk.Tk):

    def __init__(self):
        super().__init__()

        self.BUSINESS = Business()  # nested Business class
        self.BUSINESS.read_business()
        self.BUSINESS.save_business()  # save is before read bc in actual the prog will save on exit with latest info, then read back from that on launch. currently no save on exit.

        # self.BUSINESS.save_business() # move to event on exit or settings changes
        self.title(f"Small Business Manager: {self.BUSINESS.name}")
        self.lift()
        self.attributes("-topmost", True)


if __name__ == "__main__":
    main()
