from http.client import HTTPConnection
from Hangman_filter import list_words
import requests

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
        
        err = "You must fill in one letter only (no numbers, sings or blanks): "
        try:
            if len(letter)==1:
                if letter.isalpha() == True:   
                    return str(letter.upper())
                else:
                    print(err)
                    return '_'   
            else:
                print(err)
                return '_'                      
        except:
            print(err)
            return '_'
    
    def get_url(index):
        
        urls = ["Days.txt","Months.txt","Animals.txt","Whole_words.txt","words2.txt"]
        return urls[index-1]
    
    # def get_words_from_url():

    #     users_url = input("Fill in your text file URL (Ej: file.txt, file.doc)")
    #     file = open(users_url,"r")
    #     words = file.read()
    #     file.close()
    #     list_words(words, "Users_words.txt")
        
    #     return "Users_words.txt"


