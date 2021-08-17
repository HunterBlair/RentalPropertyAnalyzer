

from anaylzer_class import Analyzer

analyze = Analyzer(price=250000, interest_rate=.035, rent=1400, loan_duration=30, down_payment=30000)

mortgage = analyze.get_monthly()

print(analyze.set_cash_flow(500))
print(analyze.get_roi())
print(3.5/100)
print(mortgage)