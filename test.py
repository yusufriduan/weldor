leaderboard_file = "leaderboard.txt"
def read_leaderboard():
    with open(leaderboard_file, 'r') as f:
        return f.read()

leaderboard_contents = read_leaderboard()
print(leaderboard_contents)
q = input("Press enter to continue.")