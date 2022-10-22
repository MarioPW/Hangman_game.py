
class Validator():

    def menu_options_validator(entry, error_message="Please enter numbers only (no letters, sings or blanks): ", correct_options=range(1000000000000)):
        
        attempts = 0
        while True:
            attempts += 1
            if attempts < 5:
                try:  
                    validated_entry = int(input(entry))
                    if validated_entry in correct_options:
                        break
                    else:
                        print(error_message,"\n")        
                except:
                    print(error_message,"\n")
            else:
                print("Sorry, you have exceeded the valid number of attempts...\n")
                exit()
        return validated_entry

    def letter_validator(letter):
        
        lower_letters = [chr(i) for i in range(97,123)]
        upper_letters = [chr(i) for i in range(65,91)]
        valid_chr = lower_letters + upper_letters

        if letter in valid_chr:
            return letter

        else:
            print("You must fill in one letter only (no numbers, sings or blanks): ")


