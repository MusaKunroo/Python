# good_credit_downpayment=1000000*(10/100)
# bad_credit_downpayment=1000000*(20/100)
# has_good_credit=False
# if has_good_credit:
#     print("Downpayment required is: $" + str(good_credit_downpayment))
#  #!  OR print(f"Downpayment required is: {good_credit_downpayment}")
# else:
#     print("Dowpayment required is: $" + str(bad_credit_downpayment))
#     #!  OR print(f"Downpayment required is: {bad_credit_downpayment}")

                 #TODO_Way more Efficient Way_
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")
