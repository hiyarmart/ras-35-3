class SavingAccount:
    pass
class CheckingAccount:
   pass
class Bound:
    pass
class Stock:
    pass
class RealEstate:
    pass
class Security(Stock, Bound):
    pass
class BankAccount(SavingAccount, CheckingAccount):
    pass
class InterestBearingItem(Security, BankAccount):
    pass
class Insurableltem(BankAccount, RealEstate):
    pass
class Asset(Security, BankAccount, RealEstate):
    pass





