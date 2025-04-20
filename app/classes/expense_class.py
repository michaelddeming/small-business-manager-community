
class Expense:

    def __init__(self, id:int, date:str, description:str, cost:int, category:str, method:str, note:str=None):

        self.id = id
        self.date = date
        self.description = description
        self.cost = cost
        self.category = category
        self.method = method
        self.note = note

        