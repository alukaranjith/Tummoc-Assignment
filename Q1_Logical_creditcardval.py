def validate_credit_card(number):
    # Convert the credit card number to a string
    number = str(number)

    # Check the length of the credit card number
    if len(number) < 13 or len(number) > 16:
        return False

    # Check the card type and length
    if number[0] == '4' and len(number) == 13:  # Visa
        card_type = "Visa"
    elif number[0] == '5' and len(number) == 16:  # MasterCard
        card_type = "MasterCard"
    elif number[:2] == '37' and len(number) == 15:  # American Express
        card_type = "American Express"
    elif number[0] == '6' and len(number) == 16:  # Discover
        card_type = "Discover"
    else:
        return False

    # Apply the Luhn algorithm to validate the credit card number
    total = 0
    for i in range(len(number) - 2, -1, -2):
        digit = int(number[i]) * 2
        if digit > 9:
            digit = digit // 10 + digit % 10
        total += digit
        print(total)

    for i in range(len(number) - 1, -1, -2):
        total += int(number[i])

    if total % 10 == 0:
        return True
    else:
        return False


# Prompt the user to enter a credit card number
credit_card_number = int(input("Enter a credit card number: "))

# Validate the credit card number
if validate_credit_card(credit_card_number):
    print("Valid credit card")
else:
    print("Invalid credit card")
