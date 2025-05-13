class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.balance = 0
        self.ledger = []
    
    def __str__(self):
        result = f'{self.category_name:*^30}\n'
        total = 0
        
        for item in self.ledger:
            result += f'{item["description"][:23]:23}'
            result += f'{item["amount"]:>7.2f}\n'
            total += item['amount']
        result += f'Total: {total:.2f}'
        
        return result

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self.balance += amount
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(
                amount, 
                f'Transfer to {category.category_name}'
            )
            category.deposit(
                amount, 
                f'Transfer from {self.category_name}'
            )
            return True
        return False


    def check_funds(self, amount):
        return self.balance >= amount

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    category_spendings = []
    total_spent = 0

    for category in categories:
        spending = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spendings.append(spending)
        total_spent += spending

    percentages = [int((spending / total_spent) * 100) // 10 * 10 for spending in category_spendings]

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = max(len(category.category_name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category_name):
                chart += category.category_name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")
food.withdraw(15.89, "restaurant")

clothing = Category("Clothing")
clothing.deposit(1000, "initial deposit")
clothing.withdraw(50.75, "shoes")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(33.40, "movies")

categories = [food, clothing, entertainment]
print(create_spend_chart(categories))