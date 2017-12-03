def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    roundlist = []
    sums = 0
    for rounds in ops:
        if rounds == 'C':
            sums -= roundlist[-1]
            del roundlist[-1]
        else:
            if rounds == 'D':
                roundlist.append(roundlist[-1]*2)
            elif rounds == '+':
                roundlist.append(roundlist[-1] + roundlist[-2])
            else:
                roundlist.append(int(rounds))
            sums += roundlist[-1]
    return sums

if __name__ == '__main__':
    print(calPoints(["5","-2","4","C","D","9","+","+"]))
