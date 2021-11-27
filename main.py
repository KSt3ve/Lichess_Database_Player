f = open("databases/lichess_db_standard_rated_2013-01.pgn", "r")
for x in f:
    l = x.readline()
    # listed = []
    # for a in range(0, 10):
    #     listed = listed + [x]
    #     print(x, end='')
