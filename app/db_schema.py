import platform
from pathlib import Path
import sqlite3


def get_database_path():
    """Get the path to create the database based on the OS"""
    app_name = "small_business_manager"

    system = platform.system()
    if system == "Windows":
        data_dir = Path.home() / "AppData" / "Roaming" / app_name
    elif system == "Darwin":
        data_dir = Path.home() / "Library" / "Application Support" / app_name
    else:
        # Linux distros
        data_dir = Path.home() / ".local" / "share" / app_name

    data_dir.mkdir(exist_ok=True)
    db_path = Path(data_dir / "sbm.db")
    db_path.touch(exist_ok=True)  # Creating .db file at path

    return db_path

#
# def database_initialization():
#     db_path = get_database_path()
#
#     conn = sqlite3.connect()
#     db = conn.cursor()
#
"""INVENTORY TABLE"""
# db.execute("""CREATE TABLE inventory (

#         id INTEGER PRIMARY KEY,
#         date_purchased TIMESTAMP,
#         description TEXT,
#         size TEXT,
#         cost INTEGER,
#         status TEXT
#         )
# """)

# """EXPENSES TABLE"""
# db.execute("""CREATE TABLE expenses (

#         id INTEGER PRIMARY KEY,
#         date TIMESTAMP,
#         description TEXT,
#         cost INTEGER,
#         category TEXT,
#         method TEXT,
#         note TEXT
#         )
# """)

# """TRANSACTIONS TABLE"""
# db.execute(
#     """CREATE TABLE transactions (

#         id INTEGER PRIMARY KEY,
#         type TEXT,
#         date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         item_id INTEGER,
#         item_amount INTEGER,
#         sale_platform TEXT,
#         transportation TEXT,
#         transportation_charge INTEGER,
#         fee INTEGER,
#         discount INTEGER,
#         transaction_total INTEGER GENERATED ALWAYS AS (item_amount + transportation_charge - fee - discount),
#         note TEXT,
#         FOREIGN KEY (item_id) REFERENCES inventory(id)
#         )
# """
# )

# db.execute("""CREATE TABLE income_statement (

#         year INTEGER PRIMARY KEY,
#         gross_sales INTEGER NOT NULL,
#         sales_transport INTEGER DEFAULT 0,
#         allowances INTEGER DEFAULT 0,
#         fees INTEGER DEFAULT 0,
#         discounts INTEGER DEFAULT 0,
#         net_sales INTEGER GENERATED ALWAYS AS (gross_sales + sales_transport - allowances - fees - discounts) STORED,
#         cost_of_goods_sold INTEGER NOT NULL,
#         gross_margin INTEGER GENERATED ALWAYS AS (net_sales - cost_of_goods_sold) STORED,
#         expenses INTEGER DEFAULT 0,
#         net_income INTEGER GENERATED ALWAYS AS (gross_margin - expenses) STORED
#         )
#         """)

# BALANCE SHEET
# db.execute("""CREATE TABLE balance_sheet (

#         year INTEGER PRIMARY KEY,
#         unsold_inventory INTEGER NOT NULL
#         )
#         """)

# REMOVE DATA in TABLES
# db.execute("DELETE FROM inventory")
# db.execute("DELETE FROM expenses")
# db.execute("DELETE FROM transactions")
# db.execute("DELETE FROM income_statement")
# db.execute("DELETE FROM balance_sheet")

conn.commit()


# all_inventory = db.execute("SELECT * FROM inventory").fetchall()
# print(all_inventory)


# test_item = Item(1, "2025-03-18", "test_item", "M", 10)

# db.execute("INSERT INTO inventory (date_purchased, description, size, cost, status) VALUES (?,?,?,?,?)", (test_item.date_purchased, test_item.item_desc, test_item.item_size, test_item.item_cost, test_item.status))

# db.execute("SELECT * FROM inventory")
# conn.commit()


# def table_stuff(table_name: str):
#     conn = sqlite3.connect("/Users/michaeldeming/repos/small_business_manager/sbm.db")
#     db = conn.cursor()
#     return db.execute(f"SELECT * FROM {table_name}").fetchall()


# print(table_stuff("inventory"))
