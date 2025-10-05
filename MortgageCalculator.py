#PART ONE --> ASSIGNMENT ONE --> MORTGAGE PAYMENTS --> SHON VAKSMAN 

#Print objective of the code
print ("----- Mortgage Payment Calculator -----")
print ("   ")

#Design a class to calculate a variety of payment methods
class MortgagePayment:

    #Design method for the quoted (semiannual) interest rate and amortized period 
    def __init__(self, semiCompoundRates, amortPeriod):

        #Store the semiannual compounded rates and the number of amortized years
        self.__semiCompoundRates = semiCompoundRates
        self.__amortPeriod = amortPeriod

    #Design method to calculate the periodic interest rate for a given number of payments 
    def periodicIR (self, annualPayments):

        #Convert interest rate with semi-annual compounding to the Effective Annual Rate 
            # Formula --> EAR = (1 + i/n)^n -1
            # "n" is 2 (semi annually occur twice) to calculate the interest rate
        semiMonthlyPeriod = 2 
        EAR = (1 + self.__semiCompoundRates/semiMonthlyPeriod) ** semiMonthlyPeriod - 1

        #Convert EAR into the Periodic Interest Rate for each payment type 
            # Formula --> r = (1+ APR/m)^m/f -1)
            # APR/m is equal to the EAR; m is equal to one year (to divide payments throughout the year); f is equal to annualPayments
        return (1 + EAR) ** (1/annualPayments) - 1

    #Design method to calcuate payment amount (given principal and payment period)
    def calcPMT (self, principalAmount, annualPayments):

        #Calculate periodic interest rate based on the payment frequency 
        rate = self.periodicIR(annualPayments)

        #Calculate total number of payments over the full amortiziation period
        numOfPayments = annualPayments * self.__amortPeriod

        #Calculate payment required based on the interest and time period
            #Rearrange the Present Value of Annuity Factor formula to isolate and solve for PMT 
        return principalAmount * rate/(1-(1+rate) ** (-numOfPayments))

    #Design method to calculate the payment for all six payment periods
    def payments (self, principalAmount):

        #Calculate the mortgage payment amount 
        monthly = self.calcPMT(principalAmount, 12)
        semiMonthly = self.calcPMT(principalAmount, 24)
        biWeekly = self.calcPMT(principalAmount, 26)
        weekly = self.calcPMT(principalAmount, 52)

        #BiWeekly occurs twice a month, while Weekly occurs four times a month
        biWeek = 2
        perMonth = 4
        
        accelBiweekly = monthly /biWeek
        accelWeekly = monthly /perMonth 
   
    #Return a tuple for all six payment options, rounded to 2 decimals
        twoDecimals = 2

        return (
        "{:.2f}".format(monthly),
        "{:.2f}".format(semiMonthly),
        "{:.2f}".format(biWeekly),
        "{:.2f}".format(weekly),
        "{:.2f}".format(accelBiweekly),
        "{:.2f}".format(accelWeekly)
        )
 
#Prompt the user to enter the mortgage principal, quoted interest rate (%), and amortization period of mortgage (in years)  
principalAmount = float((input("Enter Mortgage Principal (e.g., 80,000): ")))
semiCompoundRates = float((input ("Enter Quoted Annual Interest Rate % (e.g., 4.2): ")))
amortPeriod = int((input ("Enter Amortization In # of Years (e.g., 20): ")))

#Calculate the quoted interest and amoritzed period for the inputed answers (convert interest rate into decimal)
convertPercent = 100.0
calcIR_AP = MortgagePayment(semiCompoundRates / convertPercent, amortPeriod)

#Returning the tuple --> take the principal amount and calculate for payment options
monthly, semiMonthly, biWeekly, weekly, accelBiweekly, accelWeekly = calcIR_AP.payments(principalAmount)

#Print the values for all six payment options
print ("")
print ("PAYMENT AMOUNTS:")
print ("")
print ("Monthly Payment: $" + monthly)
print ("Semi-monthly Payment: $" + semiMonthly)
print ("Bi-weekly Payment: $" + biWeekly)
print ("Weekly Payment: $" + weekly)
print ("Rapid Bi-weekly Payment: $" + accelBiweekly)
print ("Rapid Weekly Payment: $" + accelWeekly)