import tkinter as tk

from tkinter import ttk

import sqlite3

from classes.transaction_class import Transaction

from classes.funcs import *


class TransactionsTab(ttk.Frame):
    def __init__(
        self, parent: tk.Tk | ttk.Notebook, database, BUSINESS, inventory_tab, income_statement_tab, balance_sheet_tab
    ):
        super().__init__(parent)
        self.database = database
        self.BUSINESS = BUSINESS
        self.inventory_tab = inventory_tab
        self.income_statement_tab = income_statement_tab
        self.balance_sheet_tab = balance_sheet_tab

        # TRANSACTIONS MATRIX FRAME
        self.matrix_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.matrix_frame.config(width=850, height=730)
        self.matrix_frame.grid_propagate(False)
        self.matrix_frame.place(x=0, y=0)
        self.matrix_frame.grid_columnconfigure(0, weight=1)
        self.matrix_frame.grid_rowconfigure(0, weight=1)

        # COMMIT TRANSACTIONS FRAME
        self.transaction_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.transaction_frame.config(
            width=1200 - 850 - 65, height=730 / 1.5 - 5, padding=15
        )
        self.transaction_frame.grid_propagate(False)
        self.transaction_frame.place(x=860, y=0)

        for i in range(15):
            self.transaction_frame.rowconfigure(i, weight=1)

        self.transaction_frame.columnconfigure(0, weight=1)
        self.transaction_frame.columnconfigure(1, weight=1)

        # SEARCH TRANSACTION FRAME
        self.search_transactions_frame = ttk.Frame(
            self, relief="solid", borderwidth=1, padding=15
        )
        self.search_transactions_frame.config(
            width=1200 - 850 - 65, height=(730 / 3 - 5)
        )
        self.search_transactions_frame.grid_propagate(False)
        self.search_transactions_frame.place(x=860, y=492)

        self.search_transactions_frame.rowconfigure(0, weight=1)  # Header Label
        self.search_transactions_frame.rowconfigure(1, weight=1)  # Item Search Entry
        self.search_transactions_frame.rowconfigure(2, weight=1)  # Item Search Button
        self.search_transactions_frame.rowconfigure(
            3, weight=1
        )  # Item Search Clear Button
        self.search_transactions_frame.rowconfigure(
            4, weight=1
        )  # Search Transactio Status Message Label

        self.search_transactions_frame.columnconfigure(0, weight=3)  # Combo Box
        self.search_transactions_frame.columnconfigure(1, weight=1)  # Item Search Entry

        # MATRIX

        self.transactions_matrix_headings = database.fetch_transactions_headings()

        self.transactions_matrix_tree = ttk.Treeview(
            self.matrix_frame,
            columns=self.transactions_matrix_headings,
            show="headings",
        )

        for index, heading in enumerate(self.transactions_matrix_headings, start=1):

            if heading in ("id", "type", "item_id", "fee", "discount", "item_amount"):
                self.transactions_matrix_tree.heading(f"#{index}", text=heading)
                self.transactions_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=20, width=35
                )

            elif heading in ("sale_platform", "transportation", "note"):
                self.transactions_matrix_tree.heading(f"#{index}", text=heading)
                self.transactions_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=65, width=75
                )

            elif heading in ("transportation_charge", "transaction_total", "date"):
                self.transactions_matrix_tree.heading(f"#{index}", text=heading)
                self.transactions_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=85, width=85
                )

        self.transactions_matrix_tree.grid(row=0, column=0, sticky="nsew")

        self.load_all_trasactions_matrix()

        # COMMIT TRANSACTION
        self.commit_transaction_label = ttk.Label(
            self.transaction_frame,
            text="COMMIT TRANSACTION",
            font=("Arial", 34),
            wraplength=250,
            justify="center",
        )
        self.commit_transaction_label.grid(row=0, column=0, columnspan=2)

        self.transaction_type_label = ttk.Label(self.transaction_frame, text="Trans. Type", wraplength=50)
        self.transaction_type_label.grid(row=2, column=0)

        transaction_types = ["sale", "return"]
        self.transaction_type_entry = ttk.Combobox(self.transaction_frame, values=transaction_types, width=15)
        self.transaction_type_entry.grid(row=2, column=1)

        self.date_label = ttk.Label(self.transaction_frame, text="Date")
        self.date_label.grid(row=3, column=0)
        self.date_entry = ttk.Entry(self.transaction_frame)
        self.date_entry.grid(row=3, column=1)

        self.item_id_label = ttk.Label(self.transaction_frame, text="Item ID")
        self.item_id_label.grid(row=4, column=0)
        self.item_id_entry = ttk.Entry(self.transaction_frame)
        self.item_id_entry.grid(row=4, column=1)

        self.item_amount_label = ttk.Label(
            self.transaction_frame, text="Item Amount", wraplength=50, justify="center"
        )
        self.item_amount_label.grid(row=5, column=0)
        self.item_amount_entry = ttk.Entry(self.transaction_frame)
        self.item_amount_entry.grid(row=5, column=1)

        sale_platforms = (
            self.BUSINESS.sale_platforms
        )  # make a part of the business class, import business class instance as param to the TransactionsTab
        self.plaform_label = ttk.Label(
            self.transaction_frame,
            text="Sale Platform",
            wraplength=60,
            justify="center",
        )
        self.plaform_label.grid(row=6, column=0)
        self.platform = ttk.Combobox(
            self.transaction_frame, values=sale_platforms, width=15
        )
        self.platform.grid(row=6, column=1, columnspan=3)

        self.transportation_methods = self.BUSINESS.transportation_methods
        self.transport_method_label = ttk.Label(
            self.transaction_frame,
            text="Transp. Method",
            wraplength=50,
            justify="center",
        )
        self.transport_method_label.grid(row=7, column=0)
        self.transport_method = ttk.Combobox(
            self.transaction_frame, values=self.transportation_methods, width=15
        )
        self.transport_method.grid(row=7, column=1)

        self.transport_charge_label = ttk.Label(
            self.transaction_frame,
            text="Transp. Charge",
            wraplength=50,
            justify="center",
        )
        self.transport_charge_label.grid(row=8, column=0)
        self.transport_charge_entry = ttk.Entry(self.transaction_frame)
        self.transport_charge_entry.grid(row=8, column=1)

        self.fee_label = ttk.Label(self.transaction_frame, text="Fee")
        self.fee_label.grid(row=9, column=0)
        self.fee_entry = ttk.Entry(self.transaction_frame)
        self.fee_entry.grid(row=9, column=1)

        self.discount_label = ttk.Label(self.transaction_frame, text="Discount")
        self.discount_label.grid(row=10, column=0)
        self.discount_entry = ttk.Entry(self.transaction_frame)
        self.discount_entry.grid(row=10, column=1)

        self.note_label = ttk.Label(self.transaction_frame, text="Note")
        self.note_label.grid(row=11, column=0)
        self.note_entry = ttk.Entry(self.transaction_frame)
        self.note_entry.grid(row=11, column=1)

        self.commit_transaction_button = ttk.Button(
            self.transaction_frame,
            text="COMMIT TRANSACTION",
            command=self.add_transaction_to_transactions,
        )
        self.commit_transaction_button.grid(row=12, column=0, columnspan=2)

        self.refresh_transactions_button = ttk.Button(
            self.transaction_frame,
            text="REFRESH",
            command=self.refresh_transactions_matrix,
        )
        self.refresh_transactions_button.grid(row=13, column=0, columnspan=2)

        self.commit_transaction_status_label = ttk.Label(
            self.transaction_frame, text=f"Status: None", wraplength=200
        )
        self.commit_transaction_status_label.grid(row=14, column=0, columnspan=2)

        # SEARCH TRANSACTIONS
        self.commit_transaction_label = ttk.Label(
            self.search_transactions_frame,
            text="SEARCH TRANSACTION",
            font=("Arial", 34),
            wraplength=300,
            justify="center",
            anchor="center",
        )
        self.commit_transaction_label.grid(row=0, column=0, columnspan=2)

        self.search_transactions_filter = ttk.Combobox(
            self.search_transactions_frame, values=self.transactions_matrix_headings
        )
        self.search_transactions_filter.grid(row=1, column=0)
        self.search_transactions_entry = ttk.Entry(self.search_transactions_frame)
        self.search_transactions_entry.grid(row=1, column=1)

        self.search_transactions_button = ttk.Button(
            self.search_transactions_frame,
            text="SEARCH",
            command=self.transactions_transaction_search,
        )
        self.search_transactions_button.grid(row=2, column=0, columnspan=2)

        self.search_transactions_clear_button = ttk.Button(
            self.search_transactions_frame,
            text="REFRESH",
            command=self.refresh_transactions_matrix,
        )
        self.search_transactions_clear_button.grid(row=3, column=0, columnspan=2)

        self.search_transactions_status_message_label = ttk.Label(
            self.search_transactions_frame, text=f"Status: None", wraplength=200
        )
        self.search_transactions_status_message_label.grid(
            row=4, column=0, columnspan=2
        )

    # EVENT FUNCTIONS

    # ADD TRANSACTION

    def add_transaction_to_transactions(self):

        trans_type = self.transaction_type_entry.get()
        
        match trans_type:
            case "sale":

                entries = [trans_type,
                date := self.date_entry.get(),
                item_id := self.item_id_entry.get(),
                item_amount := self.item_amount_entry.get(),
                sale_platform := self.platform.get(),
                transportation_method := self.transport_method.get(),
                transportation_charge := self.transport_charge_entry.get(),
                fee := self.fee_entry.get(),
                discount := self.discount_entry.get(),]
                
                note = self.note_entry.get()

                # No Entry field or ComboBox for Commit Transaction is allowed to be empty EXCEPT for the 'note_entry' as no note is permitted.
                if any(entry == "" for entry in entries):
                    self.commit_transaction_status_label.config(
                        text="Status: Failed, blank entry"
                    )
                    return False

                # Check the Date for validity within the aux functions.
                try:
                    date = check_date(date)
                    trans_year = int(date[:4])
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, date={e}!"
                    )
                    return False

                # Check the Item ID for validity within the Database
                try:
                    item_id = self.database.check_item_id(item_id)
                except ValueError as e:
                    self.commit_transaction_status_label.config(text=f"Status: Failed, {e}!")
                    return False

                # Check the Item sale amount for validity within the aux functions.
                try:
                    item_amount = check_cost(item_amount)
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, item_amount={e}!"
                    )
                    return False

                # Check the Sale Platform for validity within the BUSINESS object.
                try:
                    sale_platform = self.BUSINESS.check_sale_platform(sale_platform)
                except ValueError as e:
                    self.commit_transaction_status_label.config(text=f"Status: Failed, {e}!")
                    return False

                # Check the Transportation Method for validity within the BUSINESS object.
                try:
                    transportation_method = self.BUSINESS.check_transportation_method(
                        transportation_method
                    )
                except ValueError as e:
                    self.commit_transaction_status_label.config(text=f"Status: Failed, {e}!")
                    return False

                # Check the transportation charge amount for validity within the aux functions.
                try:
                    transportation_charge = check_cost(transportation_charge)
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, transportation_charge={e}!"
                    )
                    return False

                # Check the Fee amount for validity within the aux functions.
                try:
                    fee = check_cost(fee)
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, fee={e}!"
                    )
                    return False

                # Check the Discount amount for validity within the aux functions.
                try:
                    discount = check_cost(discount)
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, discount={e}!"
                    )
                    return False

                item_status = self.database.check_item_status(item_id)
                if item_status[0][0] == "sold":
                    item_transactions = self.database.check_duplicate_transaction(item_id)
                    if item_transactions:
                        self.populate_transactions_matrix_via_duplicate(item_transactions)
                    self.commit_transaction_status_label.config(text=f"Status: Failed, item_id={item_id} Already Sold!")
                    return False
                else:
                    self.database.add_transaction_to_transactons(
                        date=date,
                        type=trans_type,
                        item_id=item_id,
                        item_amount=item_amount,
                        sale_platform=sale_platform,
                        transportation_method=transportation_method,
                        transportation_charge=transportation_charge,
                        fee=fee,
                        discount=discount,
                        note=note,)
                    self.database.convert_item_status_sold(item_id)
                    self.database.create_income_statement([trans_year])
                    self.commit_transaction_status_label.config(
                    text=f"Status: Success, Sale Transaction Committed!")
        
            
            case "return":
                
                required_entries = [trans_type,
                date := self.date_entry.get(),
                item_id := self.item_id_entry.get(),
                item_amount := self.item_amount_entry.get(),]
                
                nonrequired_entries = [sale_platform := self.platform.get(),
                transportation_method := self.transport_method.get(),
                transportation_charge := self.transport_charge_entry.get(),
                fee := self.fee_entry.get(),
                discount := self.discount_entry.get(),
                note := self.note_entry.get()]
                

                if any(entry == "" for entry in required_entries):
                    self.commit_transaction_status_label.config(
                        text="Status: Failed, blank entry!"
                    )
                    return False
                if any(entry != "" for entry in nonrequired_entries):
                    self.commit_transaction_status_label.config(
                        text="Status: Failed, unwanted entry!"
                    )
                    return False
                
                # Check the Date for validity within the aux functions.
                try:
                    date = check_date(date)
                    trans_year = int(date[:4])
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, date={e}!"
                    )
                    return False

                # Check the Item ID for validity within the Database
                try:
                    item_id = self.database.check_item_id(item_id)
                except ValueError as e:
                    self.commit_transaction_status_label.config(text=f"Status: Failed, {e}!")
                    return False

                # Check the Item return amount for validity within the aux functions.
                try:
                    item_amount = check_cost(item_amount)
                except ValueError as e:
                    self.commit_transaction_status_label.config(
                        text=f"Status: Failed, item_amount={e}!"
                    )
                    return False
                
                # set the custom note for item return if needed
                item_status = self.database.check_item_status(item_id)
                if item_status[0][0] == "inventory":
                    item_transactions = self.database.check_duplicate_transaction(item_id)
                    if item_transactions:
                        self.populate_transactions_matrix_via_duplicate(item_transactions)
                    self.commit_transaction_status_label.config(text=f"Status: Failed, item_id={item_id} in inventory!")
                    return False
                else:
                    self.database.add_transaction_to_transactons(
                    date=date,
                    type=trans_type,
                    item_id=item_id,
                    item_amount=item_amount,
                    sale_platform="n/a",
                    transportation_method="n/a",
                    transportation_charge=transportation_charge,
                    fee=0,
                    discount=0,
                    note=f"RET. ITEM_ID={item_id}",)
                    self.database.convert_item_status_inventory(item_id)
                    self.database.create_income_statement([trans_year])
                    self.commit_transaction_status_label.config(
                    text=f"Status: Success, Return Transaction Committed!"
                )
            case _:
                self.commit_transaction_status_label.config(
                text="Status: Failed, Invalid Transaction Type!"
                )
                return False
        
        self.refresh_transactions_matrix()
        self.inventory_tab.load_all_inventory_matrix()
        self.income_statement_tab.load_all_income_statements_into_matrix()
        self.database.create_balance_sheet(trans_year)
        self.balance_sheet_tab.load_all_balance_sheets_into_matrix()
        return True
    
        
    def transactions_transaction_search(self):
        column = self.search_transactions_filter.get()
        value = self.search_transactions_entry.get()

        if column == "" or (column == "" and value == ""):
            self.search_transactions_status_message_label.config(
                text="Status: Failed, blank entry!"
            )
            return False
        # call func() within the DatabaseManger class to query for the specified value located within the given column.
        match column:

            case "id":
                try:
                    value = int(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text="Status: Failed, Item id=integer!"
                    )
                    return False
            case "type":
                try:
                    if value not in ("sale", "return"):
                        raise ValueError("Invalid Transaction Type")
                except (ValueError, TypeError) as e:
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, {e}!"
                    )
                    return False
            case "date":
                try:
                    value = check_date(value)
                except ValueError:
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, Invalid Date!"
                    )
                    return False
            case "item_id":
                try:
                    value = self.database.check_item_id(int(value))
                except ValueError as e:
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, {e}!"
                    )
                    return False
            case "item_amount":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, item_amount=integer!"
                    )
                    return False
            case "sale_platform":
                try:
                    value = self.BUSINESS.check_sale_platform(value)
                except ValueError as e:
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, {e}!"
                    )
                    return False
            case "transportation":
                try:
                    value = self.BUSINESS.check_transportation_method(value)
                except ValueError as e:
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, {e}!"
                    )
                    return False
            case "transportation_charge":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, transportation_charge=integer!"
                    )
                    return False
            case "fee":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, fee=integer!"
                    )
                    return False
            case "discount":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, discount=integer!"
                    )
                    return False
            case "transaction_total":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_transactions_status_message_label.config(
                        text=f"Status: Failed, transaction_total=integer!"
                    )
                    return False

        found_items = self.database.fetch_transactions_transaction_search(column, value)
        return self.populate_trasactions_matrix_via_search(found_items)

    def load_all_trasactions_matrix(self):

        all_transactions = self.database.fetch_transactions(amount="all")

        self.clear_transactions_matrix()

        if all_transactions:
            indexes = (4, 7, 8, 9, 10)
            for transaction in all_transactions:
                transaction = list(transaction)
                for index in indexes:
                    try:
                        transaction[index] = cents_to_dollars(transaction[index])
                    except ValueError:
                        transaction[index] = 0.0
                self.transactions_matrix_tree.insert(
                    "", "end", iid=transaction[0], values=transaction
                )
            return True
        return False

    def clear_transactions_matrix(self):

        self.transactions_matrix_tree.delete(
            *self.transactions_matrix_tree.get_children()
        )

    def refresh_transactions_matrix(self):
        val = self.load_all_trasactions_matrix()
        if val is True:
            self.commit_transaction_status_label.config(text="Status: Refreshed")
            self.search_transactions_status_message_label.config(
                text="Status: Refreshed"
            )
            return True
        self.commit_transaction_status_label.config(text="Status: No Transactions!")
        self.search_transactions_status_message_label.config(
            text="Status: Transactions!"
        )
        return False

    def populate_trasactions_matrix_via_search(self, found_transactions):
        if found_transactions:
            self.clear_transactions_matrix()
            indexes = (4, 7, 8, 9, 10)
            for transaction in found_transactions:
                transaction = list(transaction)
                for index in indexes:
                    try:
                        transaction[index] = cents_to_dollars(transaction[index])
                    except ValueError:
                        transaction[index] = 0.0
                self.transactions_matrix_tree.insert(
                    "", "end", iid=transaction[0], values=transaction
                )
            self.search_transactions_status_message_label.config(
                text="Status: Success, Transactions Found!"
            )
            return True
        else:
            self.search_transactions_status_message_label.config(
                text="Status: Failed, No Transactions Found!"
            )
            self.clear_transactions_matrix()
            return False

    def populate_transactions_matrix_via_duplicate(self, duplicate_transaction):
        if duplicate_transaction:
            print(duplicate_transaction)
            self.clear_transactions_matrix()
            indexes = (4, 7, 8, 9, 10)
            for transaction in duplicate_transaction:
                transaction = list(transaction)
                for index in indexes:
                    try:
                        transaction[index] = cents_to_dollars(transaction[index])
                    except ValueError:
                        transaction[index] = 0.0
                self.transactions_matrix_tree.insert(
                    "", "end", iid=transaction[0], values=transaction
                )
            self.commit_transaction_status_label.config(
                text=f"Status: Failed, Duplicate Transaction!"
            )
            return True
        return False
