your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())
print(your_total_expenses)
print(partner_total_expenses)
if your_total_expenses > partner_total_expenses:
    print("You spent more than your partner.")
else:
    print("Your partner spent more than you.")
    print("Difference:", your_expenses["Hotel"] - partner_expenses["Hotel"])

