class FinancialEntryDTO():
    def __init__(self, id: int, userName:str, categoryID: int, amount: int, targetAmount: int, title: str):
        self.id = id
        self.userName = userName
        self.categoryID = categoryID
        self.amount = amount
        self.target_amount = targetAmount
        self.title =  title