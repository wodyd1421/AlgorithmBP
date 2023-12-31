def solution(answers):
    n1=0
    n2=0
    n3=0
    for i in range(len(answers)):
        n1+=int(answers[i]==i%5+1)
        n2+=int(answers[i]==int(i%2==0)*2+int(i%2==1)*((i%8+1)/2+int(i%8!=1)))
        n3+=int(answers[i]==int(i%10==0)*3+int(i%10==2)+int(i%10==4)*2+int(i%10==6)*4+int(i%10==8)*5+int((i-1)%10==0)*3+int((i-1)%10==2)+int((i-1)%10==4)*2+int((i-1)%10==6)*4+int((i-1)%10==8)*5)
    N={1:n1,2:n2,3:n3}
    M=sorted(N.items(),key=lambda x:x[1],reverse=True)
    if M[0][1]!=M[1][1]:
        return [M[0][0]]
    elif M[0][1]!=M[2][1]:
        return [M[0][0],M[1][0]]
    else:
        return [M[0][0],M[1][0],M[2][0]]