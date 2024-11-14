import re
import string

text="Hello..!! this is an example of text processing."

nonpunc=text.translate(str.maketrans('','',string.punctuation))
print(nonpunc)

lowertxt=text.lower()
print(lowertxt)

uppertxt=text.upper()
print(uppertxt)

tokens = text.split()
print(tokens)

