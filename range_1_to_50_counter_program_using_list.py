"""If this did not work, then I will try to do it as a variable."""
one_to_ten = []
eleven_to_twenty = []
twentyone_to_thirty = []
thirtyone_to_forty = []
fortyone_to_fifty = []

#Create a loop for the repetition of input numbers
#Create a loop for the input numbers
while True:
    try:
        #loop for:
        inp_number = int(input("Please insert a number: "))
        #Execute the comparatives (if and elif) and add 1 for each category:
        if inp_number >= 1 and inp_number <= 10: #1 to 10
            one_to_ten.append(inp_number)
        elif inp_number >= 11 and inp_number <=20: #11 to 20
            eleven_to_twenty.append(inp_number)
        elif inp_number >= 21 and inp_number <=30: #21 to 30
            twentyone_to_thirty.append(inp_number)
        elif inp_number >= 31 and inp_number <=40: #31 to 40
            thirtyone_to_forty.append(inp_number)
        elif inp_number >= 41 and inp_number <=50: #41 to 50
            fortyone_to_fifty.append(inp_number)
        else:
            raise
        
    except:
        #Make an error message for invalid input and;
        print("You have placed a wrong input...")

        num_in_one = len(one_to_ten)
        num_in_two = len(eleven_to_twenty)
        num_in_three = len(twentyone_to_thirty)
        num_in_four = len(thirtyone_to_forty)
        num_in_five = len(fortyone_to_fifty)

        #print the range of numbers
        print(f"So here is the count:")
        print(f"1 to 10: {num_in_one}")
        print(f"11 to 20: {num_in_two}")
        print(f"21 to 30: {num_in_three}")
        print(f"31 to 40: {num_in_four}")
        print(f"41 to 50: {num_in_five}")
        break