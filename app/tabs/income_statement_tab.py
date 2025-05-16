import tkinter as tk

from tkinter import ttk

from app.classes.funcs import *

class IncomeStatementTab(ttk.Frame):
    def __init__(self, parent: tk.Tk | ttk.Notebook, text: str, database, BUSINESS):
        super().__init__(parent)
        self.database = database
        self.BUSINESS = BUSINESS

        # INCOME STATEMENT MATRIX FRAME
        self.income_statment_matrix_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.income_statment_matrix_frame.config(width=1200 - 55, height=730)
        self.income_statment_matrix_frame.grid_propagate(False)
        self.income_statment_matrix_frame.place(x=0, y=0)

        self.income_statment_matrix_frame.rowconfigure(0, weight=1)
        self.income_statment_matrix_frame.columnconfigure(0, weight=1)

        # INCOME STATMENT MATRIX

        self.income_statment_matrix_headings = database.fetch_income_statement_headings()
        self.income_statement_matrix_tree = ttk.Treeview(
            self.income_statment_matrix_frame,
            columns=self.income_statment_matrix_headings,
            show="headings",
        )

        for heading in self.income_statment_matrix_headings:
            match heading:
                case "year":
                    self.income_statement_matrix_tree.heading(heading, text=heading)
                    self.income_statement_matrix_tree.column(heading, anchor="w", minwidth=40, width=50)
                case "discounts", "fees":
                    self.income_statement_matrix_tree.heading(heading, text=heading)
                    self.income_statement_matrix_tree.column(heading, anchor="w", minwidth=50, width=60)
                case _:
                    self.income_statement_matrix_tree.heading(heading, text=heading)
                    self.income_statement_matrix_tree.column(heading, anchor="w", minwidth=95, width=110)
        
        self.income_statement_matrix_tree.grid(row=0, column=0, sticky="nsew")
        
        self.database.create_income_statement(self.BUSINESS.years)
        self.load_all_income_statements_into_matrix()





# FUNCTIONS

# MATRIX FUNCTIONS

    def load_all_income_statements_into_matrix(self):

        all_income_statements = self.database.fetch_income_statements("all")

        self.clear_income_statement_matrix_tree()

        if all_income_statements:

            for income_statement in all_income_statements:

                income_statement = list(income_statement)
                for i in range(1, 11):

                    income_statement[i] = cents_to_dollars(income_statement[i])
                self.income_statement_matrix_tree.insert("", "end", iid=income_statement[0], values=income_statement)
                
            return True
        return False

    def clear_income_statement_matrix_tree(self):

        self.income_statement_matrix_tree.delete(
            *self.income_statement_matrix_tree.get_children()
        )
