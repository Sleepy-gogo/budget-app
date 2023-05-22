class Category:

	def __init__(self, name):
		self.name = name
		self.balance = 0
		self.ledger = []

	def update_balance(self, value):
		self.balance += value

	def update_ledger(self, ammount, description):
		transaction = {
			"ammount" : ammount,
			"description" : description
		}

		self.ledger.append(transaction)

	def deposit(self, ammount, description = ""):
		self.update_balance(ammount)
		self.update_ledger(ammount, description)

	def withdraw(self, ammount, description = ""):

		if ammount > self.balance:
			return False

		self.update_balance(-ammount)
		self.update_ledger(-ammount, description)

		return True

		







def create_spend_chart(categories):