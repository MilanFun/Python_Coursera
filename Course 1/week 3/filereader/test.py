from typing import Text
from solution import FileReader

f = FileReader("/home/alekseyhp/test11.txt")
text = f.read()
print(text)
