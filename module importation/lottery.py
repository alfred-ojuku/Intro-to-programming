from random import choice

list1 = list(range(2,12))
list1.append('f')
list1.append('o')
list1.append('t')
list1.append('m')
list1.append('x')
print(list1)

i = 0
active = True
while active:
    first = choice(list1)
    sec = choice(list1)
    third = choice(list1)
    fourth = choice(list1)
    lottery_char = f"{first}{sec}{third}{fourth}"
    i += 1
    if lottery_char == 1511:
        active = False

print(i)
#print(f"Ticket matching these four numbers or letters has won: {first}{sec}{third}{fourth}")