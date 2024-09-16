def stableMatching(n, menPreferences, womenPreferences):
    unMarriedMen = list(range(n))
    manSpouse = [None] * n
    womanSpouse = [None] * n
    nextManChoice = [0] * n

    while unMarriedMen:
        he = unMarriedMen[0]
        hisPreferences = menPreferences[he]
        she = hisPreferences[nextManChoice[he]]
        herPreferences = womenPreferences[she]
        currentHusband = womanSpouse[she]

        if currentHusband is None:
            manSpouse[he] = she
            womanSpouse[she] = he
            unMarriedMen.pop(0)
        else:
            if herPreferences.index(he) < herPreferences.index(currentHusband):
                manSpouse[he] = she
                womanSpouse[she] = he
                manSpouse[currentHusband] = None
                unMarriedMen[0] = currentHusband
        nextManChoice[he] += 1

    return manSpouse

# Teste
print(stableMatching(1, [[0]], [[0]]) == [0])
print(stableMatching(2, [[0,1], [1,0]], [[0,1], [1,0]]) == [0, 1])
