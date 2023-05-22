class Category:

	def __init__(self, name):
		self.name = name
		self.ledger = []


	def update_ledger(self, amount, description):
		transaction = {
			"amount" : amount,
			"description" : description
		}

		self.ledger.append(transaction)


	def get_balance(self):
		balance = 0
		for transaction in self.ledger:
			balance += transaction["amount"]
		return balance


	def check_funds(self, amount):
		balance = self.get_balance()

		if amount > balance:
			return False

		return True


	def deposit(self, amount, description = ""):
		self.update_ledger(amount, description)


	def withdraw(self, amount, description = ""):

		if not self.check_funds(amount):
			return False

		self.update_ledger(-amount, description)

		return True

	
	def transfer(self, amount, category):
		success = self.withdraw(amount, f"Transfer to {category.name}")

		if not success:
			return False

		category.deposit(amount, f"Transfer from {self.name}")

		return True


	def __str__(self):
		title_diff = 30 - len(self.name)
		string = "*" * int(title_diff / 2) + self.name + "*" * int(title_diff / 2) + "\n"

		for transaction in self.ledger:
			amount = "{:.2f}".format(transaction["amount"])
			description = transaction["description"]

			margin = 29 - len(amount)
			spaces = 30 - len(description[:margin]) - len(amount)

			string += description[:margin] + (" " * spaces) + amount + "\n"

		string += f"Total: " + "{:.2f}".format(self.get_balance())

		return string


def create_spend_chart(categories):
	return ""