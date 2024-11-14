import re
str = "My name is Aniket varape and my roll number is 51"

regex='\d+'
result= re.search(regex,str)
print(result.group())

match=re.search(r'Aniket',str)
print("Start index: ",match.start())
print("End index: ",match.end())

pattern ="[a-m]"
output=re.findall(pattern,str)
print(output)

str1="DYP.CET"
match1=re.search(r'\.',str1)
print(match1)

p= re.compile('[a,e]')
print(p.findall("Hello,I'm Aniket varape"))


condition=r'^Hello'
# for string in str:
#     if re.match(condition,string):
#         print("Condition matched")
#     else:
#         print("condtion not matched")

if re.findall(condition,str):
     print("Condition matched")
else:
        print("condtion not matched")
