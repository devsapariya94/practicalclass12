file1=open("first.txt")
file2=open("out.txt","a")
Content = file1.read()
CoList = Content.split("\n") 
 

search_keyword="a"
for i in range (0, len(CoList)):
    if search_keyword in CoList[i]:
        file2.write(CoList[i]+"\n")
    else:
        pass
file1.close()
file2.close()
print("All line containing '",search_keyword,"' are printed in 'out.text'")

