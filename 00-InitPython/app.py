def sum(numbe_one,number_two):
    numbe_one = convert_integer(numbe_one)
    number_two = convert_integer(number_two)
    
    result = numbe_one + number_two
    
    return result

def convert_integer(number_string):
    
    converted_interger = int(number_string)
    return converted_interger

answer = sum("1","2")