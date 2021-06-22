from collections import Counter
import re
import uuid
def pre_end(file):
    f=open(file,'r')
    flower=f.read().split()
    #print(flower)
    count1 = 0
    count2 = 0

    for i in flower:
        if(i.startswith('to')==1 or i.startswith('To')==1):
            count1=count1+1
    for i in flower:
        if(i.endswith('ing')==1):
            count2=count2+1
    return count1 , count2
    fo= Counter(f.read().split())

    print("most common word is ", fo.most_common(1))
    print(fo)
def rep(file):
    f = open(file, 'r')
    flower =Counter( f.read().split())
    print("most common word is " , flower.most_common(1))
    dict={}
    for x ,element in enumerate (flower):
        dict[element]=x
    print(dict)


def pali(file):
    f = open(file, 'r')
    flower = f.read().split()
    for p in flower:
        if (p == p[::-1]):
            print("The letter is a palindrome is ",p)

def uni(file):
    flower = open(file, 'r')
    f=flower.read().split()
    arr = []
    for i in f :
        res = re.split('a|e|i|o|u', i)
        print ( 'Splitted word ', res)
        separator =''
        res=separator.join(res)
        arr.append(res)
    print('Appended the splitted word ', arr)
    n_arr=[]
    p=''
    for j in arr:
        if len(j)>2 :
            p = j[:2] + j[2].upper() + j[2 + 1:]
            n_arr.append(p)
        else :
            p=j
            n_arr.append(p)
    print( 'After capitalizing 3rd letter ', n_arr)
    cap=[]
    for j in n_arr:
        if (n_arr.index(j)+1) % 5 ==0 :
            j=j.upper()
        cap.append(j)
    print('After capitalizing every 5th word',cap)
    return cap

def SwapBlank(cap) :
    strg=''
    for r in cap:
        if(r.endswith('.')==1) :
            r = r.rstrip(r[-1])
            strg=strg+str(r)+';\n'
        else:
            strg = strg + str(r) + '-'
    print('after swapping with blank space : \n',strg)
    unique_filename = str(uuid.uuid4())
    print(unique_filename)
    file=open(unique_filename,'w')
    file.write(strg)

c,d,=pre_end('flowering')
print("The number of words having prefix with “To” and in the input file is",c)
print("The number of words hending with “ing” in the input file is",d)
pre_end('flowering')
rep('flowering')
pali('flowering')
cap = uni('flowering')
SwapBlank(cap)

