class Item:

    def __init__(
        self,
        item_number: int,
        date_purchased: str,
        item_desc: str,
        item_size: str,
        item_cost: int,
    ):

        # REQUIRED ATTR TO MAKE AN ITEM
        self.item_number = item_number  # a unique number for every Item
        self.date_purchased = date_purchased  # date the Item was purchased
        self.item_desc = item_desc  # short description/name of the Item
        self.item_size = item_size  # the size of the Item
        self.item_cost = item_cost  # the cost of the Item (cost of good)

        # SET ITEM STATUS TO INVENTORY
        self.status = "inventory"  # status of the Item

    def mark_for_sale(self):
        if self.status == "for-sale":
            raise ValueError("ERROR: Item is already ForSale.")
        elif self.status == "sold":
            raise ValueError("ERROR: Item is already Sold.")
        self.status = "for-sale"

    def mark_sold(self):
        if self.status == "inventory":
            raise ValueError("ERROR: Item is not listed ForSale.")
        if self.status == "sold":
            raise ValueError("ERROR: Item is already Sold.")
        self.status = "sold"


class ForSaleItem:

    def __init__(self, item: Item, listing_price: int, date_listed: str):

        # REQUIRED ATTR TO MAKE A ForSaleItem
        self.item = item
        self.listing_price = listing_price  # price the Item was listed for
        self.date_listed = date_listed  # date the Item was listed on

        # SET ITEM STATUS FOR-SALE
        self.item.mark_for_sale()


class SoldItem:

    def __init__(self, for_sale_item: ForSaleItem, sold_price: int, date_sold: str):

        # REQUIRED ATTR TO MAKE A SoldItem
        self.for_sale_item = for_sale_item
        self.sold_price = sold_price  # price the Item was sold for
        self.date_sold = date_sold  # date the Item was sold on

        # SET ITEM STATUS SOLD
        self.for_sale_item.item.mark_sold()
