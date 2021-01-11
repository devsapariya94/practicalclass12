# # Python program to find the k most frequent words 
# # from data set 
# from collections import Counter 

# #data_set = "phished emails"  
# def most_common_word(dataset , n=10):   
#     # split() returns list of all the words in the string 
#     split_it = data_set.split() 
    
#     # Pass the split_it list to instance of Counter class. 
#     count = Counter(split_it) 
    
#     # most_common() produces k frequently encountered 
#     # input values and their respective counts. 
#     most_occur = count.most_common(n) 
    
#     print(most_occur)
# file1=open("first.txt")
# most_common_word(file1)
# file1.close()


import collections
fin = open('email.txt','r')
a= fin.read()
d={ }
L=a.lower().split()
for word in L:
     word = word.replace(".","")
     word = word.replace(",","")
     word = word.replace(":","")
     word = word.replace("\"","")
     word = word.replace("!","")
     word = word.replace("&","")
     word = word.replace("*","")
     word=word.replace("@","")

for k in L:
     key=k
     if key not in d:
           count=L.count(key)
           d[key]=count

# n_print = int(input("How many most common words to print: "))
# print("\nOK. The {} most common words are as follows\n".format(n_print))
print( "top 5 common word are: ")
word_counter = collections.Counter(d)
for word, count in word_counter.most_common(5):
      print(word, ": ", count ,"times")
fin.close()