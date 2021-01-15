turns=1
while 1>0:
    n=int(input())
    if n!=0:
        if turns>1:
            print("")
        bicolorable=0
        stats=[0]*n
        m=int(input())
        graph=[]
        for _ in range(n):
            graph.append([])
        while m > 0:
            x, y = map(int, input().split())
            graph[x].append(y)
            m=m-1
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if stats[i]==0:
                    stats[graph[i][j]]=1
                else:
                    stats[graph[i][j]]=0
        for u in range(len(graph)):
            for j in range(len(graph[u])):
                if stats[u]==stats[graph[u][j]]:
                    bicolorable=1
                    break
            if bicolorable==1:
                break
        if bicolorable==0:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
        turns=turns+1
    else:
        break
