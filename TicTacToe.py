def b():
    table = {'1': ' ' , '2': ' ' , '3': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '7': ' ' , '8': ' ' , '9': ' ' }

    table_keys = []

    for key in table:
        table_keys.append(key)

    def printTable(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])

    turn = 'X'
    count = 0


    for i in range(10):
        printTable(table)
        print("Ваш ред е," + turn + ".На коя позиция искате да отидете? (1 - 9)")

        move = input()        

        if table[move] == ' ':
            table[move] = turn
            count += 1
        else:
            print("На това място вече има фигура.\nНа кое място искате да отидете? (1 - 9)")
            continue

        if count >= 5:
            if table['7'] == table['8'] == table['9'] != ' ':
                printTable(table)
                print("\Играта свърши.\n")                
                print(" **** " +turn + " победи. ****")                
                break
            elif table['4'] == table['5'] == table['6'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break
            elif table['1'] == table['2'] == table['3'] != ' ': 
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break
            elif table['1'] == table['4'] == table['7'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break
            elif table['2'] == table['5'] == table['8'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break
            elif table['3'] == table['6'] == table['9'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break 
            elif table['7'] == table['5'] == table['3'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break
            elif table['1'] == table['5'] == table['9'] != ' ':
                printTable(table)
                print("\nИграта свърши.\n")                
                print(" **** " +turn + " победи. ****")
                break 

        if count == 9:
            print("\nИграта свърши.\n")                
            print("Равенство!")

        if turn =='X':
            turn = 'O'

        else:
            turn = 'X'      
