def check_anagram(S1, S2):
    temp1 = dict()
    temp2 = dict()
    for e in S1:
        if e not in temp1:
            temp1[e] = None
    for e in S2:
        if e not in temp2:
            temp2[e] = None
    #print(temp1,"\n",temp2)
    return temp1 == temp2


if __name__ == '__main__':
    S1 = "listen"
    S2 = "silent"
    print("Are {} and {} anagram? {}".format(S1, S2, check_anagram(S1, S2)))
