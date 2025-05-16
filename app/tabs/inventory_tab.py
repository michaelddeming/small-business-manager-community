import tkinter as tk

from tkinter import ttk

from classes.item_class import Item

from classes.funcs import *


class InventoryTab(ttk.Frame):
    def __init__(
        self,
        parent: tk.Tk | ttk.Notebook,
        text: str,
        database,
        BUSINESS,
        income_statement_tab,
        balance_sheet_tab
    ):
        super().__init__(parent)
        self.database = database
        self.BUSINESS = BUSINESS
        self.income_statement_tab = income_statement_tab
        self.balance_sheet_tab=balance_sheet_tab

        # INVENTORY MATRIX FRAME
        self.matrix_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.matrix_frame.config(width=850, height=730)
        self.matrix_frame.grid_propagate(False)
        self.matrix_frame.place(x=0, y=0)
        self.matrix_frame.grid_columnconfigure(0, weight=1)
        self.matrix_frame.grid_rowconfigure(0, weight=1)

        # ADD ITEM FRAME
        self.add_item_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.add_item_frame.config(
            width=1200 - 850 - 65, height=(730 / 1.5 - 5), padding=20
        )
        self.add_item_frame.grid_propagate(False)
        self.add_item_frame.place(x=860, y=0)

        self.add_item_frame.rowconfigure(0, weight=1)  # Header Label
        self.add_item_frame.rowconfigure(1, weight=1)  # Spacing
        self.add_item_frame.rowconfigure(2, weight=1)  # Entry
        self.add_item_frame.rowconfigure(3, weight=1)  # Entry
        self.add_item_frame.rowconfigure(4, weight=1)  # Entry
        self.add_item_frame.rowconfigure(5, weight=1)  # Entry
        self.add_item_frame.rowconfigure(6, weight=1)  # Entry
        self.add_item_frame.rowconfigure(7, weight=1)  # Add Item Button
        self.add_item_frame.rowconfigure(8, weight=1)  # Refresh Matrix Button

        self.add_item_frame.columnconfigure(0, weight=1)  # Entry Labels
        self.add_item_frame.columnconfigure(1, weight=1)  # Entry Boxes

        self.search_item_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.search_item_frame.config(
            width=1200 - 850 - 65, height=(730 / 3 - 5), padding=20
        )
        self.search_item_frame.grid_propagate(False)
        self.search_item_frame.place(x=860, y=492)

        self.search_item_frame.rowconfigure(0, weight=1)  # Header Label
        self.search_item_frame.rowconfigure(1, weight=1)  # Item Search Entry
        self.search_item_frame.rowconfigure(2, weight=1)  # Item Search Button
        self.search_item_frame.rowconfigure(3, weight=1)  # Item Search Clear Button
        self.search_item_frame.rowconfigure(4, weight=1)  # Status Message Label

        self.search_item_frame.columnconfigure(0, weight=1)  # Combo Box
        self.search_item_frame.columnconfigure(1, weight=1)  # Item Search Entry

        # MATRIX

        self.inventory_matrix_headings = database.fetch_inventory_headings()

        self.inventory_matrix_tree = ttk.Treeview(
            self.matrix_frame, columns=self.inventory_matrix_headings, show="headings"
        )

        for index, heading in enumerate(self.inventory_matrix_headings, start=1):

            if heading in ("id", "size"):
                self.inventory_matrix_tree.heading(f"#{index}", text=heading)
                self.inventory_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=35, width=40
                )

            elif heading in ("date_purchased", "cost", "status"):
                self.inventory_matrix_tree.heading(f"#{index}", text=heading)
                self.inventory_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=95, width=100
                )
            else:
                self.inventory_matrix_tree.heading(
                    f"#{index}", text=heading, anchor="w"
                )
                self.inventory_matrix_tree.column(
                    f"#{index}", anchor="w", minwidth=300, width=350
                )

        self.inventory_matrix_tree.grid(row=0, column=0, sticky="nsew")

        self.load_all_inventory_matrix()

        # ADD ITEM
        self.add_item_label = ttk.Label(
            self.add_item_frame,
            text="ADD ITEM",
            font=("Arial", 34),
            wraplength=100,
            justify="center",
            anchor="center",
        )
        self.add_item_label.grid(row=0, column=0, columnspan=2)

        self.date_purchased_entry_label = ttk.Label(self.add_item_frame, text="Date")
        self.date_purchased_entry_label.grid(row=1, column=0)
        self.date_purchased_entry = ttk.Entry(self.add_item_frame)
        self.date_purchased_entry.grid(row=1, column=1)

        self.item_desc_entry_label = ttk.Label(self.add_item_frame, text="Desc.")
        self.item_desc_entry_label.grid(row=2, column=0)
        self.item_desc_entry = ttk.Entry(self.add_item_frame)
        self.item_desc_entry.grid(row=2, column=1)

        self.item_size_entry_label = ttk.Label(self.add_item_frame, text="Size")
        self.item_size_entry_label.grid(row=3, column=0)
        self.item_size_entry = ttk.Combobox(self.add_item_frame, values=BUSINESS.item_sizes, width=15)
        self.item_size_entry.grid(row=3, column=1)

        self.item_cost_entry_label = ttk.Label(self.add_item_frame, text="Cost")
        self.item_cost_entry_label.grid(row=4, column=0)
        self.item_cost_entry = ttk.Entry(self.add_item_frame)
        self.item_cost_entry.grid(row=4, column=1)

        self.add_item_button = ttk.Button(
            self.add_item_frame,
            text="ADD ITEM",
            width=7,
            command=self.add_item_to_inventory,
        )
        self.add_item_button.grid(row=5, column=0, columnspan=2)

        self.add_item_refresh_matrix_button = ttk.Button(
            self.add_item_frame,
            text="REFRESH",
            width=7,
            command=self.refresh_all_inventory_matrix,
        )
        self.add_item_refresh_matrix_button.grid(row=6, column=0, columnspan=2)

        self.add_item_status_message_label = ttk.Label(
            self.add_item_frame, text=f"Status: None", wraplength=200, justify="center"
        )
        self.add_item_status_message_label.grid(row=7, column=0, columnspan=2)

        # SEARCH ITEM
        self.search_item_label = ttk.Label(
            self.search_item_frame,
            text="SEARCH ITEM",
            font=("Arial", 34),
            wraplength=150,
            justify="center",
            anchor="center",
        )
        self.search_item_label.grid(row=0, column=0, columnspan=2)

        self.search_item_filter = ttk.Combobox(
            self.search_item_frame, values=self.inventory_matrix_headings
        )
        self.search_item_filter.grid(row=1, column=0)
        self.search_item_entry = ttk.Entry(self.search_item_frame)
        self.search_item_entry.grid(row=1, column=1)

        self.search_item_button = ttk.Button(
            self.search_item_frame,
            text="SEARCH",
            width=7,
            command=self.command_inventory_item_search,
        )
        self.search_item_button.grid(row=2, column=0, columnspan=2)

        self.search_item_refresh_matrix_button = ttk.Button(
            self.search_item_frame,
            text="REFRESH",
            width=7,
            command=self.refresh_all_inventory_matrix,
        )
        self.search_item_refresh_matrix_button.grid(row=3, column=0, columnspan=2)

        self.search_item_status_message_label = ttk.Label(
            self.search_item_frame, text=f"Status: None"
        )
        self.search_item_status_message_label.grid(row=4, column=0, columnspan=2)

    # EVENT FUNCTIONS

    # ADD ITEM

    def add_item_to_inventory(self):

        date_purchased = self.date_purchased_entry.get()
        item_description = self.item_desc_entry.get()
        item_size = self.item_size_entry.get()
        item_cost = self.item_cost_entry.get()

        if (
            date_purchased == ""
            or item_description == ""
            or item_size == ""
            or item_cost == ""
        ):
            self.add_item_status_message_label.config(
                text="Status: Failed, blank entry!"
            )
            return False

        item_description = item_description.title()  # Force title case on Item Desc.

        try:
            date_purchased = check_date(date_purchased)
            year = int(date_purchased[:4])
            # add the year to the BUSINESS years set
            if year not in self.BUSINESS.years:
                self.BUSINESS.years.append(year)
        except ValueError as e:
            self.add_item_status_message_label.config(text=f"Status: Failed, {e}!")
            return False
        try:
            item_size = check_size(item_size, BUSINESS=self.BUSINESS)
        except ValueError as e:
            self.add_item_status_message_label.config(text=f"Status: Failed, {e}!")
            return False
        try:
            item_cost = check_cost(item_cost)
        except ValueError as e:
            self.add_item_status_message_label.config(text=f"Status: Failed, {e}!")
            return False

        duplicate_item = self.database.check_duplicate_item(
            date_purchased=date_purchased,
            item_desc=item_description,
            item_size=item_size,
            item_cost=item_cost,
        )
        if duplicate_item:
            self.populate_matrix_via_duplicate(duplicate_item)
            return False
        self.database.add_item_to_inventory(
            date_purchased=date_purchased,
            item_desc=item_description,
            item_size=item_size,
            item_cost=item_cost,
            status="inventory",
        )
        self.database.create_balance_sheet(date_purchased[:4])
        self.balance_sheet_tab.load_all_balance_sheets_into_matrix()
        self.refresh_all_inventory_matrix()
        self.add_item_status_message_label.config(text=f"Status: Success, Item Added!")
        self.BUSINESS.save_business()
        return True

    def load_all_inventory_matrix(self):

        all_inventory = self.database.fetch_inventory(amount="all")
        # Clear the tree view before inserting new items
        self.clear_inventory_matrix()

        if all_inventory:
            for item in all_inventory:
                item = list(item)
                item[4] = cents_to_dollars(item[4])
                self.inventory_matrix_tree.insert("", "end", iid=item[0], values=item)
            return True
        return False

    def refresh_all_inventory_matrix(self):

        val = self.load_all_inventory_matrix()
        if val is True:
            self.add_item_status_message_label.config(text="Status: Refreshed")
            self.search_item_status_message_label.config(text="Status: Refreshed")
            return True
        self.add_item_status_message_label.config(text="Status: No Items!")
        self.search_item_status_message_label.config(text="Status: No Items!")
        return False

    def clear_inventory_matrix(self):
        self.inventory_matrix_tree.delete(*self.inventory_matrix_tree.get_children())

    def command_inventory_item_search(self):
        column = self.search_item_filter.get()
        value = self.search_item_entry.get()

        if column == "" or value == "":
            self.search_item_status_message_label.config(
                text="Status: Failed, blank entry!"
            )
            return False
        # call func() within the DatabaseManger class to query for the specified value located within the given column.
        match column:

            case "id":
                try:
                    value = int(value)
                except (ValueError, TypeError):
                    self.search_item_status_message_label.config(
                        text="Status: Failed, Item id=integer!"
                    )
                    return False
            case "cost":
                try:
                    value = check_cost(value)
                except (ValueError, TypeError):
                    self.search_item_status_message_label.config(
                        text=f"Status: Failed, Item cost=integer!"
                    )
                    return False
            case "size":
                try:
                    value = check_size(value, self.BUSINESS)
                except ValueError:
                    self.search_item_status_message_label.config(
                        text=f"Status: Failed, Invalid Size!"
                    )
                    return False
            case "date_purchased":
                try:
                    value = check_date(value)
                except ValueError:
                    self.search_item_status_message_label.config(
                        text=f"Status: Failed, Invalid Date!"
                    )
                    return False
            case "description":
                value = value.title().strip()

        found_items = self.database.fetch_inventory_item_search(column, value)
        return self.populate_matrix_via_search(found_items)

    def populate_matrix_via_search(self, items: list):
        if items:
            self.clear_inventory_matrix()
            for item in items:
                item = list(item)
                item[4] = cents_to_dollars(item[4])
                self.inventory_matrix_tree.insert("", "end", iid=item[0], values=item)
            self.search_item_status_message_label.config(
                text="Status: Success, Items Found!"
            )
            return True
        else:
            self.search_item_status_message_label.config(
                text="Status: Failed, No Items Found!"
            )
            self.clear_inventory_matrix()
            return False

    def populate_matrix_via_duplicate(self, items: list):
        if items:
            self.clear_inventory_matrix()
            for item in items:
                item = list(item)
                item[4] = cents_to_dollars(item[4])
                self.inventory_matrix_tree.insert("", "end", iid=item[0], values=item)
            self.add_item_status_message_label.config(
                text="Status: Failed, Duplicate Item!"
            )
            return True
        return False
