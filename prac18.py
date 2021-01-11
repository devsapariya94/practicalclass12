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

print( "top 5 common word are: ")
word_counter = collections.Counter(d)
for word, count in word_counter.most_common(5):
      print(word, ": ", count ,"times")
fin.close()
