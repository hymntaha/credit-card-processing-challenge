from collections import namedtuple, deque
import sys

from utils.luhn import is_luhn_valid

Account = namedtuple('Accounts',
                     ['name',
                      'account_number',
                      'limit',
                      'amount',
                      'verified'])

Transaction = namedtuple('Transactions',
                         ['type',
                          'name',
                          'amount'])


def get_data():
    try:
        # Open content from file passed as arg
        file_name = sys.argv[1]
        with open(file_name) as f:
            content = f.read()

    except IndexError:
        # Pass content in STDIN
        content = sys.stdin.read()

    return content


def format_data(data,
                accounts=deque(),
                transactions=deque()):
    for line in data.splitlines():
        line = line.split(' ')

        if line[0] == 'Add':
            accounts.append(Account(
                name=line[1],
                account_number=line[2],
                limit=int(line[3][1:]),
                amount=0,
                verified=is_luhn_valid(line[2])))

        else:
            transactions.append(Transaction(
                type=line[0],
                name=line[1],
                amount=int(line[2][1:])))

    return accounts, transactions
