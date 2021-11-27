import chess.pgn
import os.path
import json

pgn = open("./databases/lichess_db_standard_rated_2015-01.pgn")

def addOpening(player, opening):
    # Vérifier si le fichier du joueur existe
    path = './players/'
    path1 = path + player + ".json"
    # Vérifier si le chemin existe ou non
    if not os.path.exists(path1):
        fichier = open(path1, "a")
        fichier.write("{\"openings\" : []}")
        fichier.close()
    isBroke = False
    with open(path1, "r") as json_file:
        data = json.load(json_file)
        for parse in data['openings']:
            if parse["opening"] == opening:
                parse["nb"] = parse["nb"] + 1
                isBroke = True
                break
        if not isBroke:
            data['openings'].append({
                'opening': opening,
                'nb': 1
            })
    with open(path1, "w") as f:
        f.write(json.dumps(data))

print(" commencé !")
while True:
    # Récupérer une partie
    game = chess.pgn.read_game(pgn)
    if game is None:
        break

    # Récupérer noms joueurs + Opening
    opening = game.headers._others["Opening"]

    whitePlayer = game.headers._tag_roster["White"]
    if whitePlayer != "?":
        addOpening(whitePlayer, opening)

    blackPlayer = game.headers._tag_roster["Black"]
    if blackPlayer != "?":
        addOpening(blackPlayer, opening)