"""import libraries"""
from collections import Counter
import re
import uuid
import logging
import configparser as cp
from configparser import ConfigParser, ExtendedInterpolation
config = cp.ConfigParser()
config.read_file(open(r'configuration.txt'))
path1 = config.get('Input File', 'path1')
path2 = config.get('Log File', 'path2')
path3 = config.get('Output File', 'path3')
class New_Class:


    def __init__(self, filename, unique_filename):
        self.file = filename
        self.fileWrite = unique_filename

    def read_file(self ):
        f = open(self.file, 'r')
        crk = f.read().split()
        print(crk)
        return crk

class student(New_Class):
    def to_ing(self,crk):
        count1 = 0
        count2 = 0
        for i in crk:
            if i.startswith('to') == 1 or i.startswith('T0') == 1:
                count1 = count1 + 1
        self.printstmt("The number of words having prefix with “To” in the input file", count1)
        for i in crk:
            if i.endswith('ing') == 1:
                count2 = count2 + 1
        self.printstmt("The number of words ending with 'ing' in the input file", count2)

    def cou(self, crk):  # pylint: disable=redefined-outer-name
        flower = Counter(crk)
        print(flower)
        self.printstmt("most common word is ", flower.most_common(1))
        dict1 = {}
        for i, element in enumerate(flower):
            dict1[element] = i
        print(dict1)
        return dict1

    def pali(self, crk):#pylint: disable=redefined-outer-name

        for i in crk:
            if i == i[::-1]:
                self.printstmt("The palindrome is",i)
        return i

    """inheriting a child class uni to split the words by vowels"""

    def uin(self, crk):  # pylint: disable=redefined-outer-name
        arr = []
        for i in crk:
            res = re.split('a|e|i|o|u', i)
            print('Splitted word ', res)
            separator = ''
            res = separator.join(res)
            arr.append(res)
        self.printstmt('Appended the splitted word ', arr)
        n_arr = []
        lit = ''
        for j in arr:
            if len(j) > 2:
                pup = j[:2] + j[2].upper() + j[2 + 1:]
                n_arr.append(pup)
            else:
                lit = j
                n_arr.append(lit)
        self.printstmt('After capitalizing 3rd letter ', n_arr)
        cap = []  # pylint: disable=redefined-outer-name
        for j in n_arr:  # pylint: disable=redefined-outer-name

            if (n_arr.index(j) + 1) % 5 == 0:
                j = j.upper()
            cap.append(j)
        self.printstmt('After capitalizing every 5th word', cap)
        return cap

    """Inheriting child class to swaping the blank space"""

    def swapblank(self, cap):  # pylint: disable=redefined-outer-name

        strg = ''  # pylint: disable=redefined-outer-name
        for i in cap:
            if i.endswith('.') == 1:
                i = i.rstrip(i[-1])
                strg = strg + str(i) + ';\n'
            else:
                strg = strg + str(i) + '-'
        self.printstmt('after swapping with blank space : \n', strg)
        return strg

    def printstmt(self, data, ans):
        print(data, ans)
        strg = data + ":" + str(ans)
        logging.info(strg)


unique_filename = str(uuid.uuid4())
print(unique_filename)
s = student('Cricket.txt',unique_filename)
crk= s.read_file()
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info(str(path1))
logging.info(str(path2))
logging.info(str(path3))
logging.info('This will get logged to a file')
s.to_ing(crk)
d=s.cou(crk)
name=s.pali(crk)
cap=s.uin(crk)
strg=s.swapblank(cap)
logging.info('logging done !!')

