# Define a function to convert a number to its corresponding word
def number_to_word(num):
    # Create dictionaries for numbers 0 to 20 and multiples of 10 up to 90
    # These will be used to look up the corresponding word for each digit
    ones_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    tens_dict = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 
        7: 'seventy', 8: 'eighty', 9: 'ninety'
    }
    
    # Invalid input (numbers outside of the range of 0 to 999)
    if num < 0 or num > 999:
        return "Error: Number must be between 0 and 999."
    
    # Numbers 0 to 20
    if num < 20:
        return ones_dict[num]
    
    # Numbers 21 to 99
    if num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens_dict[tens_digit]
        else:
            return tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
    
    # Numbers 100 to 999
    else:
        hundreds_digit = num // 100
        tens_digit = (num // 10) % 10
        ones_digit = num % 10
        if tens_digit == 0 and ones_digit == 0:
            return ones_dict[hundreds_digit] + ' hundred'
        elif tens_digit == 0:
            return ones_dict[hundreds_digit] + ' hundred and ' + ones_dict[ones_digit]
        elif tens_digit == 1:
            return ones_dict[hundreds_digit] + ' hundred and ' + ones_dict[num % 100]
        elif ones_digit == 0:
            return ones_dict[hundreds_digit] + ' hundred and ' + tens_dict[tens_digit]
        else:
            return ones_dict[hundreds_digit] + ' hundred and ' + tens_dict[tens_digit] + '-' + ones_dict[ones_digit]

# Ask the user to input a number
while True:
    num = int(input("Please enter a number between 0 and 999: "))

    # Call the number_to_word function and print the result
    print(number_to_word(num))
