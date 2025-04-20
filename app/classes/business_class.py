import json


class Business:

    def __init__(self, name=None):
        if name:

            self.name = name
        else:
            self.name = "DEFAULT NAME"
        self.expense_categories = ["equipment", "shipping", "delivery"]
        self.expense_methods = ["cash", "credit"]
        self.sale_platforms = ["instagram", "depop"]
        self.transportation_methods = ["shipping", "delivery", "pick-up"]
        self.item_sizes = ["XXS", "XS", "S", "S/M", "M", "M/L", "L", "XL", "XXL"]
        self.years = []

    # CHECK FUNCTIONS

    def check_sale_platform(self, sale_platform: str):

        if sale_platform in self.sale_platforms:
            return sale_platform
        else:
            raise ValueError("Invalid Transaction Platform")

    def check_transportation_method(self, transportation_method):
        if transportation_method in self.transportation_methods:
            return transportation_method
        else:
            raise ValueError("Invalid Transportation Method")

    def read_business(self):
        try:
            with open("business_info.json", "r") as file:
                content = json.load(file)

                for key, value in content.items():
                    match key:
                        case "name":
                            self.name = value
                        case "expense_categories":
                            self.categories = value
                        case "methods":
                            self.expense_methods = value
                        case "platforms":
                            self.sale_platforms = value
                        case "methods":
                            self.transportation_methods = value
                        case "item_sizes":
                            self.item_sizes = value
                        case "years":
                            self.years = value
        except FileNotFoundError:
            with open("business_info.json", "w") as file:
                json.dump({}, file)

    def save_business(self):
        with open("business_info.json", "w") as file:

            json.dump(self.__dict__, file, indent=4)
