# Add csv module to read csv files
import csv

# Add os module to create file path across operating systems
import os

csvpath = os.path.join("Pybank","Resources", "budget_data.csv")

# Open csv file budget_data.csv
with open(csvpath) as csvfile:

    # Use csv reader to specify variable csvreader to hold the contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and go to the next line starting of the content
    csv_header = next(csvreader)

    # Print an empty line to space out
    print("")

    # Print the title of the analysis
    print("Financial Analysis")

    # Print space between two lines
    print("")

    # Print the line to seperate the title and the content
    print("----------------------------")

    # Create a list of months to take all months in the spreadsheet after running a loop through
    month_list = []

    # Create a list of profit/losses to take all profit/loss
    profit_loss = []

    # Set initial profit/losses total as 0 
    profit_loss_total = 0

    # Set a variable to hold the accrued amount of profit/loss changes
    profit_loss_change_accrued = 0
    
    # Run a for loop to read through each row after header...
    for row in csvreader:

        # Add each value of month in the first column to the month list
        month_list.append(row[0])

        # Use len function to calculate the month total
        month_total = len(month_list)

        # Add each value of monthly profit/losses to the total
        profit_loss_total += int(row[1])

        # Add each value to the cart of profit/losses
        profit_loss.append(row[1])

        # Set a variable to hold a list of profit/lost changes
        profit_loss_change_cart=[]

    # Run a for loop from the second row (row [1]) to the end of the profit/loss list
    for x in range(1,len(profit_loss)):

        # Calculate profit_loss change between the current month's with the previous month's
        profit_loss_change = int(profit_loss[x]) - int(profit_loss[x-1])

        profit_loss_change_cart.append(profit_loss_change)

        # Add the changes up
        profit_loss_change_accrued += profit_loss_change

        # Calculate the average of the Profit/Losses changes
        Average = round((profit_loss_change_accrued/(len(profit_loss)-1)),2)

    # Run a loop of profit/loss change in its' cart  
    for profit_loss_change in profit_loss_change_cart:

        # Find a max change and the date of max change
        if profit_loss_change == max(profit_loss_change_cart):
            greatest_inc_date = month_list[profit_loss_change_cart.index(profit_loss_change)+1]
            greatest_increase = profit_loss_change

        # Find a min change and the date of min change 
        elif profit_loss_change == min(profit_loss_change_cart):
            greatest_dec_date = month_list[profit_loss_change_cart.index(profit_loss_change)+1]
            greatest_decrease = profit_loss_change
            

    # Print all values to the terminal
    # Print a space line and total month
    print("")
    print(f'Total Months: {month_total}')
    # Print a space line and total profit/losses
    print("")
    print(f'Total: ${profit_loss_total}')
     # Print a space line and average change
    print("")
    print(f'Average Change: ${Average}')
    # Print a space line and the greatest increase amount and date
    print("")
    print(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})')
    # Print a space line and the greatest decrease amount and date
    print("")
    print(f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease})')

# ---------------------------------------------------------------------------------------------
# Export a text file of the analysis

# Use os module to locate output file path/ file name
file_output = os.path.join("Pybank","analysis", "analysis_result.txt")

# Create the file
with open(file_output, 'w') as output_text:
    # Write a blank line and the title
    output_text.write('\n')
    output_text.write('Financial Analysis')

    # Write a blank line and separation symbol line
    output_text.write('\n')
    output_text.write('\n')
    output_text.write('----------------------------')

    # Write a blank line and the month total
    output_text.write('\n')
    output_text.write('\n')
    output_text.write(f'Total Months: {month_total}')

    # Write a blank line and the profit/losses total

    output_text.write('\n')
    output_text.write('\n')
    output_text.write(f'Total: ${profit_loss_total}')

    # Write a blank line and the average profit/losses change

    output_text.write('\n')
    output_text.write('\n')
    output_text.write('Average Change: $' + str(Average))

    # Write a blank line and the greatest increase in the profit and date
    output_text.write('\n')
    output_text.write('\n')
    output_text.write(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})')

    # Write a blank line and the greatest decrease in the profit and date
    output_text.write('\n')
    output_text.write('\n')
    output_text.write(f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease})')
   
