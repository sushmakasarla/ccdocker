import glob
import os
import socket

output = ""

os.chdir(r'/home/data')
my_files = glob.glob('*.txt')
output = "\nFiles present in '/home/data' : [{},{}]\n\n".format(my_files[0], my_files[1])
#output = output + my_files[0]+" , "+my_files[1] + "\n\n"


number_of_words_if = 0
number_of_words_limerick = 0
if_dict = {}
unwanted_chars = ",:?;!"
with open(r'IF.txt','r') as file:
    data = file.read()
    lines = data.split()
    number_of_words_if += len(lines)
    for line in lines:
        line = line.lower()
        line = line.strip(unwanted_chars)
        if line not in if_dict:
            if_dict[line] = 0
        if_dict[line]+=1


with open(r'Limerick.txt','r') as file:
    
    data = file.read()
    lines = data.split()
    number_of_words_limerick += len(lines)

output = output + "Printing total number of words in each text file:" + "\n"
output = output + "Limerick: {}".format(number_of_words_if)+"\n"
output = output + "IF: {}".format(number_of_words_limerick)+"\n"
output = output + "Grand Total: {}".format(number_of_words_if+number_of_words_limerick)+"\n\n"

if_dict_3 = sorted(if_dict.items(), key=lambda x: x[1], reverse=True)[:3]

output = output+"Top 3 words with maximum number of counts in IF.txt :"+"\n"

for key,value in if_dict_3:
    output = output + "{}: {}".format(key,value)+"\n"

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

output = output + "\nIP Address of computer :" + "\n"
output = output + "Your Computer Name is: {}".format(hostname)+"\n"
output = output + "Your Computer IP Address is: {}".format(IPAddr)+"\n\n"

path = "/home/output"
if not os.path.exists(path):
    os.makedirs(path)

if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")

result = open(path + "/" +"result.txt","w")
result.write(output)
result.close()
for line in open(path + "/" +"result.txt","r").readlines():
    print(line.replace("\n",""))


