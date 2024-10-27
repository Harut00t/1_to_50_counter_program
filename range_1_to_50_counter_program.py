import math

"""If this did not work, then I will try to do it as a variable."""
one_to_ten = 0
eleven_to_twenty = 0
twentyone_to_thirty = 0
thirtyone_to_forty = 0
fortyone_to_fifty = 0

#Create a loop for the repetition of input numbers
while True:
    #Create a loop for the input numbers
    while True:
        try:
            #loop for:
            inp_number = int(input("Please insert a number: "))
            #Execute the comparatives (if and elif) and add 1 for each category:
            if inp_number >= 1 and inp_number <= 10: #1 to 10
                one_to_ten = one_to_ten + 1
            elif inp_number >= 11 and inp_number <=20: #11 to 20
                eleven_to_twenty = eleven_to_twenty + 1
            elif inp_number >= 21 and inp_number <=30: #21 to 30
                twentyone_to_thirty = twentyone_to_thirty + 1
            elif inp_number >= 31 and inp_number <=40: #31 to 40
                thirtyone_to_forty = thirtyone_to_forty + 1
            elif inp_number >= 41 and inp_number <=50: #41 to 50
                fortyone_to_fifty = fortyone_to_fifty + 1
            else:
                raise
            
        except:
            print("You have placed a wrong input...")
            print(f" Here is the count: {one_to_ten, eleven_to_twenty, twentyone_to_thirty, thirtyone_to_forty, fortyone_to_fifty}")


#Make an error message for invalid input and;

#print the range of numbers

print(f"1 to 10 is {one_to_ten}")