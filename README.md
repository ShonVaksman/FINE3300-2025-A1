# FINE3300-2025-A1
The purpose of the following code is to create a class that will calculate mortgage payments for Canadian fixed-rate mortgages and to create a class that reads currency exchange data and converts currencies interchangeably between CAD and USD. 

Part One: Calculating mortgage payments (based on user inputs) for various time periods such as the following:
    Monthly --> (12/yr)
    Semi-monthly --> twice per month for a total of (24/yr)
    Bi-weekly --> every two weeks for a total of (26/yr)
    Rapid bi-weekly --> half of paid monthly mortgage payment every two weeks for a total of (26/yr)
    Weekly --> (52/yr)
    Rapid weekly --> mortgage paid every week for a total of (52/year)

Once you will input the principal amount, quoted annual interest rate, and number of amortized years, the amounts due will be calculated and appear on the screen (for all six payment types). 

SAMPLE OUTPUT for a principal amount of $100,000, quoted at 5.5%, and amortized over 25 years:
shonvaksman@Shons-MacBook-Air FINE3300-2025-A1 % /usr/local/bin/python3 /Users/shonvaksman/FINE3300-2025-A1/Mortgage.py
----- Mortgage Payment Calculator -----

*INPUT*   
Enter Mortgage Principal (e.g., 80,000): 100000
Enter Quoted Annual Interest Rate % (e.g., 4.2): 5.5
Enter Amortization In # of Years (e.g., 20): 25

*OUTPUT*
PAYMENT AMOUNTS:

Monthly Payment: $610.39
Semi-monthly Payment: $304.85
Bi-weekly Payment: $281.38
Weekly Payment: $140.61
Rapid Bi-weekly Payment: $305.20
Rapid Weekly Payment: $152.60


Part Two: Converting ($) from one currency to another using given exchange rates. In this code, the focus is on the conversion of the USD dollar and CAD dollar. You will be able to convert any principal between these two currencies. If the currency typed in is not either USD or CAD, a message will appear stating that the currency is unrecognized and will return the same principal amount that you entered.

SAMPLE OUTPUT for an amount of $100,000 from USD to CAD
/usr/local/bin/python3 /Users/shonvaksman/FINE3300-2025-A1/ExchangeRates.py
shonvaksman@Shons-MacBook-Air FINE3300-2025-A1 % /usr/local/bin/python3 /Users/shonvaksman/FINE3300-2025-A1/ExchangeRates.py
----- Exchange Rate Converter -----

*INPUT*
Conversion Amount ($): 100000
From Currency (e.g., USD): USD
To Currency (e.g., CAD): CAD

*OUTPUT*
The Converted Amount Is (USD-->CAD): $136,980.00


SAMPLE OUTPUT for an amount of $100,000 from CAD to USD
shonvaksman@Shons-MacBook-Air FINE3300-2025-A1 % /usr/local/bin/python3 /Users/shonvaksman/FINE3300-2025-A1/ExchangeRates.py
----- Exchange Rate Converter -----

*INPUT*
Conversion Amount ($): 100000
From Currency (e.g., USD): CAD
To Currency (e.g., CAD): USD

*OUTPUT*
The Converted Amount Is (CAD-->USD): $73,003.36
    
