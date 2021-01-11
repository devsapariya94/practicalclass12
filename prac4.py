def read(fname):
          with open(fname, "r+") as file:
                    lines=file.readlines()
                    return lines
fname="mytext.txt"
lines=read(fname)
for i in lines:
          print(i.rstrip())