import tkinter as tk

from tkinter import ttk

from classes.funcs import *

class SettingsTab(ttk.Frame):
    def __init__(self, parent: tk.Tk | ttk.Notebook, BUSINESS, app, inventory_tab, expense_tab, transactions_tab):
        super().__init__(parent)
        self.BUSINESS = BUSINESS
        self.app = app
        self.inventory_tab = inventory_tab
        self.expense_tab = expense_tab
        self.transactions_tab = transactions_tab


        # class Setting(ttk.Frame):
        #     def __init__(self, parent, label_text, data_list, add_dropdown_text, remove_dropdown_text, button_text):
        #         super().__init__(parent)
        #         self.label_text = label_text
        #         self.data_list = data_list
        #         self.add_dropdown_text = add_dropdown_text
        #         self.remove_dropdown_text = remove_dropdown_text
        #         self.button_text = button_text
                
        #         current_data_label = ttk.Label(parent, text=self.label_text)
        #         current_data_listed_label = ttk.Label(parent, self.data_list)
        #         current_data_label.grid(row=0,column=0, sticky="e",padx=20)
        #         current_data_listed_label.grid(row=0,column=1, sticky="w")
            

                
        #         add_remove_data_option = ttk.Combobox(parent, values=[self.add_dropdown_text, self.remove_dropdown_text], width=10)
        #         add_remove_data_entry = ttk.Entry(parent)
        #         add_remove_data_option.grid(row=1,column=0, sticky="e",padx=20)
        #         add_remove_data_entry.grid(row=1,column=1, sticky="w")

        #         update_data_button = ttk.Button(parent, text=self.button_text, width=20)
        #         update_data_button.grid(row=2, column=0, columnspan=2)


        # SETTINGS FRAME

        self.settings_frame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.settings_frame.config(width=1200 - 55, height=730)
        self.settings_frame.grid_propagate(False)
        self.settings_frame.place(x=0, y=0)
        for i in range(20):
            self.settings_frame.rowconfigure(i, weight=5) if i == 18 else self.settings_frame.rowconfigure(i, weight=1)

        self.settings_frame.columnconfigure(0, weight=1)
        self.settings_frame.columnconfigure(1, weight=1)

   
      

        # SETTINGS

        self.settings_title_label = ttk.Label(self.settings_frame, text="BUSINESS SETTINGS", justify="center", font=("Arial", 34))
        self.settings_title_label.grid(row=0, column=0, columnspan=2)
        
        
        # BUSINESS NAME SETTING
        self.business_name_label = ttk.Label(self.settings_frame, text="Business Name")
        self.business_name_entry = ttk.Entry(self.settings_frame)
        self.business_name_label.grid(row=1, column=0, sticky="e",padx=20)
        self.business_name_entry.grid(row=1, column=1, sticky="w")

        self.update_name_button = ttk.Button(self.settings_frame, text="Update Business Name", width=20, command=self.update_name)
        self.update_name_button.grid(row=2, column=0, columnspan=2)

        
        
        # BUSINESS ITEM_SIZE SETTING
        self.current_sizes_label = ttk.Label(self.settings_frame, text="Current Item Sizes:")
        self.current_sizes_listed_label = ttk.Label(self.settings_frame, text=BUSINESS.item_sizes)
        self.current_sizes_label.grid(row=3,column=0, sticky="e",padx=20)
        self.current_sizes_listed_label.grid(row=3,column=1, sticky="w")
    

        
        self.add_remove_size_option = ttk.Combobox(self.settings_frame, values=["Add Size", "Remove Size"], width=10)
        self.add_remove_size_entry = ttk.Entry(self.settings_frame)
        self.add_remove_size_option.grid(row=4,column=0, sticky="e",padx=20)
        self.add_remove_size_entry.grid(row=4,column=1, sticky="w")

        self.update_sizes_button = ttk.Button(self.settings_frame, text="Update Sizes", width=20, command=self.update_sizes)
        self.update_sizes_button.grid(row=5, column=0, columnspan=2)
        
        # BUSINESS EXPENSE_CATS SETTING
        self.current_expense_categories_label = ttk.Label(self.settings_frame, text="Current Expense Categories:")
        self.current_expense_categories_listed_label = ttk.Label(self.settings_frame, text=BUSINESS.expense_categories)
        self.current_expense_categories_label.grid(row=6,column=0, sticky="e",padx=20)
        self.current_expense_categories_listed_label.grid(row=6,column=1, sticky="w")

        
        self.add_remove_expense_category_option = ttk.Combobox(self.settings_frame, values=["Add Exp. Category", "Remove Exp. Category"], width=15)
        self.add_remove_expense_category_entry = ttk.Entry(self.settings_frame)
        self.add_remove_expense_category_option.grid(row=7,column=0, sticky="e",padx=20)
        self.add_remove_expense_category_entry.grid(row=7,column=1, sticky="w")

        self.update_expense_categories_button = ttk.Button(self.settings_frame, text="Update Expense Categories", width=20, command=self.update_expense_categories)
        self.update_expense_categories_button.grid(row=8, column=0, columnspan=2)
        
        
        # BUSINESS EXPENSE_METHODS SETTING
        self.current_expense_methods_label = ttk.Label(self.settings_frame, text="Current Expense Methods:")
        self.current_expense_methods_listed_label = ttk.Label(self.settings_frame, text=BUSINESS.expense_methods)
        self.current_expense_methods_label.grid(row=9,column=0, sticky="e",padx=20)
        self.current_expense_methods_listed_label.grid(row=9,column=1, sticky="w")

        self.add_remove_expense_method_option = ttk.Combobox(self.settings_frame, values=["Add Exp. Method", "Remove Exp. Method"], width=15)
        self.add_remove_expense_method_entry = ttk.Entry(self.settings_frame)
        self.add_remove_expense_method_option.grid(row=10,column=0, sticky="e",padx=20)
        self.add_remove_expense_method_entry.grid(row=10,column=1, sticky="w")

        
        self.update_expense_methods_button = ttk.Button(self.settings_frame, text="Update Expense Methods", width=20, command=self.update_expense_methods)
        self.update_expense_methods_button.grid(row=11, column=0, columnspan=2)
        
        # TRANSACTIONS SALE_PLATFORM SETTINGS
        self.current_sale_platforms_label = ttk.Label(self.settings_frame, text="Current Sale Platforms:")
        self.current_sale_platforms_listed_label = ttk.Label(self.settings_frame, text=BUSINESS.sale_platforms)
        self.current_sale_platforms_label.grid(row=12,column=0, sticky="e",padx=20)
        self.current_sale_platforms_listed_label.grid(row=12,column=1,sticky="w")

        
        self.add_remove_sale_platform_option = ttk.Combobox(self.settings_frame, values=["Add Sale Platform", "Remove Sale Platform"], width=16)
        self.add_remove_sale_platform_entry = ttk.Entry(self.settings_frame)
        self.add_remove_sale_platform_option.grid(row=13,column=0, sticky="e",padx=20)
        self.add_remove_sale_platform_entry.grid(row=13,column=1, sticky="w")

        self.update_sale_platforms_button = ttk.Button(self.settings_frame, text="Update Sale Platforms", width=20, command=self.update_sale_platforms)
        self.update_sale_platforms_button.grid(row=14, column=0, columnspan=2)
        
        # TRANSACTIONS TRANS_METHODS SETTINGS
        self.current_transportation_methods_label = ttk.Label(self.settings_frame, text="Current Sale Transp. Methods:")
        self.current_transportation_methods_listed_label = ttk.Label(self.settings_frame, text=BUSINESS.transportation_methods)
        self.current_transportation_methods_label.grid(row=15,column=0, sticky="e",padx=20)
        self.current_transportation_methods_listed_label.grid(row=15,column=1, sticky="w")

        
        self.add_remove_transportation_method_option = ttk.Combobox(self.settings_frame, values=["Add Transp. Method", "Remove Transp. Method"], width=17)
        self.add_remove_transportation_method_entry = ttk.Entry(self.settings_frame)
        self.add_remove_transportation_method_option.grid(row=16,column=0, sticky="e",padx=20)
        self.add_remove_transportation_method_entry.grid(row=16,column=1, sticky="w")

        
        self.update_transportation_methods_button = ttk.Button(self.settings_frame, text="Update Sale Transp. Methods", width=20, command=self.update_transportation_methods)
        self.update_transportation_methods_button.grid(row=17, column=0, columnspan=2)
        
      
        
       
        self.settings_status_label = ttk.Label(self.settings_frame, text="Status: None")
        self.settings_status_label.grid(row=18, column=0, columnspan=2)
        

        
    def update_name(self):

        # get the entries for the update name setting
        
        new_business_name = self.business_name_entry.get()

        if new_business_name == "":
            self.settings_status_label.config(text="Status: Name Update Failed, Blank Entry!")
            return False
        if not new_business_name.replace(" ", "").isalnum():
            self.settings_status_label.config(text="Status: Name Update Failed, Business Name Alpha-numerical Only!")
            return False
        if not len(new_business_name) <= 25:         
            self.settings_status_label.config(text="Status: Name Update Failed, Business Name Must Be <25 Characters!")
            return False
        else:
            self.BUSINESS.name = new_business_name
            self.app.title(f"Small Business Manager: {new_business_name}")
            self.settings_status_label.config(text="Status: Success, Business Name Updated!")
            self.BUSINESS.save_business()
            return True
            
    def update_sizes(self):

        add_or_remove_option = self.add_remove_size_option.get()
        
        new_size = self.add_remove_size_entry.get()

        if add_or_remove_option == "" or new_size == "":
            self.settings_status_label.config(text=f"Status: Size Update Failed, Blank Entry!")
            return False

        new_size = new_size.upper()


        match add_or_remove_option:

            case "Add Size":
                try:
                    if new_size in self.BUSINESS.item_sizes:
                        raise ValueError("Size Already Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                
                self.BUSINESS.item_sizes.append(new_size)

            case "Remove Size":
                try:
                    if new_size not in self.BUSINESS.item_sizes:
                        raise ValueError("Size Doesn't Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                self.BUSINESS.item_sizes.remove(new_size)
            case _:
                self.settings_status_label.config(text=f"Status: Size Update Failed, Invalid Update Option!")
                return False
            
        self.BUSINESS.save_business()
        self.current_sizes_listed_label.config(text=self.BUSINESS.item_sizes)
        self.inventory_tab.item_size_entry.config(values=self.BUSINESS.item_sizes)
        self.settings_status_label.config(text=f"Status: {add_or_remove_option} '{new_size}' Update Success!")
        return True
    
    def update_expense_categories(self):

        add_or_remove_option = self.add_remove_expense_category_option.get()
        
        new_expense_category = self.add_remove_expense_category_entry.get()

        if add_or_remove_option == "" or new_expense_category == "":
            self.settings_status_label.config(text=f"Status: Exp. Category Update Failed, Blank Entry!")
            return False

        new_expense_category = new_expense_category.lower()


        match add_or_remove_option:

            case "Add Exp. Category":
                try:
                    if new_expense_category in self.BUSINESS.expense_categories:
                        raise ValueError("Exp. Category Already Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                
                self.BUSINESS.expense_categories.append(new_expense_category)

            case "Remove Exp. Category":
                try:
                    if new_expense_category not in self.BUSINESS.expense_categories:
                        raise ValueError("Exp. Category Doesn't Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                self.BUSINESS.expense_categories.remove(new_expense_category)
            case _:
                self.settings_status_label.config(text=f"Status: Exp. Cateogory Update Failed, Invalid Update Option!")
                return False
            
        self.BUSINESS.save_business()
        self.current_expense_categories_listed_label.config(text=self.BUSINESS.expense_categories)
        self.expense_tab.category.config(values=self.BUSINESS.expense_categories)
        self.settings_status_label.config(text=f"Status: {add_or_remove_option} '{new_expense_category}' Update Success!")
        return True
    
    def update_expense_methods(self):

        add_or_remove_option = self.add_remove_expense_method_option.get()
        
        new_expense_method = self.add_remove_expense_method_entry.get()

        if add_or_remove_option == "" or new_expense_method == "":
            self.settings_status_label.config(text=f"Status: Exp. Method Update Failed, Blank Entry!")
            return False

        new_expense_method = new_expense_method.lower()


        match add_or_remove_option:

            case "Add Exp. Method":
                try:
                    if new_expense_method in self.BUSINESS.expense_methods:
                        raise ValueError("Exp. Method Already Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                
                self.BUSINESS.expense_methods.append(new_expense_method)

            case "Remove Exp. Method":
                try:
                    if new_expense_method not in self.BUSINESS.expense_methods:
                        raise ValueError("Exp. Method Doesn't Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                self.BUSINESS.expense_methods.remove(new_expense_method)
            case _:
                self.settings_status_label.config(text=f"Status: Exp. Method Update Failed, Invalid Update Option!")
                return False
            
        self.BUSINESS.save_business()
        self.current_expense_methods_listed_label.config(text=self.BUSINESS.expense_methods)
        self.expense_tab.method.config(values=self.BUSINESS.expense_methods)
        self.settings_status_label.config(text=f"Status: {add_or_remove_option} '{new_expense_method}' Update Success!")
        return True
    
    
    
    def update_sale_platforms(self):

        add_or_remove_option = self.add_remove_sale_platform_option.get()
        
        new_sale_platform = self.add_remove_sale_platform_entry.get()

        if add_or_remove_option == "" or new_sale_platform == "":
            self.settings_status_label.config(text=f"Status: Sale Platform Update Failed, Blank Entry!")
            return False

        new_sale_platform = new_sale_platform.lower()


        match add_or_remove_option:

            case "Add Sale Platform":
                try:
                    if new_sale_platform in self.BUSINESS.sale_platforms:
                        raise ValueError("Sale Platform Already Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                
                self.BUSINESS.sale_platforms.append(new_sale_platform)

            case "Remove Sale Platform":
                try:
                    if new_sale_platform not in self.BUSINESS.sale_platforms:
                        raise ValueError("Sale Platform Doesn't Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                self.BUSINESS.sale_platforms.remove(new_sale_platform)
            case _:
                self.settings_status_label.config(text=f"Status: Sale Platform Update Failed, Invalid Update Option!")
                return False
            
        self.BUSINESS.save_business()
        self.current_sale_platforms_listed_label.config(text=self.BUSINESS.sale_platforms)
        self.transactions_tab.platform.config(values=self.BUSINESS.sale_platforms)
        self.settings_status_label.config(text=f"Status: {add_or_remove_option} '{new_sale_platform}' Update Success!")
        return True
    
    def update_transportation_methods(self):

        add_or_remove_option = self.add_remove_transportation_method_option.get()
        
        new_transportation_method = self.add_remove_transportation_method_entry.get()

        if add_or_remove_option == "" or new_transportation_method == "":
            self.settings_status_label.config(text=f"Status: Transp. Method Update Failed, Blank Entry!")
            return False

        new_transportation_method = new_transportation_method.lower()


        match add_or_remove_option:

            case "Add Transp. Method":
                try:
                    if new_transportation_method in self.BUSINESS.transportation_methods:
                        raise ValueError("Transp. Method Already Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                
                self.BUSINESS.transportation_methods.append(new_transportation_method)

            case "Remove Transp. Method":
                try:
                    if new_transportation_method not in self.BUSINESS.transportation_methods:
                        raise ValueError("Transp. Method Doesn't Exists")
                except ValueError as e:
                    self.settings_status_label.config(text=f"Status: {add_or_remove_option} Update Failed, {e}!")
                    return False
                self.BUSINESS.transportation_methods.remove(new_transportation_method)
            case _:
                self.settings_status_label.config(text=f"Status: Transp. Method Update Failed, Invalid Update Option!")
                return False
            
        self.BUSINESS.save_business()
        self.current_transportation_methods_listed_label.config(text=self.BUSINESS.transportation_methods)
        self.transactions_tab.transport_method.config(values=self.BUSINESS.transportation_methods)
        self.settings_status_label.config(text=f"Status: {add_or_remove_option} '{new_transportation_method}' Update Success!")
        return True
    







        

         


  
       

    