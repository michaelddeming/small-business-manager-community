# Small Business Manager v1.0 by Michael Deming

## Purpose

The purpose for this project is to ease the technicality behind running a small business. Many entrepreneurs or creatives are focused on growing the company through marketing and branding, meanwhile leaving gaps in book-keeping and accounting. 

This project by no means reinvents the wheel as a business management program, but provides a simplistic and effective interface for experienced AND inexperienced business owners alike. 


- Some features include:
    - Inventory Management and Individual Itemization
    - Expense Management Tracking
    - Customizable Sales Tracking, Both Sales and Returns
    - Automated Annual Income Statements and Balance Sheets
    - Customizable Business Attributes for Detailed Tracking/Statistics

## Getting Started

### Demo Video

- DEMO: https://www.youtube.com/watch?v=SHd532_LNY8&t=1s

### Requirements

- `Python 3.13`
    - No external packages are required. This project uses the following built-in Python libraries:
        1. `tkinter`
        2. `datetime`
        3. `JSON`
        4. `sqlite3`

### Database Sync

- Copy the filepath for the `sbm.db` file found within the `small_business_manager` project directory. 
- Paste the `sbm.db` filepath as the **variable value** for the variable `FILEPATH` found within the `FILEPATH.env` file inside the `app` directory.

### Workflow

- The `Small Business Manager` consists of a `tkinter` GUI with **6 primary tabs** or interfaces for user interactions:
    1. **Inventory**
        - Log individual inventory items within the "Add Item" frame by assigning them the following attributes or bits of information related to said item:
            - Item Date
            - Item Description
            - Item Size (Customizable per Settings)
            - Item Cost (Cost of Good)
        - Valid items, not duplicate or incomplete, are logged into the inventory table via a `sqlite3` database and displayed in the treeview matrix within the tab.
        - Search for logged items within the database via the "Search Item" frame. Found items are displayed to the matrix treeview upon a successful search. Refresh treeview matrix to reset display state.
    2. **Expenses**
        - Log individual expenses within the "Add Expense" frame by assigning them the following attributes or bits of information related to said expense:
            - Exp. Date
            - Exp. Description
            - Exp. Cost 
            - Exp. Category (Type of expense)
            - Exp. Method (How was expense purchased?)
            - Exp. Note (Optional)
        - Valid expenses, not duplicate or incomplete, are logged into the expenses table via a `sqlite3` database and displayed in the treeview matrix within the tab.
        - Search for logged expenses within the database via the "Search Expense" frame. Found expenses are displayed to the matrix treeview upon a successful search. Refresh treeview matrix to reset display state.
    3. **Transactions**
        - Log sales and returns of valid inventory items within the "Commit Transaction" frame by assigning them the following attributes or bits of information related to said transaction:
            - For "Sale" Transaction Type:
                1. Transaction Date
                2. Item ID (ID of Item to be sold)
                3. Item Amount (Sticker price item sold for)
                4. Sale Platform (where item sold, customizable in settings)
                5. Transportation Method (How customer received their item)
                6. Transportation Charge (Charge given to customer for transporting sale)
                7. Fee (NOT APPLIED TO CUSTOMER! Optional "fee" for cost of doing business on Transaction like platform fees etc. reducing income)
                8. Discount (Cost savings for customer)
                9. Note (Optional)
            - For "Return" Transaction Type:
                1. Transaction Date
                2. Item ID (ID of item to be returned)
                3. Item Amount (Total Return Price)
                **NOTE**: "Return" type transactions only require Transaction Date, Item ID, and Item Amount (Return Total). All other entry options remain blank for a valid return to be committed.  
        - Valid transactions, not duplicate or incomplete, are logged into the transactions table via a `sqlite3` database and displayed in the treeview matrix within the tab.
        - Search for logged transactions within the database via the "Search Transaction" frame. Found transactions are displayed to the matrix treeview upon a successful search. Refresh treeview matrix to reset display state.
    4. **Income Statement**
        - Transactions and expenses, logged under equal calendar periods are grouped and analyzed automatically. An Income Statement is then generated for that calendar period. 
        
        - An Income Statement generates the following information:
            1. Year (Calendar period)
            2. Gross Sales (Sum of invoice total of "Sale" type transactions within calendar period)
            3. Sales Transport (Sum of "Transportation Charge" from "Sale" type transactions within calendar period)
            4. Allowances (Sum of invoice total of "Return" type transactions within calendar period)
            5. Fees (Sum of "Fee" from "Sale" type transactions within calendar period, NOT additional charges to customer)
            6. Discounts (Sum of "Discount" from "Sale" type transactions within calendar period)
            7. Net Sales (Gross Sales + Sales Transport - Allowances - Fees - Discounts within calendar period)
            8. Cost of Goods Sold (Sum of "cost" of items, when acquired/logged into inventory, for "Sale" type transactions within calendar period)
            9. Gross Margin (Net Sales - Cost of Goods Sold)
            10. Expenses (Sum of expenses "cost" within calendar period)
            11. Net Income (Gross Margin - Expenses)
    5. **Balance Sheet**
        - The Balance Sheet generates the following:
            1. Unsold Inventory Asset-values ("cost" of items, when acquired/logged into inventory) within the calendar period are summed and reported.
    6. **Settings**
        - Business owners can tailor their business attributes by customizing the following features:
            1. Business Name
            2. Sizing (Add or remove item sizing options)
            3. Exp. Categories (Add or remove expense categories)
            4. Exp. Methods (Add or remove expense methods)
            5. Sale Platforms (Add or remove sale platforms)
            6. Sale Transp. Methods (Add or remove sale transport methods)

## Community Version

I plan to launch a Community Edition of this project as a separate repository. This version will be open to contributions from my YouTube and Twitch subscribers, as well as members of the Discord server.

The goal is to encourage collaboration in an open-source format — whether you’re learning, contributing features, fixing bugs, or just exploring how it all works.