
def main():
    OverallBudget = 1000
    selection = 0
    while selection != 5:
        print(' 1 = Add on Expense')
        print(' 2 = Subtract the Expense')
        print(' 3 = Add on Revenue')
        print(' 4 = Subtract Revenue')
        print(' 5 = End')

        selection = int(input())

        if selection == 1:
            OverallBudget = addition_of_expense(OverallBudget)
        elif selection == 2:
            OverallBudget = subtraction_of_expense(OverallBudget)
        elif selection == 3:
            OverallBudget = add_on_revenue(OverallBudget)
        elif selection == 4:
            OverallBudget = subtract_revenue(OverallBudget)
        elif selection == 5:
            print('Thank you')
        else:
            print('Wrong entry. Please choose an option 1-5. ')

#Function Definitions

def addition_of_expense(OverallBudget):
    billing = int(input('Please enter the expense amount: '))
    many_bill = int(input('Enter how many times this expense occurs per month: '))
    complete_bill = billing * many_bill
    OverallBudget = OverallBudget - complete_bill
    check_on_budget(OverallBudget)
    return OverallBudget

def subtraction_of_expense(OverallBudget):
    reverse_bill = int(input('Enter the amount to be subtracted: '))
    if reverse_bill <= OverallBudget:
        OverallBudget = OverallBudget + reverse_bill
        check_on_budget(OverallBudget)
    else:
        print('Please check the amount entered.')
        return OverallBudget


def add_on_revenue(OverallBudget):
    income = int(input('Enter the amount of income over the starting $1,000 to add: '))
    many_income = int(input('Enter how many times this income occurs per month: '))
    total_income = income * many_income
    OverallBudget = OverallBudget + total_income
    check_on_budget(OverallBudget)
    return OverallBudget

def subtract_revenue(OverallBudget):
    income_loss = int(input('Enter the amount your income was reduced: '))
    OverallBudget = OverallBudget - income_loss
    check_on_budget(OverallBudget)
    return OverallBudget

def check_on_budget(OverallBudget):
    if OverallBudget >= 0:
        print(f"The overall remaining budget is {OverallBudget}.")
    else:
        print(f"You have exceeded the monthly budget. \n Re-evaluate your expenses and balance the budget. \n"
              f"Calculate based on {OverallBudget}.")


print('Please make a selection from the following:')
main()