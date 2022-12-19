"""Count words in file."""

#create a function (one of the paramaters needs to accept a file)
#file open 
#create an empty dict
#create a loop and iterate through the parameter that is being passed through
    #utilize the .get function to see if the string we're trying to search is already in the dict or not
        #if it's not there, use the default value of zero and incriment it by 1
        #if it is there, incriment by 1 
#return the dictionary we made 



def wordcount(filename):
    word_dict = {}
    
    file = open(filename, "r").read()
    print(file)
    ind_words = file.split()
    
    #remove all unnecessary text from the file that we imported using lstrip and rstrip as there is unwanted text before and after the actual text
    
    for word in ind_words:
        #word is the key and we'll add 1 each time, and if the key doesn't exist it'll add it to the dict
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict

#Previous ideas: 
#if word_in_search == word:
  #file = file.strip()
    #return file

print(wordcount("test.txt"))