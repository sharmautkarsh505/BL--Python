#could the user input any number of numbers
#do not need to change the input to integer as in the sample list all elements are strings 
input_string=input('Enter numbers seperated by comma:')
input_list=[]
input_list=input_string.split(',')
print(input_list)
print(tuple(input_list))
