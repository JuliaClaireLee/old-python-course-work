# -------------------------------------------------
#        Name: Julia Lee AND Anushree Goswami
#    Filename: lab3.py
#        Date: 9/26/2018
#
# Description: This lab will show
#               how we can manipulate strings              
# -------------------------------------------------

# Challenge 1:
s = "Smith College CS Department"
department = s[14:27]
school = s[0:14]
print("+"+"-"+'-'*(len(school + department)+1)+"+")
print('|',school + department,"|")
print("+"+ "-"+'-'*(len(school + department)+1)+"+")

# Challenge 2:

phone_number = "2022243121"
print("(" +phone_number[:3]+")" + " " + phone_number[3:6] + "-"+ phone_number[6:11])


#final Challenge:
name = "Name: Julia Lee and Anushree Goswami"
filename = "filename: lab3.py"
date = "Date: 9/26/2018"
space = ""
desc = """Description: This lab will show
              how we can manipulate strings"""
desc = desc.split()
name_len = len(name)+10
line = "-"*name_len
words = ""
words_2 = ""
words_3 = ""
for var in [line, name, filename, date, space]:
     print('#',var)
for w in desc[0:5]:
    words += w + " "
for w in desc [5:15]:
    words_2 += w +" "
for w in desc [15:]:
    words_3 += w +" "
if len(desc) >= 15:
    print("#", words)
    print("#", words_2)
    print("#", words_3)
elif len(desc) > 5:
    print("#", words)
    print("#", words_2)
else:
    print("#", words)
print("#" ,line)
      
       




