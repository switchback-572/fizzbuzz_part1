number = int(input("１つの自然数を入れてね："))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(str(number))

# Day1 6:24
# リファクタリングしていく
# cont +G でマルチカ-ソル
