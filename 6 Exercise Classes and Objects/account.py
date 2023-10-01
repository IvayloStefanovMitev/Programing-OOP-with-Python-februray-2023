class Account:

    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> (str, int):
        if amount > self.balance:
            return "Amount exceeded balance"
        self.balance -= amount
        return self.balance

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())