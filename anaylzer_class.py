
from mortgage import *


class Analyzer():
    """
    This class is used to crete a new analysis of a rental
    property. This class will calculate all metrics to be used
    to analyze a property.
    """

    def __init__(self, price, interest_rate, rent, loan_duration, down_payment):
        self.down_payment = down_payment
        self.price = price
        self.interest_rate = interest_rate
        self.rent = rent
        self.loan_duration = loan_duration
        self.mortgage = Loan(principal=price, interest=float(interest_rate/100), term=loan_duration).monthly_payment
        self.cash_flow = 0

    def get_monthly(self):
        return self.mortgage

    def set_cash_flow(self, expenses):
        self.cash_flow = self.rent - (self.mortgage + expenses)

    def get_cash_flow(self):
        return self.cash_flow

    def get_roi(self):
        roi = ((self.cash_flow * 12)/self.down_payment) * 100
        return roi



