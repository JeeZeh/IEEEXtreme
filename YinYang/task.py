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

print("".join(string))