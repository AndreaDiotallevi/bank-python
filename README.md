[![Build Status](https://travis-ci.com/AndreaDiotallevi/bank-python.svg?branch=master)](https://travis-ci.com/AndreaDiotallevi/bank-python) [![Test Coverage](https://api.codeclimate.com/v1/badges/65678327fbf59b19d876/test_coverage)](https://codeclimate.com/github/AndreaDiotallevi/bank-python/test_coverage)

# Bank Tech Test

[Description](#description) | [Requirements](#requirements) | [Acceptance Criteria](#acceptance-criteria) | [User Stories](#user-stories) | [Domain Models](#domain-models) | [Design Approach](#design-approach) | [Code Structure](#code-structure) | [Technologies Used](#technologies-used) | [Getting Started](#getting-started) | [How to Run the Tests](#how-to-run-the-tests) | [How to Run the App](#how-to-run-the-app) | [Feature Test](#feature-test)

## Description

A python implementation of the bank tech test, which shows object-oriented programming principles and decoupled test suites.

## Requirements

* You should be able to interact with your code via a REPL like IRB or the JavaScript console.  (You don't need to implement a command line interface that takes input from STDIN)
* Deposits, withdrawal
* Account statement (date, amount, balance) printing
* Data can be kept in memory (it doesn't need to be stored to a database or anything)

## Acceptance Criteria

**Given** a client makes a deposit of 1000 on 10-01-2012  
**And** a deposit of 2000 on 13-01-2012  
**And** a withdrawal of 500 on 14-01-2012  
**When** she prints her bank statement  
**Then** she would see

```
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```
                  
## User Stories

```
As a bank user
So that I can store some money
I want to be able to make a deposit to my account
```

```
As a bank user
So that I can use some of my stored money
I want to be able to make a withdrawal from my account
```

```
As a bank user
So that I know when I am running out of money
I want to see an error message when I try to withdraw more money than the actual balance
```

```
As a bank user
So that I can see all the history of my transactions in reverse chronological order
I want to be able to see my overall account statement
```

## Domain Models

| ACCOUNT         | STATEMENT               | TRANSACTION
| --------------- | ----------------------- | ---------------
| self.balance    | self.transactions       | self.credit
| self.statement  | self.transaction_class  | self.debit
|                 |                         | self.balance
|                 |                         |
| print_statement | add_transaction         | format
| deposit         | format_transactions     | format_date
| withdraw        |                         | format_decimals

## Design Approach

The program has three classes and each of them has a clear responsibility:

- **ACCOUNT**: takes care of the account behaviours, like keeping track of the overall balance, deposit on the account, withdraw from the account and print the overall statement. A statement instance variable is dependency injected into the account class, to allow the transaction history and formatting responsibilities to be carried out by the statement class.

- **STATEMENT**: takes care of the transactions history and formatting of all transactions into a printable statement. The transaction class is dependency injected into the statement class, to allow the creation of a new transaction at each deposit and withdrawal.

- **TRANSACTION**: takes care of the single transaction properties and their formatting.

## Code Structure

The code is structured into two main folders:
- The ```src``` folder, which includes the code
- The ```tests``` folder, which includes the tests. This folder is also divided into two folders:
  - The ```features``` folder, which includes the feature tests
  - The ```units``` folder, which includes the unit tests

## Technologies Used

* ```python``` for the code
* ```pytest``` for testing
* ```pytest-cov``` for test coverage

## Getting Started

* Clone the repository
* Change into the new repository
* Create a virtual environment named ```env``` with ```python3 -m venv env```
* Activate it with ```source env/bin/activate```
* Install the requirements with ```pip install -r requirements/dev.txt```

## How To Run The Tests

To run the tests type ```pytest```

## How to Run the App

* Open the python REPL with ```python3```
* Require the model files with:
  - ```from src.account import Account```
  - ```from src.statement import Statement```
  - ```from src.transaction import Transaction```

## Feature Test

```
$ python3
>>> from src.account import Account
>>> from src.statement import Statement
>>> from src.transaction import Transaction
>>> account = Account()
>>> account.print_statement()
date || credit || debit || balance
>>> account.withdraw(500)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/andrea/Code/python/bank-python/src/account.py", line 18, in withdraw
    raise NotEnoughMoney("You don't have enough money in the account!")
src.account.NotEnoughMoney: You don't have enough money in the account!
>>> account.deposit(1000)
1000
>>> account.print_statement()
date || credit || debit || balance
03/06/2020 || 1000.00 || || 1000.00
>>> account.deposit(2000)
3000
>>> account.print_statement()
date || credit || debit || balance
03/06/2020 || 2000.00 || || 3000.00
03/06/2020 || 1000.00 || || 1000.00
>>> account.withdraw(500)
2500
>>> account.print_statement()
date || credit || debit || balance
03/06/2020 || || 500.00 || 2500.00
03/06/2020 || 2000.00 || || 3000.00
03/06/2020 || 1000.00 || || 1000.00
>>> 
```
