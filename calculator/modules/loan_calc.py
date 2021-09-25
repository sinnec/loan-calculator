'''This modules calculates the maximum number of loans Lender can administer based on a specific budget and plan'''

'''Each loan administered is handled as a seperate object from Loan class'''
class Loan:
    loan_list = []
    def __init__(self, loan_class, loan_amount, plan_duration):
        self.loan_class = loan_class
        self.loan_amount = loan_amount
        self.plan_duration = plan_duration
        self.remaining_debt = loan_amount
        self.monthly_installment = int(loan_amount / plan_duration)
        Loan.loan_list.append(self) # Each object created is added in the list automatically
        
    def pay_installment(self):
        self.remaining_debt -= self.monthly_installment

'''This function accepts 2 arguments, an integer which is the budget provided by the user and a plan object which is derived from
    the plans database in Django and contains all the class plan data.
    Each plan object has the id, class_name, available_plans, amount and months attributes'''
def loan_calculator(budget, plan_obj):
    total_loans = 0
    loan_amount = plan_obj.amount
    loan_installment = int(plan_obj.amount / plan_obj.months)
        
    if budget < loan_amount: # If the budget is less than the loan amount, the function terminates returning 0.
        return total_loans
    for i in range(1, 7): # repeat for 6 times (months)
        loans_this_month = 0
        if budget >= loan_amount:
            loans_this_month = budget // loan_amount # Amount of loans that can be given using floor division
            if len(Loan.loan_list) + loans_this_month > plan_obj.available_plans: # if the given loans and new loans that can be given are more than the available plans
                loans_this_month = plan_obj.available_plans - len(Loan.loan_list) # only the remaining to the available amount plans are given (if any)
            for j in range(loans_this_month): # Creates as many plan objects as administered this month
                Loan(plan_obj.class_name, loan_amount, plan_obj.months)
            total_loans += loans_this_month
            budget -= loan_amount * loans_this_month
        for loan in list(Loan.loan_list): # For all active loans
            budget += loan_installment # Add installment to budget
            loan.pay_installment() # and reduce remaining debt
            if loan.remaining_debt == 0: #remove paid loans
                Loan.loan_list.remove(loan) 
            
        #print(f"Month {i}, Total loans given: {loans_given}, Budget: {budget}, New loans: {loans_this_month} Active loans: {len(Loan.loan_list)}")
    Loan.loan_list.clear() # Clear the list for a new query
    return total_loans