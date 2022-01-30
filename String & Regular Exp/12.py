import re

txt = "Hello VIT, No.1 private university VIT in India is VIT"

x = re.search("VIT", txt)
print(x)

if (x):
  print("Yes, match!")
else:
  print("No match")
