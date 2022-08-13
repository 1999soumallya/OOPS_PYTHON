class Bank:
    cash=100000000
    @classmethod
    def avalable_cash(cls):
        print(cls.cash)
class AlahabadBank(Bank):
    pass
class Statebank(Bank):
    cash=200000000
    @classmethod
    def avalable_cash(cls):
        print(cls.cash)
        print(cls.cash+Bank.cash)
a=AlahabadBank()
a.avalable_cash()
s=Statebank()
s.avalable_cash()

'''class Bank:
    #avalable_cash=10000000
    def __init__(self,avalable_cash=0) -> None:
        self.avalable_cash=avalable_cash
    def display_cash(self):
        print(self.avalable_cash)
class Alahabadbank(Bank):
    pass
class Statebank(Bank):
    def __init__(self,avalable_cash,avalable_cash1=0) -> None:
        super().__init__(avalable_cash)
        self.avalable_cash1=avalable_cash1
    def display_cash(self):
        super().display_cash()
        print(self.avalable_cash+self.avalable_cash1)


a=Alahabadbank()
a.display_cash()
s=Statebank(10000000+20000000)
s.display_cash()'''