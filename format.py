import sys

fr=open(sys.argv[1],"r")
fw=open("output","w")
lines =fr.readlines()
#print(len(lines))
#print(lines)
for l in lines :
    words = l.split()
    if words[0] == 'Chr' :
       chrome = words[1]
       start  = words[12]
       end    = words[15]
       print(chrome+' '+start+' '+end)
       print(chrome+'\t'+start+'\t'+end, file = fw)
fw.close()
