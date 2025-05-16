import tkinter as tk

from tkinter import ttk

import datetime
from app.classes.funcs import *

class BalanceSheetTab(ttk.Frame):
    def __init__(self, parent: tk.Tk | ttk.Notebook, database, BUSINESS, income_statement_tab):
        super().__init__(parent)
        self.database = database
        self.BUSINESS = BUSINESS
        self.income_statement_tab = income_statement_tab
        self.current_year = str(datetime.date.today())[:4]

        # INCOME STATEMENT MATRIX FRAME
        self.balance_sheet_matrix_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.balance_sheet_matrix_frame.config(width=1200 - 55, height=730)
        self.balance_sheet_matrix_frame.grid_propagate(False)
        self.balance_sheet_matrix_frame.place(x=0, y=0)

        self.balance_sheet_matrix_frame.rowconfigure(0, weight=1)
        self.balance_sheet_matrix_frame.columnconfigure(0, weight=1)

        # INCOME STATMENT MATRIX

        self.balance_sheet_matrix_headings = database.fetch_balance_sheet_headings()
        self.balance_sheet_matrix_tree = ttk.Treeview(
            self.balance_sheet_matrix_frame,
            columns=self.balance_sheet_matrix_headings,
            show="headings",
        )

        for heading in self.balance_sheet_matrix_headings:
            match heading:
                case "year":
                    self.balance_sheet_matrix_tree.heading(heading, text=heading)
                    self.balance_sheet_matrix_tree.column(heading, anchor="w", minwidth=30, width=50)
                case _:
                    self.balance_sheet_matrix_tree.heading(heading, text=heading)
                    self.balance_sheet_matrix_tree.column(heading, anchor="w", minwidth=80, width=110)
        
        self.balance_sheet_matrix_tree.grid(row=0, column=0, sticky="nsew")
        
        self.database.create_balance_sheet(self.current_year)
        self.load_all_balance_sheets_into_matrix()

    # FUNCTIONS

    def load_all_balance_sheets_into_matrix(self):

        
        all_balance_sheets = self.database.fetch_balance_sheet(amount="all")

        # Clear the tree view before inserting new items
        self.clear_balance_sheet_matrix()

        if all_balance_sheets:
            for bs in all_balance_sheets:
                bs = list(bs)
                bs[1] = cents_to_dollars(bs[1])
                self.balance_sheet_matrix_tree.insert("", "end", iid=bs[0], values=bs)
            return True
        return False

    def clear_balance_sheet_matrix(self):
        self.balance_sheet_matrix_tree.delete(*self.balance_sheet_matrix_tree.get_children())
