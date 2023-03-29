#exo pwd
def  auth(a):
    a="jedha123"
    pwd=input("write pwd")
    while  pwd!=a :
        pwd=input("write pwd")
    print("correct!")    


auth("hkrfgr")    
#crrection
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_lowercase_quant = 0
digits = '0123456789'
# digits_quant = 0
# user_password = input("Enter your passeword ")
# for car in user_password : 
#   if car in ascii_lowercase : 
#     ascii_lowercase_quant +=1
#   elif car in digits :
#       digits_quant +=1
# print(ascii_lowercase_quant)
# print(digits_quant)

ascii_lowercase_quant = 1
digits_quant = 1

while ascii_lowercase_quant < 6 or digits_quant <2 :
    print("Your password has to have at least 6 letters and at least 1 caracter")
    user_password = input("Enter your password ")
    digits_quant = 0
    digits_quant = 0
    for car in user_password : 
      if car in ascii_lowercase : 
        ascii_lowercase_quant +=1
      elif car in digits :
        digits_quant +=1
    print(ascii_lowercase_quant)
    print(digits_quant)

print("this is good")