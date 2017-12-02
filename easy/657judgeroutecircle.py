udlr = {'U':1,
        'D':-1,
        'R':1,
        'L':-1}

def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    '''
    #naive solution
    lr = 0
    ud = 0
    for move in list(moves):
        if move == 'U' or move == 'D':
            ud += udlr[move]
        elif move == 'R' or move == 'L':
            lr += udlr[move]
    if ud == 0 and lr == 0:
        return True
    return False
    '''
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

if __name__ == '__main__':
    print(judgeCircle('UDLRUUDDLRLRLRLRLRL'))
