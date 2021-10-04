import random
def game(Comp,Your):
    if Comp == Your:
        return 'tie'
    elif Comp == 's' and Your == 'w':
        return 'You lose'
    elif Comp == 's' and Your == 'g':
        return 'You win'
    elif Comp == 'w' and Your == 's':
        return 'You win'
    elif Comp == 'w' and Your == 'g':
        return 'You lose'
    elif Comp == 'g' and Your == 's':
        return 'You lose'
    elif Comp == 'g' and Your == 'w':
        return 'You win'

print('Comp turn: Snake(s), Water(w), Gun(g) ?')
a = random.randint(1,3)
Comp = ''
if a == 1:
    Comp = 's'
elif a == 2:
    Comp = 'w'
else:
    Comp = 'g'
print('Comp selected: ',Comp)
Your = input('Your turn: Snake(s), water(w), Gun(g) ?')
print(Your)

print(game(Comp,Your))

