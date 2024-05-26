from experta import *
import csv
import numpy as np

csv_file = "transactions.csv"

transactions = []

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row['Amount'] = float(row['Amount'])  # Convertir el monto a un número
        transactions.append(row)

class Transaction(Fact):
    def __str__(self):
        return "Transaction(AccountNumber={}, Amount={})".format(self['account_number'],self['amount'])

class History(Fact):
    pass

class FraudDetector(KnowledgeEngine):

    """
    Hallamos si hay un fraude en la transacción
    con respecto a la historia de transacciones
    y un monto de transacción dado.
    """
    @Rule(AS.tr << Transaction(),
          AS.h << History(transactions=MATCH.transactions))
    def fraud_amount(self, tr, h):

        mounts = [t['Amount'] for t in h['transactions']]
        mean = np.mean(mounts)
        d_std = np.std(mounts)
        max_amount = mean + 3 * d_std
        min_amount = mean - 3 * d_std

        if tr['amount'] > max_amount or tr['amount'] < min_amount:
            print("Fraud detected based on amount in transaction: ", tr)
        else:
            print("Transaction is not fraud based on amount: ", tr)
    
    """
    Hallamos si hay un fraude en la transacción
    con respecto
    a la historia de transacciones y la ciudad de la transacción.
    """
    @Rule(AS.tr << Transaction(),
        AS.h << History(transactions=MATCH.transactions))
    def fraud_city(self, tr, h):
        cities = [t['City'] for t in h['transactions']]
        if tr['city'] not in cities:
            print("Fraud detected based on city in transaction: ", tr)
        else:
            print("Transaction is not fraud based on city: ", tr)
    
    """
    Hallamos si hay un fraude en la transacción
    con respecto
    a la historia de transacciones y la hora de la transacción.
    """
    @Rule(AS.tr << Transaction(),
    AS.h << History(transactions=MATCH.transactions))
    def fraud_time(self, tr, h):
        times = [t['Time'] for t in h['transactions']]
        # Convertir las horas a minutos para comparar
        def time_to_minutes(time_str):
            hours, minutes, _ = map(int, time_str.split(':'))
            return hours * 60 + minutes

        transaction_minutes = time_to_minutes(tr['time'])
        transaction_times_in_minutes = [time_to_minutes(t) for t in times]

        mean_time = np.mean(transaction_times_in_minutes)
        d_std_time = np.std(transaction_times_in_minutes)
        max_time = mean_time + 3 * d_std_time
        min_time = mean_time - 3 * d_std_time

        if transaction_minutes > max_time or transaction_minutes < min_time:
            print("Fraud detected based on time in transaction: ", tr)
        else:
            print("Transaction is not fraud based on time: ", tr)



engine = FraudDetector()
engine.reset()
user_transactions = [transaction for transaction in transactions if transaction['AccountNumber'] == "1001"]
engine.declare(History(transactions=user_transactions))
engine.declare(Transaction(amount=1000, account_number="1001", city="Lima", time="24:00:00"))
engine.run()
