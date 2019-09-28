class bank:
    balance=50000
    def __init__(self,acc_no=None,acc_type=None,cash_amount=None,cheque_no=None,
                cheque_amount=None,dd_no=None,dd_amount=None):
        
        if acc_no!=None and acc_type!=None and cash_amount!=None:
            bank.balance+=cash_amount
            print("After adding cash amount your main balance is :",bank.balance)
        elif acc_no!=None and acc_type!=None and cheque_no!=None and cheque_amount!=None:
            bank.balance+=cheque_amount
            print("After adding cheque amount your main balance is :",bank.balance)
        elif acc_no!=None and acc_type!=None and dd_no!=None and dd_amount!=None:
            bank.balance+=dd_amount
            print("After adding dd amount your main balance is :",bank.balance)
        else:
            print("Please enter a valid input")
         

bank(acc_no=11223344556677,acc_type='saving',cash_amount=2000000)
bank(acc_no=11223344556677,acc_type='saving',cheque_no='CH1122',cheque_amount=4000000)
bank(acc_no=11223344556677,acc_type='saving',dd_no='DD1122',dd_amount=5000000)
bank(acc_no=11223344556677,acc_type='saving')
           

