# 조건문

# list = [1,2,3,4,5]

# if 1 in list:
#     print("number 1 is in list!")

# if 0 not in list:
#     print("number 0 isn't in list!")

# if (1 in list) and (2 in list):
#     print("number 1 and 2 are in list!")

# if (1 in list) or (0 in list):
#     print("number 0 or 1 is in list!")

# 조건문 복습

# students = [
#     {'name' : 'Tommy', 'age' : 39, 'height' : 177},
#     {'name' : 'Mini', 'age' : 38, 'height' : 157},
#     {'name' : 'Michael', 'age' : 8, 'height' : 180},
#     {'name' : 'Jenny', 'age' : 7, 'height' : 170}
# ]

# for student in students:
#     if student['age'] > 20:
#         if student['height'] >= 175:
#             print(f"{student['name']} 은 키가 175가 넘는 성인입니다.")
#         else:
#             print(f"{student['name']} 은 키가 175가 넘지 않은 성인입니다.")
#     else:
#         print(f"{student['name']} 은 미성년자입니다.")


fruits = ['apple', 'apple', 'banana', 'banana', 'banana', 'strawberry', 'kiwi', 'watermelon', 'watermelon']

num_fruits = {}
for fruit in fruits:
    if fruit in num_fruits:
        num_fruits[fruit] += 1
    else:
        num_fruits[fruit] = 1
print(num_fruits)