import tkinter as tk

from tkinter import ttk

import sqlite3

from classes.expense_class import Expense

from classes.funcs import *


class ExpenseTab(ttk.Frame):
    def __init__(self, parent: tk.Tk | ttk.Notebook, text: str, database, BUSINESS, income_statement_tab):
        super().__init__(parent)
        self.database = database
        self.BUSINESS = BUSINESS
        self.income_statement_tab = income_statement_tab

        self.matrix_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.matrix_frame.config(width=850, height=730)
        self.matrix_frame.grid_propagate(False)
        self.matrix_frame.place(x=0, y=0)
        self.matrix_frame.grid_columnconfigure(0, weight=1)
        self.matrix_frame.grid_rowconfigure(0, weight=1)

        self.add_expense_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.add_expense_frame.config(
            width=1200 - 850 - 65, height=(730 / 1.5 - 5), padding=15
        )
        self.add_expense_frame.grid_propagate(False)
        self.add_expense_frame.place(x=860, y=0)

        self.add_expense_frame.rowconfigure(0, weight=1)  # Header Label
        self.add_expense_frame.rowconfigure(1, weight=1)  # Spacing
        self.add_expense_frame.rowconfigure(2, weight=1)  # Entry
        self.add_expense_frame.rowconfigure(3, weight=1)  # Entry
        self.add_expense_frame.rowconfigure(4, weight=1)  # Entry
        self.add_expense_frame.rowconfigure(5, weight=1)  # Entry
        self.add_expense_frame.rowconfigure(6, weight=1)  # Entry
        self.add_expense_frame.rowconfigure(7, weight=1)  # Add Expense Button
        self.add_expense_frame.rowconfigure(8, weight=1)  # Refresh Matrix Button
        self.add_expense_frame.rowconfigure(9, weight=1)  # Add Expense Status Label

        self.add_expense_frame.columnconfigure(0, weight=1)  # Entry Labels
        self.add_expense_frame.columnconfigure(1, weight=1)  # Entry Boxes

        # SEARCH EXPENSE FRAME

        self.search_expense_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.search_expense_frame.config(
            width=1200 - 850 - 65, height=(730 / 3 - 5), padding=20
        )
        self.search_expense_frame.grid_propagate(False)
        self.search_expense_frame.place(x=860, y=492)

        self.search_expense_frame.rowconfigure(0, weight=1)  # Header Label
        self.search_expense_frame.rowconfigure(1, weight=1)  # Expense Search Entry
        self.search_expense_frame.rowconfigure(2, weight=1)  # Expense Search Button
        self.search_expense_frame.rowconfigure(
            3, weight=1
        )  # Expense Search Clear Button
        self.search_expense_frame.rowconfigure(4, weight=1)  # Status Message Label

        self.search_expense_frame.columnconfigure(0, weight=2)  # Combo Box
        self.search_expense_frame.columnconfigure(1, weight=1)  # Item Search Entry

        # EXPENSES MATRIX

        self.expenses_matrix_headings = database.fetch_expenses_headings()

        self.expenses_matrix_tree = ttk.Treeview(
            self.matrix_frame, columns=self.expenses_matrix_headings, show="headings"
        )

        for index, heading in enumerate(self.expenses_matrix_headings, start=1):

            if heading in ("id"):
                self.expenses_matrix_tree.heading(f"#{index}", text=heading)
                self.expenses_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=35, width=40
                )

            elif heading in ("date", "cost", "category", "method", "note"):
                self.expenses_matrix_tree.heading(f"#{index}", text=heading)
                self.expenses_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=95, width=100
                )
            else:
                self.expenses_matrix_tree.heading(f"#{index}", text=heading, anchor="w")
                self.expenses_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=250, width=300
                )

        self.expenses_matrix_tree.grid(row=0, column=0, sticky="nsew")

        self.load_all_expenses_matrix()

        # ADD EXPENSE
        self.add_expense_label = ttk.Label(
            self.add_expense_frame,
            text="ADD EXPENSE",
            font=("Arial", 34),
            wraplength=200,
            justify="center",
            anchor="center",
        )
        self.add_expense_label.grid(row=0, column=0, columnspan=2)

        self.date_label = ttk.Label(self.add_expense_frame, text="Date")
        self.date_label.grid(row=1, column=0)
        self.date_entry = ttk.Entry(self.add_expense_frame)
        self.date_entry.grid(row=1, column=1)

        self.desc_label = ttk.Label(self.add_expense_frame, text="Desc.")
        self.desc_label.grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.add_expense_frame)
        self.desc_entry.grid(row=2, column=1)

        self.cost_label = ttk.Label(self.add_expense_frame, text="Cost")
        self.cost_label.grid(row=3, column=0)
        self.cost_entry = ttk.Entry(self.add_expense_frame)
        self.cost_entry.grid(row=3, column=1)

        self.categories = self.BUSINESS.expense_categories
        self.category_label = ttk.Label(self.add_expense_frame, text="Category")
        self.category_label.grid(row=4, column=0)
        self.category = ttk.Combobox(
            self.add_expense_frame, values=self.categories, width=15
        )
        self.category.grid(row=4, column=1, columnspan=3)

        self.methods = self.BUSINESS.expense_methods
        self.method_label = ttk.Label(self.add_expense_frame, text="Method")
        self.method_label.grid(row=5, column=0)
        self.method = ttk.Combobox(
            self.add_expense_frame, values=self.methods, width=15
        )
        self.method.grid(row=5, column=1)

        self.note_label = ttk.Label(self.add_expense_frame, text="Note")
        self.note_label.grid(row=6, column=0)
        self.note_entry = ttk.Entry(self.add_expense_frame)
        self.note_entry.grid(row=6, column=1)

        self.add_expense_button = ttk.Button(
            self.add_expense_frame,
            text="ADD EXPENSE",
            width=10,
            command=self.add_expense_to_expenses,
        )
        self.add_expense_button.grid(row=7, column=0, columnspan=2)

        self.refresh_expenses_matrix_button = ttk.Button(
            self.add_expense_frame,
            text="REFRESH",
            width=10,
            command=self.refresh_expenses_matrix,
        )
        self.refresh_expenses_matrix_button.grid(row=8, column=0, columnspan=2)

        self.add_expense_status_message_label = ttk.Label(
            self.add_expense_frame, text=f"Status: None"
        )
        self.add_expense_status_message_label.grid(row=9, column=0, columnspan=2)

        # SEARCH EXPENSE
        self.search_item_label = ttk.Label(
            self.search_expense_frame,
            text="SEARCH EXPENSE",
            font=("Arial", 34),
            wraplength=200,
            justify="center",
        )
        self.search_item_label.grid(row=0, column=0, columnspan=2)

        self.search_expense_filter = ttk.Combobox(
            self.search_expense_frame, values=self.expenses_matrix_headings
        )
        self.search_expense_filter.grid(row=1, column=0)
        self.search_expense_entry = ttk.Entry(self.search_expense_frame)
        self.search_expense_entry.grid(row=1, column=1)

        self.search_expense_button = ttk.Button(
            self.search_expense_frame,
            text="SEARCH",
            width=10,
            command=self.expenses_expense_search,
        )
        self.search_expense_button.grid(row=2, column=0, columnspan=2)

        self.search_expense_clear_button = ttk.Button(
            self.search_expense_frame,
            text="REFRESH",
            width=10,
            command=self.refresh_expenses_matrix,
        )
        self.search_expense_clear_button.grid(row=3, column=0, columnspan=2)

        self.search_expense_status_message_label = ttk.Label(
            self.search_expense_frame, text=f"Status: None"
        )
        self.search_expense_status_message_label.grid(row=4, column=0, columnspan=2)

    # EVENT FUNCTIONS

    def load_all_expenses_matrix(self):

        all_expenses = self.database.fetch_expenses(amount="all")

        self.clear_expenses_matrix()

        if all_expenses:

            for expense in all_expenses:
                expense = list(expense)
                expense[3] = cents_to_dollars(expense[3])
                self.expenses_matrix_tree.insert(
                    "", "end", iid=expense[0], values=expense
                )
            return True
        return False

    def clear_expenses_matrix(self):

        self.expenses_matrix_tree.delete(*self.expenses_matrix_tree.get_children())

    def add_expense_to_expenses(self):

        date = self.date_entry.get()
        desc = self.desc_entry.get()
        cost = self.cost_entry.get()
        category = self.category.get()
        method = self.method.get()
        note = self.note_entry.get()

        if date == "" or desc == "" or cost == "" or category == "" or method == "":
            self.add_expense_status_message_label.config(
                text="Status: Failed, blank entry!"
            )
            return False

        desc = desc.title()

        try:
            date = check_date(date)
            year = int(date[:4])
            if year not in self.BUSINESS.years:
                self.BUSINESS.years.append(year)
        except ValueError as e:
            self.add_expense_status_message_label.config(text=f"Status: Failed, {e}!")
            return False
        try:
            cost = check_cost(cost)
        except ValueError as e:
            self.add_expense_status_message_label.config(text=f"Status: Failed, {e}!")
            return False

        category = category
        method = method

        duplicate_expense = self.database.check_duplicate_expense(
            date=date, description=desc, cost=cost, category=category, method=method
        )

        if duplicate_expense:
            self.populate_matrix_via_duplicate(duplicate_expense)
            return False

        self.database.add_expense_to_expenses(
            date=date,
            description=desc,
            cost=cost,
            category=category,
            method=method,
            note=note,
        )
        self.refresh_expenses_matrix()
        self.add_expense_status_message_label.config(
            text="Status: Success, Expense Added!"
        )
        self.BUSINESS.save_business()
        self.database.create_income_statement([year])
        self.income_statement_tab.load_all_income_statements_into_matrix()
        return True

    def populate_matrix_via_duplicate(self, duplicates):
        if duplicates:
            self.clear_expenses_matrix()
            for duplicate in duplicates:
                duplicate = list(duplicate)
                duplicate[3] = cents_to_dollars(duplicate[3])
                self.expenses_matrix_tree.insert(
                    "", "end", iid=duplicate[0], values=duplicate
                )
            self.add_expense_status_message_label.config(
                text="Status: Failed, Duplicate Expense!"
            )
            return True
        return False

    def populate_matrix_via_search(self, expenses):
        if expenses:
            self.clear_expenses_matrix()
            for expense in expenses:
                expense = list(expense)
                expense[3] = cents_to_dollars(expense[3])
                self.expenses_matrix_tree.insert(
                    "", "end", iid=expense[0], values=expense
                )
            self.search_expense_status_message_label.config(
                text="Status: Success, Expense(s) Found!"
            )
            return True
        else:
            self.search_expense_status_message_label.config(
                text="Status: Failed, No Items Found!"
            )
            self.clear_expenses_matrix()
            return False

    def expenses_expense_search(self):
        column = self.search_expense_filter.get()
        value = self.search_expense_entry.get()

        if column == "" or (column == "" and value == ""):
            self.search_expense_status_message_label.config(
                text="Status: Failed, blank entry!"
            )
            return False
        # call func() within the DatabaseManger class to query for the specified value located within the given column.
        match column:

            case "id":
                try:
                    value = int(value)
                except (ValueError, TypeError):
                    self.search_expense_status_message_label.config(
                        text="Status: Failed, Item id=integer!"
                    )
                    return False
            case "date":
                try:
                    value = check_date(value)
                except ValueError:
                    self.search_expense_status_message_label.config(
                        text=f"Status: Failed, Invalid Date!"
                    )
                    return False

            case "description":
                value = value.title().strip()

            case "cost":
                try:
                    value = check_cost(value)
                    value = int(value)
                except (ValueError, TypeError):
                    self.search_expense_status_message_label.config(
                        text=f"Status: Failed, Item cost=integer!"
                    )
                    return False
            case "category":
                try:
                    value = value
                except ValueError:
                    self.search_expense_status_message_label.config(
                        text=f"Status: Failed, Invalid Category!"
                    )
                    return False
            case "method":
                try:
                    value = value
                except ValueError:
                    self.search_expense_status_message_label.config(
                        text=f"Status: Failed, Invalid Method!"
                    )
                    return False

        found_items = self.database.fetch_expenses_expense_search(column, value)
        return self.populate_matrix_via_search(found_items)

    def refresh_expenses_matrix(self):
        val = self.load_all_expenses_matrix()
        if val is True:
            self.add_expense_status_message_label.config(text="Status: Refreshed")
            self.search_expense_status_message_label.config(text="Status: Refreshed")
            return True
        self.add_expense_status_message_label.config(text="Status: No Expenses!")
        self.search_expense_status_message_label.config(text="Status: No Expenses!")
        return False
