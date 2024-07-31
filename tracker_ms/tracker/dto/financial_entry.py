class FinancialEntryDTO():
    def __init__(self, userName:str, categoryID: int, amount: int, targetAmount: int, title: int):
        self.userName = userName
        self.categoryID = categoryID
        self.amount = amount
        self.target_amount = targetAmount
        self.title =  title