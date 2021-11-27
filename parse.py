import chess.pgn
import os.path
import json

pgn = open("./databases/lichess_db_standard_rated_2013-01.pgn")
a = 0
while True:
    a += 1
    # Récupérer une partie
    game = chess.pgn.read_game(pgn)
    if game is None:
        break

    # Récupérer noms joueurs + Opening
    whitePlayer = game.headers._tag_roster["White"]
    blackPlayer = game.headers._tag_roster["Black"]
    opening = game.headers._others["Opening"]

    # Vérifier si le fichier du joueur existe
    # path = './players/'
    # path = path + whitePlayer
    # # Vérifier si le chemin existe ou non
    # if os.path.exists(path):
    #     print("Chemin ", path, " existe")
    # else:
    #     print("Chemin ", path, " n'existe pas")

    path = './players/'

    #  White player
    if whitePlayer != "?":
        path1 = path + whitePlayer + ".txt"
        fichier = open(path1, "a")
        fichier.write(opening + '\n')
        fichier.close()

    #  Black player
    if blackPlayer != "?":
        path2 = path + blackPlayer + ".txt"
        fichier = open(path2, "a")
        fichier.write(opening + '\n')
        fichier.close()

    #Si exite, on ajoute l'opening

    #Sinon on créé le fichier + on ajoute l'opening



print()
