
# Creates a .txt file with a 4-letters (or more) word list in uppercase from another text file.

def list_words(path, lists_name):

    text = open(path,"r",encoding="utf-8")
    words = text.read()
    text.close()

    clean_text = filter(lambda x: x.isalpha() or x in ("\t","\n"," ","ñ","Ñ"), words)
    clean_text1 = "".join(clean_text)
    splited = clean_text1.split()

    valid_length = [splited[i] for i in range(len(splited)) if len(splited[i])>=4]
    not_repeated = []
    for i in valid_length:  
        if i not in not_repeated:
            not_repeated.append(i)

    file = open(lists_name,"w")
    final_list = str(not_repeated).upper()
    file.write(final_list)
    file.close()

    return lists_name

def get_url(index):
        
    urls = ["Days.txt","Months.txt","Animals.txt","Whole_Words.txt"]
    return urls[index-1]
#list_words("texto.txt","words3.txt")
