szer = 6
wys = 5

przeciwnicy = [(0, 1), (2, 3), (2, 4), (3, 4)]
monety = [(1, 1), (2, 0), (3, 3), (5, 3)]
rzeka_y = 2

for y in range(wys):
    for x in range(szer):
        # ustawienie przeciwników
        if (x, y) in przeciwnicy:
            print('x', end=' ')
        # ustawienie monet
        elif (x, y) in monety:
            print('*', end=' ')
        # rzeka
        elif y == rzeka_y:
            print('=', end=' ')
        # trawa
        else:
            print('.', end=' ')
    print()
