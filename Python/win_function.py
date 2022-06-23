

def is_win(player, opponent):
    #s > p, r > s, p > r
    #returt true if the player wins
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True
    return False
