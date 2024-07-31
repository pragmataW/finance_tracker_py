from tracker.models import Category, FinancialEntry
from tracker.dto import CategoryDTO, FinancialEntryDTO
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

class TrackerRepo:
    def addCategory(category: CategoryDTO):
        Category.objects.create(name=category.name, type=category.type)

    def addFinancialEntry(financialEntry: FinancialEntryDTO):
        try:
            FinancialEntry.objects.create(
                    user_name=financialEntry.userName,
                    category=Category.objects.get(id=financialEntry.categoryID),
                    amount=financialEntry.amount,
                    target_amount=financialEntry.target_amount,
                    title=financialEntry.title
                )
        except ObjectDoesNotExist:
            raise ValueError(f"Category with id {financialEntry.categoryID} does not exist.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while creating financial entry: {str(e)}")

    def getAllCategories():
        allCatagories = Category.objects.all()
        return allCatagories

    def getFinancialEntryByCategory(categoryID: int):
        try:
            category = Category.objects.get(id=categoryID)
            entries = FinancialEntry.objects.filter(category=category)
            return entries
        except ObjectDoesNotExist:
            raise ValueError(f"Category with id {categoryID} does not exist.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching financial entries: {str(e)}")

    def getTotalTargetAmount():
        total = FinancialEntry.objects.aggregate(Sum('target_amount'))['target_amount__sum']
        if total is not None:
            return total
        return 0

    def getTotalAmount():
        total = FinancialEntry.objects.aggregate(Sum('amount'))['amount__sum']
        if total is not None:
            return total
        return 0

    def changeTargetAmount(financialEntryID: int, newAmount):
        try:
            entry = FinancialEntry.objects.get(id=financialEntryID)
            entry.target_amount = newAmount
            entry.save(update_fields=['target_amount'])
        except ObjectDoesNotExist:
            raise ValueError(f"FinancialEntry with id {financialEntryID} does not exist.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while updating the entry: {str(e)}")

    def changeAmount(financialEntryID: int, newAmount):
        try:
            entry = FinancialEntry.objects.get(id=financialEntryID)
            entry.amount = newAmount
            entry.save(update_fields=['amount'])
        except ObjectDoesNotExist:
            raise ValueError(f"FinancialEntry with id {financialEntryID} does not exist.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while updating the entry: {str(e)}")
