# Add csv module to read csv files
import csv

# Add os module to create file path across operating systems
import os

# Create a file path
csvpath = os.path.join("PyPoll","Resources", "election_data.csv")

# Open csv file election_date
with open(csvpath) as csvfile:

    # Use csv reader to specify variable csvreader to hold the contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and go to the next line, starting of the content
    csv_header = next(csvreader)

    # Print an empty line to space out
    print("")

    # Print the title of the analysis
    print("Election Results")

    # Print space between two lines
    print("")

    # Print the line to seperate the title and the content
    print("----------------------------")

    # Set a counter to count the rows (total votes)
    counter = 0

    # Set a candidate list to hold the candidate names
    candidate_list = []

    # Set a dictonary with the value as candidate name and the value as total vote per candidate name
    candidate_dic = {}
    
    # Run a for loop to read through all rows after the header
    for row in  csvreader:

        # Each time the loop goes through one row, add 1 to the counter
        counter += 1

        # set a value each time a candidate is voted
        candidate_voted = row[2]

        # Check if the candidate voted is not in the  candidate_list
        if candidate_voted not in candidate_list:

            # Add the candidate voted name to the candidate list
            candidate_list.append(candidate_voted)

            # Set the inital value as 0 when there is a new candidate added to the list
            candidate_dic[candidate_voted] = 0

            # Add 1 to the value (the count) of the newly added candidate
            candidate_dic[candidate_voted] +=1
        
        # If the candidate voted is already in the list
        else:
             # Add 1 to the value (the count) of the existing candidate in the candidate list
            candidate_dic[candidate_voted] +=1

    # Print a blank line
    print(" ")

    # Print total vote to terminal
    print(f'Total Votes: {counter}') 
    
     # Print a blank line
    print(" ")

    # Print a line separation
    print("----------------------------")

    # Set a list to hold the percent and then, to find out max percent
    percent_list =[]

    # Set a list to hold candidate messages to print out a text file later on
    candidate_messages = []

    # Run a loop to through dictionary
    for x in candidate_dic:   

        # Calculate the percentage
        percent = round((candidate_dic[x]/counter *100),3)

        # Add to the percent cart
        percent_list.append(percent)

        # Print a blank line
        print("")

        # Define the message
        message = f'{x}: {percent}% ({candidate_dic[x]})'

        # Add a value to candidate message list
        candidate_messages.append(message)

        # Print the candidate with their percents and total votes
        print(message)


    # Print a blank line
    print(" ")
    
    # Run a for loop to find out the maximun percent
    for percent in percent_list:

        # if the percent is maximum then
        if percent == max(percent_list):

            # Find out the winner according the index of the percent
            winner = candidate_list[percent_list.index(percent)]

            # Print the a line separation
            print("----------------------------")

            # Print a blank line
            print("")

            # Print the message
            print('Winner:' +' ' + str(winner))

            # Print a blank line
            print("")

            # Print the a line separation
            print("----------------------------")

# ---------------------------------------------------------------------------------------------
# Export a text file of the analysis

# Use os module to locate output file path/ file name

file_output = os.path.join("PyPoll","analysis", "analysis_result.txt")

# Create the file
with open(file_output, 'w') as output_text:
    
    # Write a blank line and the title
    output_text.write('\n')
    output_text.write('Election Result')

    # Write a blank line and separation symbol line
    output_text.write('\n')
    output_text.write('\n')
    output_text.write('----------------------------')

    # Write a blank line and the total votes
    output_text.write('\n')
    output_text.write('\n')
    output_text.write(f'Total Votes: {counter}')

    # Write a blank line and separation symbol line
    output_text.write('\n')
    output_text.write('\n')
    output_text.write('----------------------------')

    # Run a for loop through all candidate details and print out messages of their names, percentage and votes

    for message in candidate_messages:  
        output_text.write('\n')
        output_text.write('\n')
        output_text.write(message)

    # Write a blank line and separation symbol line
    output_text.write('\n')
    output_text.write('\n')
    output_text.write('----------------------------')

    # Write a blank line and the winner

    output_text.write('\n')
    output_text.write('\n')
    output_text.write('Winner:' +' ' + str(winner))

    # Write a blank line and separation symbol line
    output_text.write('\n')
    output_text.write('\n')
    output_text.write('----------------------------')

   
