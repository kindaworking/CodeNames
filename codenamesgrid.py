import random

def randomize_starting_team():
    _possible_teams = ["red     ","blue    "]
    # Starting_team = random.sample(_possible_teams,1)
    random.shuffle(_possible_teams)
    starting_team = _possible_teams[0]
    second_team = _possible_teams[1]
    return starting_team,second_team

def randomized_board(starting_team, second_team):
    default_board = []
    board_paired = {}
    # Set up a blank board numbered 1 - 25
    default_board = list(range(1,26))
    

    # Pull Random Tiles from the bag
    random_tiles = random.sample(default_board,25)
    starting_team_tiles = random_tiles[:9]
    second_team_tiles = random_tiles[9:17]
    assassin_tile = random_tiles[17]
    innocent_tiles = random_tiles[18:]

    # Use a dictionary paid to assign each key (1-25) a value (tile type)
    for x in default_board:
        if x in starting_team_tiles:
            board_paired[x] = starting_team
        elif x == assassin_tile:
            board_paired[x] = "assassin"
        elif x in innocent_tiles:
            board_paired[x] = "innocent"
        elif x in second_team_tiles:
            board_paired[x] = second_team
    return board_paired
            

def print_board(board_layout):
    print("-"*69)
    x = 1
    # This while loop is iterating through all the keys (tile location) in the dictionary and printing the value (tile type)
    while x in board_layout:
        # These if statements are what drops the tiles to the next line
        if x == 6:
            print("")
            print("-"*69)
        if x == 11:
            print("")
            print("-"*69)
        if x == 16:
            print("")
            print("-"*69)
        if x == 21:
            print("")
            print("-"*69)

        # These if statements group the tiles by their rows, seperating tiles by ||
        if x < 6:
            print("| ",board_layout [x] + " | ", end="")
            x = x + 1
        elif x > 5 and x < 11:
            print("| ",board_layout [x] + " | ", end="")
            x = x + 1
        elif x > 10 and x < 16:
            print("| ",board_layout [x] + " | ", end="")
            x = x + 1
        else:
            print("| ",board_layout [x] + " | ", end="")
            x = x + 1
    print("")
    print("-"*69)



def main():
    starting_team, second_team = randomize_starting_team()
    print("The starting team is: " + str(starting_team))
    print("The second team is: " + str(second_team))
    board_layout = randomized_board(starting_team, second_team)
    print_board(board_layout)
        
main()
