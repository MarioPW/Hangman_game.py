import os
class Validator():

    def intoptions(entry, error_message="Please enter numbers only (no letters, sings or blanks): ", correct_options=range(1000000000000)):      
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

    def letters(letter):    
        err = "You must fill in one letter only (no numbers, sings or blanks): "
        try:
            if len(letter)==1:
                if letter.isalpha() == True:   
                    return str(letter)
                else:
                    print(err)
                    return '_'   
            else:
                print(err)
                return '_'                      
        except:
            print(err)
            return '_'
    
    def url():
        
        attempts = 0
        while True:
            attempts += 1 
            if attempts < 5:
                doc = input("Fill in your .txt file URL (Ej: file.txt): ")
                clean_url = doc[1:-1]
                clean_url1 = clean_url.replace("\\", "/")
                comprob = os.path.isfile(clean_url1)
                if comprob == True:
                    break
                else:
                    print("Incorrect URL...")                         
            else:
                print("Sorry, you have exceeded the valid number of attempts...\n")
                exit()
        return clean_url
            