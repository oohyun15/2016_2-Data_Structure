import itertools
def PuzzleSolve(k, S, U, puzzle, alphabets):
    UU=[]
    first=''
    second=''
    last=''
    for i in range(len(puzzle)):
        if puzzle[i] == '+':
            first = puzzle[:i-1]
        elif puzzle[i] == '=':
            second = puzzle[len(first)+3:i-1]
            last = puzzle[i+2:] #puzzle에서 얻은 단어
    if k==0: # S 리스트에 알파벳 배열 완료
        UU = [list(x) for x in itertools.combinations(U,len(S))] # U 리스트에서 S 리스트 개수만큼 숫자를 뽑음
        for j in range(len(UU)):
            first_num=''
            second_num=''
            last_num=''
            a_dict=dict()
            for i in range(len(S)):
                a_dict[S[i]] = str(UU[j][i])
            for i in range(len(first)):
                first_num += a_dict[first[i]]
            for i in range(len(second)):
                second_num += a_dict[second[i]]
            for i in range(len(last)):
                last_num += a_dict[last[i]]
            if int(first_num) + int(second_num) == int (last_num):
                print("Solution found.")
                print("{0:} + {1:} = {2:}".format(first_num, second_num, last_num))
    else:
        for i in range(k):
            temp = alphabets
            S.append(temp[i]) # 알파벳 철자 하나씩 S로 옮김
            temp = temp[:i] + temp[i+1:]
            PuzzleSolve(k-1, S, U, puzzle, temp)
            del S[-1]


if __name__ == '__main__':

    print("Started")

    #pot + pan = bib
    print("Calculating \t pot + pan = bib...")
    PuzzleSolve(7, [], [x for x in range(10)], "pot + pan = bib", "potanbi")

    #dog + cat = pig
    print("Calculating \t dog + cat = pig...")
    PuzzleSolve(8, [], [x for x in range(10)], "dog + cat = pig", "dogcatpi")

    #boy + girl = baby
    print("Calculating \t boy + girl = baby...")
    PuzzleSolve(8, [], [x for x in range(10)], "boy + girl = baby", "boygirla")

    print("Finished")
