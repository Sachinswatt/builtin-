s = " hello sachin how are you "
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.split())
print(s.split(","))

s = ["hello","how","are","you"]
print("-".join(s))

s = ["hello","how","are","you"]
print(" ".join(s))
s = "hello how are you"
print(s.replace("how","who"))
print(s.find("how"))
print(s.index("l"))
print(s.count("h"))
print(s.startswith("h"))
print(s.endswith("t"))
print(s.endswith("o"))

p = "pythonisbest"
print(p.isalpha()) 
print(p.isdigit())
print(p.isalnum())
print(p.isspace())
print(p.center(50))
print(p.zfill(40))