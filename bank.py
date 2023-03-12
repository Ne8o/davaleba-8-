    #bank
'''
  Run your program with python bank.py. Type Hello and press Enter. Your program should output:
$0 
Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
$0
Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
$20
Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
$100

     print()
'''

hi = str(input("say hi: ")).title()

if hi.split() [0] == ("Hello"):
     print("$0")
elif hi[0] == "H":
     print("$20")
else :
    print("100$")
