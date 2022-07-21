import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec

# Budget class: store and update each category's name, balance, depositing and withdrawing amount
class Budget:
    # initialize category's name, balance, total depositing and withdrawing amount
    def __init__(self, name, initialBudget):
        self.balance = initialBudget
        self.name = name
        self.depositTotal = 0
        self.withdrawTotal = 0

    # update balance and total depositing amount base on user's input
    def deposit(self, amount):
        self.balance += amount
        print("Successfully deposited")
        print("Current balance: " + str(self.balance))
        # write details of deposition into record file
        file = open("record.txt", "a")
        file.write("\nDeposition: " + self.name + " -- " + str(amount) + "\nCurrent balance of " + self.name 
        + ": " + str(self.balance))
        file.close()
        self.depositTotal += amount

    # update balance and total withdrawing amount base on user's input
    def withdraw(self, amount):
        if self.balance-amount >= 0:
            self.balance -= amount
            print("Successfully withdrew")
            print("Current balance: " + str(self.balance))
            # write detail of withdrawal into record file
            file = open("record.txt", "a")
            file.write("\nWithdrawal: " + self.name + " -- " + str(amount)+ "\nCurrent balance of " + self.name 
            + ": " + str(self.balance))
            file.close()
            self.withdrawTotal += amount
        # avoid overwithdrawing and print out error message if overwithdraw occurs
        else:
            print("Error: Current balance is not enough to withdraw the amount of budget.")
            print("Unsuccessful withdrawal")
            # write detail of withdrawal into record file
            file = open("record.txt", "a")
            file.write("\nUnsuccessful withdrawal: " + self.name + " -- " + str(amount)+ "\nCurrent balance of " 
            + self.name + ": " + str(self.balance))
            file.close()

# depositAndWithdraw function: ask for the amount that user want to deposit or withdraw from a specific category 
# and update the object
def depositAndWithdraw(categories):
    choice = 0
    # while loop end when user choose 3. exit
    while (choice != 3):
        invalid = True
        # while loop to get valid choice
        while(invalid):
            try:
                choice = int(input("\nPlease choose your next step in the following options(1-3):\n"
                + "  1. Deposition\n  2. Withdrawal\n  3. Exit\nYour choice: "))
                if 0 < choice < 4:
                    invalid = False
                else:
                    print("Error: input must be 1/2/3. Please enter again.") # print error message
            except ValueError:
                print("Error: input must be an integer. Please enter again.") # print error message
        # 1. deposit
        if choice==1:
            invalid = True
            # while loop to get valid choice
            while(invalid):
                try:
                    order = int(input("\nPlease choose the category to deposit(1-6):\n  1. Food\n  2. Clothing" 
                    + "\n  3. Accessory or Makeup\n  4. Entertainment\n  5. Transportation\n  6. Others\nYour choice: "))
                    if 0 < order < 7:
                        invalid = False
                    else:
                        print("Error: input must be 1/2/3/4/5/6. Please enter again.") # print error message
                except ValueError:
                    print("Error: input must be an integer. Please enter again.") # print error message
            invalid = True
            # while loop to get valid choice
            while(invalid):
                try:
                    amount = float(input("Pleased enter amount of deposition: "))
                    if amount >= 0:
                        invalid = False
                    else:
                        print("Error: input must be positive. Please enter again.") # print error message
                except ValueError:
                    print("Error: input must be a float. Please enter again.") # print error message
            category = categories[order-1]
            category.deposit(amount)
        # 2. withdraw
        elif choice==2:
            invalid = True
            # while loop to get valid choice
            while(invalid):
                try:
                    order = int(input("\nPlease choose the category to withdraw(1-6):\n  1. Food\n  2. Clothing\n" 
                    + "  3. Accessory or Makeup\n  4. Entertainment\n  5. Transportation\n  6. Others\nYour choice: "))
                    if 0 < order < 7:
                        invalid = False
                    else:
                        print("Error: input must be 1/2/3/4/5/6. Please enter again.") # print error message
                except ValueError:
                    print("Error: input must be an integer. Please enter again.") # print error message
            invalid = True
            # while loop to get valid choice
            while(invalid):
                try:
                    amount = float(input("Pleased enter amount of withdrawal: "))
                    if amount >= 0:
                        invalid = False
                    else:
                        print("Error: input must be positive. Please enter again.") # print error message
                except ValueError:
                    print("Error: input must be a float. Please enter again.") # print error message
            category = categories[order-1]
            category.withdraw(amount)
        # 3. exit
        else:
            print("You choose to exit. Thanks for depositing and withdrawing with us.")

# budgetStatistics function: print current statistics of each category
def budgetStatistics(categories):
    print("\nThis is your statistics:")

    # print balance of each category and overall balance
    balanceArr = np.array([])
    print("Balance details:")
    totalBalance = 0
    for i in range(np.size(categories)):
        totalBalance += categories[i].balance
        balanceArr = np.append(balanceArr, categories[i].balance)
        print("  " + str(i+1) + ". " + categories[i].name + ": " + str(categories[i].balance))
    print("  total: " + str(totalBalance))
    print("  mean: " + str(np.mean(balanceArr)) + "  max: " + str(np.max(balanceArr)) + "  min: " + str(np.min(balanceArr)))

    # print total deposition of each category and overall deposition
    depositArr = np.array([])
    print("Deposition summary:")
    totalDeposition = 0
    for i in range(np.size(categories)):
        totalDeposition += categories[i].depositTotal
        depositArr = np.append(depositArr, categories[i].depositTotal)
        print("  " + str(i+1) + ". " + categories[i].name + ": " + str(categories[i].depositTotal))
    print("  total: " + str(totalDeposition))
    print("  mean: " + str(np.mean(depositArr)) + "  max: " + str(np.max(depositArr)) + "  min: " + str(np.min(depositArr)))

    # print total withdrawal of each category and overall withdrawal
    withdrawArr = np.array([])
    print("Withdrawal summary:")
    totalWithdrawal = 0
    for i in range(np.size(categories)):
        totalWithdrawal += categories[i].withdrawTotal
        withdrawArr = np.append(withdrawArr, categories[i].withdrawTotal)
        print("  " + str(i+1) + ". " + categories[i].name + ": " + str(categories[i].withdrawTotal))
    print("  total: " + str(totalWithdrawal))
    print("  mean: " + str(np.mean(withdrawArr)) + "  max: " + str(np.max(withdrawArr)) + "  min: " + str(np.min(withdrawArr)))

    # print percentages using table
    if totalBalance > 0:
        balanceArr = balanceArr/totalBalance*100
    if totalDeposition > 0:
        depositArr = depositArr/totalDeposition*100
    if totalWithdrawal >0:
        withdrawArr = withdrawArr/totalWithdrawal*100
    percentages = {'Category':[categories[i].name for i in range(np.size(categories))],'Balance':balanceArr
    , 'Deposition':depositArr, 'Withdrawal':withdrawArr}
    print("Percentages of each Category:")
    print(tabulate(percentages, headers='keys'))
    print("This is the end of the statistics of your budget.")


# budgetPlots function: generate bar chart comparison and pie charts in subplots
def budgetPlots(categories):
    print("\nBar chart and pie charts generated for current statistics.")

    # arrays storing statistics of each category
    balanceArr = np.array([categories[i].balance for i in range(np.size(categories))])
    depositArr = np.array([categories[i].depositTotal for i in range(np.size(categories))])
    withdrawArr = np.array([categories[i].withdrawTotal for i in range(np.size(categories))])

    # bar chart comparison
    fig, ax = plt.subplots()
    index = np.arange(6)
    bar_width = 0.3
    opacity = 0.8
    
    # generate 3 bars of balance, deposition and withdrawal
    rects1 = plt.bar(index, balanceArr, bar_width, alpha=opacity, color='r', label='Balance')
    rects2 = plt.bar(index + bar_width, depositArr, bar_width, alpha=opacity, color='g', label='Total Deposition')
    rects3 = plt.bar(index + bar_width + bar_width, withdrawArr, bar_width, alpha=opacity, color='b', label='Total Withdrawal')
    
    # plot bar chart
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    plt.title('Balance, Deposition and Withdrawal of Each Category')
    plt.xticks(index + bar_width, [categories[i].name for i in range(np.size(categories))])
    ax.tick_params(axis='x', labelsize=6.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Create 2x2 sub plots
    gs = gridspec.GridSpec(2, 2)

    # generate pie charts in subplots
    pl.figure()

    # subplot 1: pie chart of balance
    if np.sum(balanceArr) > 0:
        balanceArr = balanceArr/np.sum(balanceArr)*100
    mylabels = [categories[i].name for i in range(np.size(categories))]
    ax = pl.subplot(gs[0, :]) # row 0, col 0,1
    if np.sum(balanceArr) > 0:
        plt.pie(balanceArr, labels = mylabels, autopct='%1.1f%%', startangle = 90)
    plt.title("Balance percentage")

    # subplot 2: pie chart of deposition
    if np.sum(depositArr) > 0:
        depositArr = depositArr/np.sum(depositArr)*100
    mylabels = [categories[i].name for i in range(np.size(categories))]
    ax = pl.subplot(gs[1, 0]) # row 1, col 0
    if np.sum(depositArr) > 0:
        plt.pie(depositArr, labels = mylabels, autopct='%1.1f%%', startangle = 90)
    plt.title("Deposition percentage")

    # subplot 3: pie chart of withdrawal
    if np.sum(withdrawArr) > 0:
        withdrawArr = withdrawArr/np.sum(withdrawArr)*100
    mylabels = [categories[i].name for i in range(np.size(categories))]
    ax = pl.subplot(gs[1, 1]) # row 1, col 1
    if np.sum(withdrawArr) > 0:
        plt.pie(withdrawArr, labels = mylabels, autopct='%1.1f%%', startangle = 90)
    plt.title("Withdrawal percentage")

    plt.show()

# initialBudget function to ask for the initial budget from user and return the amount
def initialBudget(order, category):
    invalid = True
    # while loop to get valid amount of budget
    while(invalid):
        try:
            budget = float(input(order + ". Pleased enter your budget for " + category+ ": "))
            if budget >= 0:
                invalid = False
            else:
                print("Error: input must be positive. Please enter again.") # print error message
        except ValueError:
            print("Error: input must be a float. Please enter again.") # print error message
    
    # write the initial budget into record file
    file = open("record.txt", "a")
    file.write("Initial budget: " + category + " -- " + str(budget) + "\n")
    file.close()
    return budget

# main script
def main():
    categories = np.array([])

    # start a new record file
    file = open("record.txt", "w")
    file.write("Start recording\n\n")
    file.close()

    # start the program
    print("Welcome to Budget Calculator!")
    print("There are 6 categories in this Budget Calculator:\n  1. Food\n  2. Clothing\n" 
    + "  3. Accessory or Makeup\n  4. Entertainment\n  5. Transportation\n  6. Others")
    # ask for initial budget of each category, create a Budget object for each and store in an array
    print("For the first step, please enter your initial budgets for these categories respectively.")
    foodBudget = initialBudget('1', 'Food')
    food = Budget('Food', foodBudget)
    categories = np.append(categories, food)
    clothBudget = initialBudget('2', 'Clothing')
    clothing = Budget('Clothing', clothBudget)
    categories = np.append(categories, clothing)
    accessoryBudget = initialBudget('3', 'Accessory or Makeup')
    accessory = Budget('Accessory or Makeup', accessoryBudget)
    categories = np.append(categories, accessory)
    entertainBudget = initialBudget('4', 'Entertainment')
    entertainment = Budget('Entertainment', entertainBudget)
    categories = np.append(categories, entertainment)
    transportBudget = initialBudget('5', 'Transportation')
    transportation = Budget('Transportation', transportBudget)
    categories = np.append(categories, transportation)
    othersBudget = initialBudget('6', 'Others')
    others = Budget('Others', othersBudget)
    categories = np.append(categories, others)
    print("Thank you for entering the initial budgets.")

    # choose to deposit or withdraw, check statistics, generate plots ,or quit
    choice = 0
    # while loop to loop until user choose to quit the programme
    while (choice != 4):
        invalid = True
        # while loop to get valid choice
        while(invalid):
            try:
                choice = int(input("\nPlease choose your next step in the following options(1-4):\n" + 
                "  1. Deposition and Withdrawal\n  2. Check statistics\n  3. Generate plots\n  4. Quit\nYour choice: "))
                if 0 < choice < 5:
                    invalid = False
                else:
                    print("Error: input must be 1/2/3/4. Please enter again.") # print error message
            except ValueError:
                print("Error: input must be an integer. Please enter again.") # print error message
        # deposit and withdraw
        if choice==1:
            depositAndWithdraw(categories)
        # check current statistics
        elif choice==2:
            budgetStatistics(categories)
        # generate plots
        elif choice==3:
            budgetPlots(categories)
        # quit
        else:
            print("You choose to quit.")
            print("Thank you for using Budget Calculator. A record is sent to your account.")
            print("Hope you had a nice user experience!")
            # write summary into record file
            file = open("record.txt", "a")
            file.write("\n\nBalance summary:")
            for i in range(np.size(categories)):
                file.write("\n  " + str(i+1) + ". " + categories[i].name + " -- " + str(categories[i].balance))
            file.write("\n\nThis is the end of the record. Thank you for using Budget Calculator.")
            file.close()

# call main
main()
# print final version of record file
print("\n(Record:")
file = open("record.txt", "r")
print(file.read())
print(")")