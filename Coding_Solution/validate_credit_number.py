import re

def validate_credit_number(card_num):
    print(card_num)

    if card_num is None:
        return "Invalid"
    
    # Validate the format
    if not re.match(r'[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', card_num):
        return 'Invalid'
    
    # Check for repeated consecutive digits
    prev_digit = card_num[0]
    repeat_count = 1
    
    for digit in card_num[1:]:
        if digit == prev_digit:
            repeat_count += 1
        else:
            prev_digit = digit
            repeat_count = 1
        
        if repeat_count == 4:
            return "Invalid"
        
    return "Valid"

def test_validate_credit_number_valids():
    valid_inputs = ["4253625879615786", "4424424424442444", "5122-2368-7954-3214"]
    expected = "Valid"    
    for inp in valid_inputs:
        assert expected == validate_credit_number(inp)

def test_validate_credit_number_invalids():
    invalid_inputs = ["42536258796157867", "4424444424442444", "44244x4424442444", "5122-2368-7954 - 3214", "0525362587961578"]
    expected = "Invalid"
    for inp in invalid_inputs:
        assert expected == validate_credit_number(inp)
    
test_validate_credit_number_valids()
test_validate_credit_number_invalids()
print("Test cases completed successfully")
