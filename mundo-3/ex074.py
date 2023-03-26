from random import randint
num = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)

for c in num:
    print(c, end = " ")

print(f"\nO maior número é {max(num)}\n"
      f"O menor número é {min(num)}")