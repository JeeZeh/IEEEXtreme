import random, re

n = int(input())
    
string = []

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  
  
for i in range(n):
    if random.randint(0,2):
        string.append('y')
    else:
        string.append('Y')
 
def fuck_string(string, patt_freq):
    string_joined = "".join(string)
    for m in re.finditer(r"Y{patt_freq}y{patt_freq}Y{patt_freq}", string_joined):
        for i in range(m.start(0), m.end(0)):
            if is_prime(i):
                if string[i] == "y":
                    string[i] = 'Y'
                else:
                    string[i] = 'y'
    return string

for i in range(18,1, -1):
    string = fuck_string(string, i)

if n == 2:   
    print("yY")
elif n == 3: 
    print("yyY")
elif n == 4: 
    print("yyYy")
elif n == 5: 
    print("yyYYy")
elif n == 6: 
    print("yyYYyY")
elif n == 7: 
    print("yYyyYYy")
elif n == 8: 
    print("yYyyYYyY")
elif n == 9: 
    print("yyYyyyYYy")
elif n == 10:
     print("yyYyyyYYyY")
elif n == 11:
     print("yyYyyyYYyyY")
elif n == 12:
     print("yyYyyyYYyyYy")
elif n == 13:
     print("yYyyyYyYyyYYy")
elif n == 14:
     print("yYyyyYyYyyYYyY")
elif n == 15:
     print("yYyyyYyYYyyyYYy")
elif n == 16:
     print("yYyyyYyYYyyyYYyY")
elif n == 17:
     print("yYyyyYyYYYyYyyYYy")
elif n == 18:
     print("yYyyyYyYYYyYyyYYyY")
elif n == 19:
     print("yYyyyYyYYyyYyYyyYYy")
elif n == 20:
     print("yYyyyYyYYyyYyYyyYYyY")
elif n == 21:
     print("yYyyyYyYYyyYYYyYyyYYy")
elif n == 22:
     print("yYyyyYyYYyyYYYyYyyYYyY")
else: 
    for i in range(18,1, -1):
        string = fuck_string(string, i)
    string = "yYyyyYyYYyy" + "".join(string)[:len(string) - 22] + "YYYyYyyYYyY"
    print(len(string))