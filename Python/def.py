# #  함수

# def say_hello(name, location):
#     print("hello " + name)
#     print("where are you from? " + location)

# say_hello("Tommy", "New York")

def add_numbers(a, b):
    result = a + b
    print(result)

def add_numbers_with_return(a, b):
    result = a + b
    print(result)
    return result

result1 = add_numbers_with_return(1, 2)
print("결과:", result1)    