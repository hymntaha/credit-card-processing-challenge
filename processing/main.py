from utils.collection import CreditRecordsCollection
from utils.data import get_data, format_data

if __name__ == '__main__':

    data = get_data()
    accounts, transactions = format_data(data=data)

    credit_data = CreditRecordsCollection(accounts=accounts)
    credit_data.process(transactions=transactions)

    print(credit_data)
