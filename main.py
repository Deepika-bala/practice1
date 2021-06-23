from collections import Counter
import re
import uuid
import logging
import configparser
fri=configparser.ConfigParser()
path='configuration'
fri.read(path)
path1=fri.get('deepi','inp')
print(path1)
path2=fri.get('deepi','oup')
print(path2)

logging.basicConfig(filename='deepi.log',level=logging.DEBUG)
class parent():
    def __init__(self, filename, unique_filename):
        self.Cricket = filename
        self.write = unique_filename

    def FileRead(self):
        f=open(path1,'r')
        crk=f.read().split()
        return crk
    def FileWrite(self):
        unique_filename = str(uuid.uuid4())
        print(unique_filename)
        file = open(path2, 'w')
        file.write(strg)
class startend(parent):
    def To_Ing(self):
        count1=0
        count2=0
        crk=parent.FileRead(self)
        for i in crk:
            if(i.startswith('to')==1 or i.startswith('T0')==1):
                count1=count1+1
        self.printstmt("The number of words having prefix with “To” in the input file", count1)
        for i in crk:
            if(i.endswith('ing')==1):
                count2=count2+1

        self.printstmt("The number of words ending with 'ing' in the input file", count2)
        logging.debug('{},{}'.format(count1,count2))
        return count1,count2



    def  cou(self,crk):
        flower = Counter( crk )
        crk = parent.FileRead(self)
        print(flower)
        self.printstmt("most common word is ", flower.most_common(1))
        dict = {}
        for x, element in enumerate(flower):
            dict[element] = x
        print(dict)

    def pali(self,crk):
        crk = parent.FileRead(self)
        for p in crk:
            if (p == p[::-1]):
                return p

    def uin(self,crk):
        crk = parent.FileRead(self)
        arr = []
        for i in crk :
            res = re.split('a|e|i|o|u', i)
            print ( 'Splitted word ', res)
            separator =''
            res=separator.join(res)
            arr.append(res)
        self.printstmt('Appended the splitted word ', arr)
        n_arr=[]
        l=''
        for j in arr:
            if len(j)>2 :
                p = j[:2] + j[2].upper() + j[2 + 1:]
                n_arr.append(p)
            else :
                l=j
                n_arr.append(l)
        self.printstmt( 'After capitalizing 3rd letter ', n_arr)
        cap=[]
        for j in n_arr:
            if (n_arr.index(j)+1) % 5 ==0 :
                j=j.upper()
            cap.append(j)
        self.printstmt('After capitalizing every 5th word',cap)
        return cap


    def SwapBlank(self,cap):
        crk = parent.FileRead(self)
        strg = ''
        for r in cap:
            if (r.endswith('.') == 1):
                r = r.rstrip(r[-1])
                strg = strg + str(r) + ';\n'
            else:
                strg = strg + str(r) + '-'
        self.printstmt('after swapping with blank space : \n', strg)
        return strg
    def printstmt(self,f,r):
        print(f,r)
obj = startend('Cricket.txt','unigue_filename')
crk = obj.FileRead()
a,d = obj.To_Ing()
obj.cou(crk)
obj.pali(crk)
cap = obj.uin(crk)
strg=obj.SwapBlank(cap)
obj.FileWrite()




