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
    * 
    * 
* budgetStatistics function:
  * parameter: an array storing all categories objects
  * 
  * error handling:
* budgetPlots function:
  * parameter: an array storing all categories objects
  * 
  * error handling:
* record.txt: (`file writing`)
  * at the start of the program: open a new record.txt file or over write 
## Getting started
### Prerequisites
* Python 3: `3.10.1` for author
* install NumPy:  `pip install numpy`
* install Matplotlib: `pip install matplotlib`
* install tabulate: `pip install tabulate`
### Executing program
* download `budget_calc.py` and open it in a Python IDE (Visual Studio Code for author)
* run the program
## Usage
Example of usage:
> a
## Author
LKY Michelle<br>
Link of project: https://github.com/LKYMichelle/Python-Project-Budget-Calculator.git
## License
This project is licensed under the MIT License - see the `LICENSE` file for details
