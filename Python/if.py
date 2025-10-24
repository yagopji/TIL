# 조건문

name = "Jerry"
age =  50

if name == "Tommy" and age == 20:
    print("Hello Tommy!I'm 20 years old.")
elif name == "Tommy" and age != 20:
    print("Hello Tommy!I'm not 20 years old.")
elif name == "Bob" or name == "Alice":
    print("Hello Bob or Alice!")
elif name == "Jerry":
    print("Hello Jerry!")
else:
    print("Hello Stranger!")