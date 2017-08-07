# Credit Card Processing Challenge

This exercise is to build a simple payment processor for an imaginary provider.
This program will add new accounts, process the transactions, and display
account summaries.

### Instructions

Assignment completed in Python 3.5.1, Python>=3.3 acceptable

No dependencies required 

```
# From root folder (cd /path/to/braintree-creditcard-processing/)

# Run tests
python3 ./tests/test_main.py

# Run program with filename as arg
python3 ./processing/main.py input.txt

# Run program from STDIN
python3 ./processing/main.py < input.txt
```

### Exercise Questions

*data.py*
- `get_data()` Program reads data from file or STDIN 
- `format_data()` Individual row from data are stored in an accounts or
transactions queue as named tuples which are great lightweight ways of 
storing records. A queue was used to keep records in order and free
memory after use.

*collections.py*
- I created `CreditRecordsCollection` as a class so I could create
accounts on initialization and process transactions later, it also 
acts as a thin-wrapper over an `OrderedDict` so I could keep records
arranged alphabetically but still have quick lookup access.

*luhn.py*
- Function is broken up into 3 functions for easy testability

#### Why I picked python

- Python is the language that I have used the most over this last year
- It's easy to build things quickly
- It's beautiful easy for anybody to understand the thought process

### Comments

- Transactions should be uniquely identified by card number instead of 
account holder name