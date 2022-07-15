# Python Project: Budget Calculator
My first Python project from draft and design to coding and README: take in initial budgets of 6 major categories and let the user to deposit, withdraw, check current statistics and generate cuurent plots.
## Table of contents
* [Description](#description)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Author](#author)
* [License](#license)
## Description
* Implement a `Budget class` to store category's name, balance, total amount of deposition and withdrawal by updating them with functions deposit and withdraw.
* Main: 
	* 1. ask for user's initial budget of each category (Food, Clothing, Accessory or Makeup, Entertainment, Transport, and Others) and create `Budget object` for each category and store them in an array
  * 2. ask for the next step user want to do by typing choice number (Deposition and Withdraw / Check Statistics / Generate Plots / Quit)
  * 3. call functions respectively and repeat to ask for next step or end the program if user choose to quit
* depositAndWithdraw function:
  * parameter: an array storing all categories objects
  * 1. ask for the next step user want to do by typing choice number (Deposition / Withdrawal / Exit)
  * 2. ask for the catetegory and the amount user want to deposit or withdraw if they choose to
  * 3. repeatedly asking user untill user choose to exit
  * error handling:
    * user can only type 1 / 2 / 3 to choose from Deposition / Withdrawal / Exit
    * user can only type 1 / 2 / 3 / 4 / 5 / 6 to choose from Food / Clothing / Accessory or Makeup / Entertainment / Transportation / Others
    * user can only type in a positive number for the amount they want to deposit or withdraw
    * user can only type in a number smaller than the current balance of category they want to withdraw from
* budgetStatistics function:
  * parameter: an array storing all categories objects
  * 1. print balance of each category, and calculate and print total, `mean, maximum and minimum` balance of all categories
  * 2. print cumulative deposition of each category, and calculate and print total, `mean, maximum and minimum` deposition of all categories
  * 3. print cumulative withdrawal of each category, and calculate and print total, `mean, maximum and minimum` withdrawal of all categories
  * 4. use `tabulate` module to print out the percentage of balance, deposition and withdrawal of each category out the the overall statistics
  * error handling:
     * if total balance or deposition or withdrawal is equal to 0, then keep passing the respective zero array to tabulate
* budgetPlots function: (`matplotlib`)
  * parameter: an array storing all categories objects
  * 1. generate a `bar chart` with comparison between current balance, deposition and withdrawal of each category
  * 2. generate 3 `subplots` in one window
    * 1st subplot: `pie chart` showing the percentage of balance of each category out the the overall statistics
    * 2nd subplot: `pie chart` showing the percentage of deposition of each category out the the overall statistics
    * 3rd subplot: `pie chart` showing the percentage of withdrawal of each category out the the overall statistics
  * error handling:
    * if total balance or deposition or withdrawal is equal to 0, keep the respective array zero
    * if total balance or deposition or withdrawal is not equal to 100, empty plot generated for respective subplot(s)
* record.txt: (`file writing`)
  * at the start of the program: open a new record.txt file or overwrite if record.txt already exists
  * write in the amount and category user deposit or withdraw from, and write in the current balance of that category every time 
  * at the end of the program: write in the balance summary of each category and also the overall balance
## Getting started
### Prerequisites
* Python 3: `3.10.1` for author
* install NumPy:  `pip install numpy`
* install Matplotlib: `pip install matplotlib`
* install tabulate: `pip install tabulate`
### Executing program
* download `budget_calc.py` and open it in a Python IDE (Visual Studio Code for author)
* run the program and follow the instructions
## Usage
Example of usage:    
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/1.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/2.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/3.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/Figure_1.png))
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/Figure_2.png))
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/4.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/5.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/6.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/7.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/8.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/Figure_3.png))
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/Figure_4.png))
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/9.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/10.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/11.png)
> ![image](https://github.com/LKYMichelle/Python-Project-Budget-Calculator/blob/main/12.png)
## Author
LKY Michelle<br>
Link of project: https://github.com/LKYMichelle/Python-Project-Budget-Calculator.git
## License
This project is licensed under the MIT License - see the `LICENSE` file for details
