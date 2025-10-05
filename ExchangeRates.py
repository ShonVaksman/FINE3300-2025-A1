#PART TWO --> ASSIGNMENT ONE --> EXCHANGE RATE CALCULATOR --> SHON VAKSMAN 

#Import the BankOfCanadaExchangeRates data file
import csv

#Print the objective of the code
print ("----- Exchange Rate Converter -----")
print ("")

#Design a class for exchange rates
class ExchangeRates:

    #Design a constructor for the exchange rate file 
    def __init__(self, bocRates):

        #Store the exchange rates inside the object
        self.__bocRATES = bocRates

        #Create an empty dictionary for the exchange rates (store key-value pairs)
        self.__exchangeRatesDict = {}

        #Function that will open, read and call specific information from the CSV file (prompted by the user) 
        self.__loadLatestRow()

    #Design a method to load the latest exchange rates
    def __loadLatestRow(self):

        #Open the Bank of Canada Exchange Rates File
        fileCSV = open (self.__bocRATES)

        #Read each line of the file and store in a list
        reader = csv.reader(fileCSV)
        rows = list (reader)

        #Close the Bank of Canada Exchange Rates File after finished reading
        fileCSV.close()
  
        #Calling the first row of CSV and store in the list (where currency headers are located)
        checkHeader = rows[0]

        #Count the number of rows in the CSV file starting from the most recent exchange rates 
        i = len(rows) -1 

        #Loop that checks every value that is greater or equal to index [1] 
        while i >= 1:

            #Looking at the current row based on the index (position)
            row = rows[i]
            #If the cell has no data --> FALSE; if there is --> TRUE 
            has_data = False
            m = 0

            #Loop that will check every cell in each row of the file to see if any contain data
            while m < len(row):

                #If the cell is not equal to an empty string, there is a value present
                if row[m] != "":
                    has_data = True
                    #Loop stops once a non-empty cell is located
                    break
                m += 1

            #If the current row contains data, the row is saved as the latest valid record and the loop is exited
            if has_data:
                latestDataRow = row
                break
            #If there is no data, continuing check the previous rows
            i -= 1

        #Start reading the file from column 1
        c = 1

        #Loop runs as long as there are columns left to read in the header and latest data row
        while c < len(checkHeader) and c < len(latestDataRow):

            #Obtain the column name at index [j]
            columnN = checkHeader [c]

            #Obtain value from index [j]
            value = latestDataRow [c]

            #If cell is empty, move onto the next index 
            if value !="":

                #If cell obtains data, convert value from a string to a float and store in dictionary
                self.__exchangeRatesDict[columnN] = float(value) 
            else:
                pass

            #The loop moves onto the next coloumn 
            c += 1

    #Design a method for the amount to convert, the starting currency, and the ending currency
    def convert (self, amount, from_currency, to_currency):

        #Convert the users input to uppercase letters
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        #Obtain USD/CAD rate from dictionary
        rate = self.__exchangeRatesDict ["USD/CAD"]

        #Convert the amount inputted by user to a float (to include decimals if necessary)
        userAmt = float (amount)

        #CASE 1: If the currency is equal to one another, return the same amount, rounded to 2 decimals
        if from_currency == to_currency:
            return round(userAmt, 2)

        #CASE 2: If the currency is converted from USD to CAD, return CAD, rounded to 2 decimals
        if from_currency == "USD" and to_currency == "CAD":
            return round (userAmt * rate, 2)
        
        #CASE 3: If the currency is converted from CAD to USD, return USD, rounded to 2 decimals
        elif from_currency == "CAD" and to_currency == "USD":
            return round (userAmt/rate, 2)
        
        #CASE 4: If the currency is neither USD or CAD, return an ERROR message
        else:
            print ("")
            print ("!!!! Error: Unable to Complete Conversion from " + from_currency + " to " + to_currency + " !!!!")
            return round(userAmt,2)

#Locate exchange rate information
path = "bocRATES.csv"

#Prompt the user on the conversion amount, current currency, and desired currency conversion
amount = input("Conversion Amount ($): ")
fromCCY= input("From Currency (e.g., USD): ")
toCCY = input("To Currency (e.g., CAD): ")

#Create object to pass the file path into the class
create = ExchangeRates(path)

#Return converted amount
conversion = create.convert(amount, fromCCY, toCCY)

#Print converted amount
print ("")
print ("The Converted Amount Is (" + fromCCY.upper() + "-->" + toCCY.upper() +  "): " + "${:,.2f}".format(conversion))