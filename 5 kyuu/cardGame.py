import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def card_game(n):
    card_game.AliceBob = [0, 0]
    recur(n)
    return card_game.AliceBob
def recur(n):

    if n <= 0:
        return card_game.AliceBob[0]
    else:
        jon1, jon2 = n % 2, n/2
        if jon1 == 0: #jadi jon1 ini buat ngecek ganjil or genap
            if n == 4:
                card_game.AliceBob[0] += 3
                card_game.AliceBob[1] += 1
                recur(n-4)
            elif jon2 % 2 == 0 :  #nah kalo ini buat buat ngecek apakah hasil dari n /2 itu ganjil ato genap
                card_game.AliceBob = [i+1 for i in card_game.AliceBob]
                recur(n-2)#knp di kurang 2 karna card-nya si alice 1 si bob 1
            else:
                card_game.AliceBob[0] += jon2
                card_game.AliceBob[1] += 1
                recur(n-(jon2)-1)
        else:
            card_game.AliceBob[0] += 1
            n-=1
            jon2 = n/2
            if n == 4:
                card_game.AliceBob[1] += 3
                card_game.AliceBob[0] += 1
                recur(n-4)
            elif jon2 % 2 == 0:
                card_game.AliceBob[1] += 1
                recur(n-1)
            else:
                card_game.AliceBob[1] += jon2
                recur(n-jon2)
    return int(card_game.AliceBob[0])
print(card_game(112742523806484458))
#ini udah solve cuman belum solve:v



    