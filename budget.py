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


def get_expenses(categories):
	expenses = []

	for category in categories:
		expense = 0
		for transaction in category.ledger:
			if transaction["amount"] < 0:
				expense -= transaction["amount"]
		expenses.append(expense)
	return expenses


def get_percentages(categories):
	expenses = get_expenses(categories)
	return [expense / sum(expenses) * 100 for expense in expenses]


def create_spend_chart(categories):
	percentages = get_percentages(categories)

	text = "Percentage spent by category\n"
	for i in range(100, -1, -10):
		number = " " * (3 - len(str(i))) + str(i)
		text += f"{number}| "
		for j in range(len(categories)):
			text += "o  " if percentages[j] >= i else "   "
		text += "\n"

	total_dashes = 1 + len(categories) * 3
	text += "    " + "-" * total_dashes + "\n"

	max_len = max([len(category.name) for category in categories])

	for i in range(max_len):
		text += "     "
		for word in [category.name for category in categories]:
			try:
				text += word[i] + "  "
			except IndexError:
				text += "   "
		text += '\n'

	return text[:-1]