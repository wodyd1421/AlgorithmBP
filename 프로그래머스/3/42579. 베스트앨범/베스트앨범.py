def solution(genres, plays):
    gp={}
    gpl={}
    for i,g in enumerate(genres):
        try:
            gp[g]+=plays[i]
        except:
            gp[g]=0
            gp[g]+=plays[i]
    for i,g in enumerate(genres):
        try:
            gpl[g].append((plays[i],i))
        except:
            gpl[g]=[]
            gpl[g].append((plays[i],i))
    gp=sorted(gp.items(),key=lambda x:x[1],reverse=True)
    ans=[]
    for g,p in gp:
        pl=sorted(gpl[g],reverse=True)
        try:
            if pl[0][0]==pl[1][0]:
                if pl[0][1]<=pl[1][1]:
                    ans.append(pl[0][1])
                    ans.append(pl[1][1])
                else:
                    ans.append(pl[1][1])
                    ans.append(pl[0][1])
            else:
                ans.append(pl[0][1])
                try:
                    ans.append(pl[1][1])
                except:
                    pass
        except:
            ans.append(pl[0][1])
    return(ans)