class Transaction:

    def __init__(self, id, date, transaction_type, item_id):
        self.id = id
        self.date = date
        transaction_types = ("for-sale", "sold")
        if transaction_type not in transaction_types:
            raise ValueError(
                f"Error: {transaction_type} must be in {transaction_types}"
            )
        else:
            self.transaction_type = transaction_type
        self.item_id = item_id
