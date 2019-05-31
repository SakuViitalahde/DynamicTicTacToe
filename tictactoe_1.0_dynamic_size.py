import itertools
game_size = 5

#player = merkki mikä asetetaan
#Row rivi indexi
#Column sarakkeen indexi
#just_display tulestaan vain pöytä
def game_board(game_map, player = 0, row = 0, column = 0, just_display=False): 
    try:

        if game_map[row][column] != 0:
            print("This position is occupado!")
            return game_map, False


        print("   " + "  ".join([str(i) for i in range(len(game_map))]))

        #just display on true ei aseta arvoa ollenkaan
        if not just_display:
            game_map[row][column] = player

        #looppi
        #Enumerate antaa meille indexin ja valuen listasta
        #Printataan indexi ja valua saadaan kent8uijille indexi ja headerin avulla tarkat paikat
        for index, value in enumerate(game_map):
            print(index, value)	
        
        return game_map, True
    except IndexError as e:
        #virheiden hallinta tilanteessa jossa käyttäjä syöttää virheellisen arvon kenttiä syöttäessä
        print("Input value, value needs to be between 0 - 2" , e)
        return game_map, False

    except Exception as e:
        #Kaikkien muiden virhetilanteiden tulostus
        print("Error: ", e)
        return game_map, False

def win(current_game, player):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #Horizontal winner
    for row in current_game:
        #Row.count hakee countin vastaavalla arvolla ja sitä verrataan sitte row lenghtiin eli onko kaikki samaa arvio kyseisessä listassa
        if all_same(row):
            print(f"Player {player} win horizontaly")
            return True

    #Vertical winner
    #Range luo indexiarvon numerosta 0,1,2... ja len hakee pituuden joka tässä esimerkissä on 3 josta saadaan siis 0,1,2
    for col in range(len(current_game)):

        check = []
        #Loopataan rivit läpi jotta voidaan hakea jokaisen rivin samassa indexissä oleava arvo
        for row in current_game:
            check.append(row[col])

        #Checkataan että kaikkien check listalle lisättyjen arvojen arvo on sama joka tarkoittaa sitä että meillä on sarakkeessa vain yhtä numeroa
        #Checkaus tehty samalla tavalla kuin aikaisemmin eli check countilla haetaan arvojen määrä parametrisoidulla valuella ja tarkistetaan että arvo ei ole 0
        #Jos ehdot totetuu on voittaja löytynyt
        if all_same(check):
            print(f"Player {player} win verticaly")
            return True

    #Diagonal winner (Laskeva)
    check = []
    for index in range(len(current_game)):
        check.append(current_game[index][index])

    if all_same(check):
        print(f"Player {player} win horizontaly laskeva")
        return True

    #Diagonal winner (Nouseva)
    #Len haetaan pituus esimerkissä 3
    #otetaan 3 range 0,1,2
    #Reversed kääntää sen 2,1,0
    #enumeratella saadaan rivin index ja revertattu arvo
    #0,2 : 1,1 : 2:0

    #Voitaisiin käyttää myös Zip funtiota

    #cols = reversed(range(len(current_game)))
    #rows = range(len(current_game))
    
    #for x, y in zip(cols,rows):
    #    check.append(current_game[x][y])

    check = []
    for y, x in enumerate(reversed(range(len(current_game)))):
        check.append(current_game[x][y])

    if all_same(check):
        print(f"Player {player} win horizontaly nouseva")
        return True

    #Ei voittajaa
    return False


play = True
#Lista jota voidaan käydä läpi nextillä loputtomasti 
players = itertools.cycle([1,2])
while play:        
    game = []

    game_size = int(input("game size 1 - 9?"))

    #Käydään läpi range game_size = 3
    #eli tulee 0,1,2
    #sama homma kahdesti saadaan 3x3 grid
    for _ in range(game_size):
        row = []
        for _ in range(game_size):
            row.append(0)
        game.append(row)
    
    game_won = False

    #tulostetan tyhjä pelilauta
    game, _ = game_board(game_map=game,just_display=True)

    #Pelataan kunnes voittaja on löytynyt
    while not game_won:
        #Haetaan pelaaja players listalta nextillä
        current_player = next(players)

        played_correctly = False

        while not played_correctly:
            #Kysytään käyttäjältä pelattava paikka
            column_choice_answer = input(f"Player {current_player}, What column do you want to play ({[(i) for i in range(game_size)]}): ")
            row_choice_answer = input(f"Player {current_player},What row do you want to play {[(i) for i in range(game_size)]}): ")
            try:
                column_choice = int(column_choice_answer)
                row_choice = int(row_choice_answer)

                #Päivitetään pelikenttä
                game, played_correctly = game_board(game_map=game, player=current_player, row=row_choice, column=column_choice)
            except ValueError:
                print("Not valid value, try again ?")

        if win(game, current_player):
            game_won = True

            again = input("Wanna play again ? (y/n)")
            if again.lower() == "y":
                print("Restarting....")
            elif again.lower() == "n":
                print("Bye, game ended")
                play = False
            else:
                print("Not valid answer")
                play = False
            


