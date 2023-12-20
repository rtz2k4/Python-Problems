#using Hashing

def printDuplicates(str):
    count = {}

    for i in range(len(str)):
        if (str[i] in count):
            count[str[i]] += 1
        else: 
            count[str[i]] = 1
    
    for character, occurence in count.items():
        if (occurence>1):
            print(str(character) + ", count = " + str(occurence))

    
#using Sorting

def prt_sorting_duplicates(str):
    char_list = list(str)
    char_list.sort()

    i=0 
    while i<len(char_list):
        count = 1
        while i < len(char_list)-1 and char_list[i] == char_list[i+1]:
            count += 1
            i += 1
        
        if count > 1:
            print(char_list[i], ", count = ", count)
        i += 1





