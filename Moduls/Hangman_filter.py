
# Creates a .txt file with a 4-letters (or more) word list in uppercase from another text file.

def list_words(path,list_name):

    text = open(path,"r",encoding="utf-8")
    words = text.read()
    text.close

    cleaner = {
        ord(".",):None,
        ord(",",):None,
        ord("¿",):None,
        ord("-",):None,
        ord("(",):None,
        ord(")",):None,
        ord(":",):None,
        ord(";",):None,
        ord("?",):None,
        ord("<",):None,
        ord(">",):None,
        ord("!",):None,
        ord("¡",):None,
        ord("–",):None,
        ord("1",):None,
        ord("2",):None,
        ord("3",):None,
        ord("4",):None,
        ord("5",):None,
        ord("6",):None,
        ord("7",):None,
        ord("8",):None,
        ord("9",):None,
        ord("0",):None,
        ord("«",):None,
        ord("»",):None,
        ord("´",):None,
        ord("'",):None,
        ord("^",):None,
        ord("["):None,
        ord("]"):None,
        ord("á",):"a",
        ord("à",):"a",
        ord("é",):"e",
        ord("è",):"e",
        ord("í",):"i",
        ord("ì",):"i",
        ord("ó",):"o",
        ord("ò",):"o",
        ord("ú",):"u",
        ord("ù",):"u",
    }
    words = words.translate(cleaner)
    splited = words.split()

    valid_length = [splited[i] for i in range(len(splited)) if len(splited[i])>=4]
    not_repeated = []
    for i in valid_length:  
        if i not in not_repeated:
            not_repeated.append(i)

    file = open(list_name,"w")
    final_list = str(not_repeated).upper()
    file.write(final_list)
    file.close()

#list_words("The_cabala_book.txt","Whole_words.txt")
