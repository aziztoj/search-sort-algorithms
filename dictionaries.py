clubs = {
    'Man United': {
        'Bruno': {
            'Goals': 3,
            'Assists': 1,
            'Mins': 540
        },
        'Cunha':{
            'Goals': 1,
            'Assists': 2,
            'Mins': 496
        },
        'Sesko':{
            'Goals': 1,
            'Assists': 0,
            'Mins': 76
        }
    },
    'Liverpool': {
        'Isak': {
            'Goals':4,
            'Assists':0,
            'Mins':413
        },
        'Gakpo': {
            'Goals': 1,
            'Assists': 3,
            'Mins': 371
        },
        'Wirtz':{
            'Goals': 0,
            'Assists': 1,
            'Mins': 469
        }
    },
    'Chelsea':{
        'Palmer':{
            'Goals': 2,
            'Assists': 3,
            'Mins': 531
        },
        'Pedro':{
            'Goals': 5,
            'Assists': 3,
            'Mins': 432
        },
        'Rogers':{
            'Goals': 4,
            'Assists': 1,
            'Mins': 523
        }
    }
}
# print(clubs['Chelsea']['Palmer']['Goals'])
def table():
    for club,players in clubs.items():
        print(club)
        for player,stats in players.items():
            print(player+":")
            for stat, value in stats.items():
                print("     ",stat+":",value)
        print()

# name = input("Which player do you want to look up? ")
# found = False
# for players in clubs.values():
#     if players.get(name) != None:
#         print(players.get(name))
#         found = True
#         break
# if found == False:
#     print(name,"was not found")
    
# found = False
# team = input("Enter the club you want to search: ")
# for club,players in clubs.items():
#     if club == team:
#         found = True
#         for player,stats in players.items():
#             print(player+":")
#             for stat, value in stats.items():
#                 print("     ",stat+":",value)
#         print()
# if found == False:
#     print(team,"was not found")
# max = 0
# for club,players in clubs.items():
#     for player,stats in players.items():
#         if clubs[club][player]['Goals'] > max:
#             max = clubs[club][player]['Goals']
#             name2 = player
# print(name2,"is the top scorer with",max)

# def update(extragoals,updateplayer):
#     for club,players in clubs.items():
#         for player,stats in players.items():
#             if player == updateplayer:
#                 clubs[club][player]['Goals'] += extragoals

# updateplayer = input("Which player's goal count do you want to change?: ")
# extragoals = input("How many extra goals did he score?: ")
# update(extragoals,updateplayer)
# name = input("Which player do you want to look up? ")
# found = False
# for players in clubs.values():
#     if players.get(name) != None:
#         print(players.get(name))
#         found = True
#         break
# if found == False:
#     print(name,"was not found")

# def addplayer():
#     clubname = input("Enter his current club name: ")
#     player = input("Enter his name")
#     goalnum = input("How many goals did he score?: ")
#     assistnum = input("How many assists does he have?: ")
#     minsnum = input("How many mins did he play so far?: ")
#     clubs[clubname][player] = {
#         'Goals' : goalnum,
#         'Assists' : assistnum,
#         'Mins' : minsnum
#     }

# def deleteplayer():
#     name = input("Which player do u want to erase?")
#     for club,players in clubs.items():
#         for player in players.keys():
#             if player == name:
#                 del clubs[club][player]
#                 break
# addplayer()
# deleteplayer()

# table()

def app():
    usercontinue = True
    while usercontinue:
        playername = input("Enter a player name: ").capitalize()
        found = False
        for players in clubs.values():
            if players.get(playername) != None:
                print(players.get(playername))
                found = True
                break
        if found == False:
            print(playername,"was not found")
        cont = input("Do you want to stop? y/n: ").lower()
        if cont == 'y':
            usercontinue = False

app()