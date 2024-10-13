"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    monthly_incomes = []  
    total_months = int(input("Enter the number of months: "))

    while total_months <= 0:
        print("Number of months must be positive.")
        total_months = int(input("Enter the number of months: "))

    for month_index in range(1, total_months + 1):
        income = float(input(f"Income for month {month_index}: "))  
        monthly_incomes.append(income)

    display_income_report(monthly_incomes)  


def display_income_report(incomes):  
    print("\nIncome Summary\n--------------")
    cumulative_total = 0
    for month_index, monthly_income in enumerate(incomes, start=1):
        cumulative_total += monthly_income
        print(f"Month {month_index:2} - Income: ${monthly_income:10.2f} | "
              f"Cumulative Total: ${cumulative_total:10.2f}")

main()
