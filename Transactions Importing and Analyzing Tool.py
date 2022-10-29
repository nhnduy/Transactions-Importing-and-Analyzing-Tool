import csv, os

#Create the main function for the tool
def app():
    repeat = "yes"
    print("Welcome to the Adrek Robotics transaction tracker!")
    #Create a function to open and read any csv file
    def import_file(csv_file):
        with open(csv_file, "r") as file:
            trans_count = 0
            file_reader = csv.reader(file)
            list1 = []
            #Append all rows in the transactions' file to a list.
            for line in file_reader:
                list1.append(line)
            #If the ledger file isn't created, create a new file and write all values in list1 to it    
            if is_file == "no":
                with open("transaction_ledger.csv", "w") as new_file:
                    new_file_writer = csv.writer(new_file, lineterminator = "\n")
                    for i in range(0, len(list1)):
                        new_file_writer.writerow(list1[i])
                        trans_count += 1
                    
            else:
                #Open the ledger file to see if values are in the list, if yes, then remove them from the list, and skip the count.
                with open("transaction_ledger.csv", "r") as ledger_file:
                    ledger_file_reader = csv.reader(ledger_file)
                    for line in ledger_file_reader:
                        if line in list1:
                            list1.remove(line)
                            trans_count += 0
                            print("Data ID", line[0], "is already loaded")
                #Append the rest of list to the ledger file            
                with open("transaction_ledger.csv", "a") as ledger_file:
                    ledger_file_writer = csv.writer(ledger_file, lineterminator = "\n")
                    for j in range(0, len(list1)):
                        ledger_file_writer.writerow(list1[j])
                        trans_count += 1 
                        
            print(trans_count,"transaction records successfully loaded.")
    #Create this function to analyze the ledger file        
    def statistics_file(csv_file):
        trans_count = 0
        pending_status = "PENDING"
        pending_money = []
        if is_file == "no":
            print("Sorry, no transaction data was loaded yet. Please try again.")
        #if yes, then open it with read, count the columns, check if status is pending, if pending, append and sum the money
        else:
            with open("transaction_ledger.csv", "r") as ledger_file:
                new_file_reader = csv.reader(ledger_file)
                for line in new_file_reader:
                    trans_count += 1
                    money = line[3]
                    if line [4] == pending_status:
                        #print these lines below for clearer presentation if needed.
                        #print("Money for the pending transactions is/are:", money)
                        pending_money.append(money)
                        #Convert the strings of money into float
                        final_pending_money = [float(i) for i in pending_money]
                print("Number of current transactions:", trans_count)
                print("Total amount pending:", sum(final_pending_money))
                
    while repeat.lower().strip() == "yes":

        ask = input("What would you like to perform (import/statistics)? ")
        
        #Check if transaction_ledger.csv exists
        if os.path.exists("transaction_ledger.csv"):
            is_file = "yes"
        else:
            is_file = "no"
        #Call the functions above, also handle errors if the wanted file does not exist    
        if ask.lower().strip() == "import":
            try:
                ask2 = input("Which file would you like to import? ")
                import_file(ask2)
            except:
                print("Sorry, that file could not be found. Please try again.")
        
        elif ask.lower().strip() == "statistics":
            statistics_file("transaction_ledger.csv")
        
        else:
            print("The requested analysis is not supported. Please try again")
        
        repeat = input("Would you like to run any further analyses (yes/no)? ")
app()