from tracker.repo import TrackerRepo
from tracker.dto import CategoryDTO, FinancialEntryDTO

class TrackerService:
    repo = TrackerRepo()
    
    def addCategory(self, category: CategoryDTO):
        self.repo.addCategory(category=category)

    def addFinancialEntry(self, financialEntry: FinancialEntryDTO):
        try:
            self.repo.addFinancialEntry(financialEntry=financialEntry)
        except Exception as e:
            raise e

    def getAllCategories(self):
        try:
            categories = self.repo.getAllCategories()
            categoryDTOs = []

            for category in categories:
                dtoCategory = CategoryDTO(
                    id=category.id,
                    name=category.name,
                    type=category.type
                )
                categoryDTOs.append(dtoCategory)
            
            return categoryDTOs
        except Exception as e:
            raise e

    def getFinancialEntryByCategoryID(self, categoryID: int):
        try:
            entries = self.repo.getFinancialEntryByCategory(categoryID=categoryID)
            entryDTOs = []

            for entry in entries:
                dtoEntry = FinancialEntryDTO(
                    id=entry.id,
                    userName=entry.user_name,
                    categoryID=entry.category.id,
                    amount=entry.amount,
                    targetAmount=entry.target_amount,
                    title=entry.title
                )

                entryDTOs.append(dtoEntry)

            return entryDTOs
        except Exception as e: 
            raise e

    def getTotalTargetAmount(self):
        return self.repo.getTotalTargetAmount()

    def getTotalAmount(self):
        return self.repo.getTotalAmount()

    def changeTargetAmount(self, financialEntryID: int, newAmount: int):
        try:
            self.repo.changeTargetAmount(financialEntryID=financialEntryID, newAmount=newAmount)
        except Exception as e:
            raise e

    def changeAmount(self, financialEntryID: int, newAmount: int):
        try:
            self.repo.changeAmount(financialEntryID=financialEntryID, newAmount=newAmount)
        except Exception as e:
            raise e