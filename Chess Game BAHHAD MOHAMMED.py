' BAHHAD MOHAMMED 1TSI2 '
' CHESS GAME '


def deplacer(piece):
    ''' permet de donner les positions accessibles par la pièce 
    '''
    nm,l,ch = piece[0],piece[2],piece[3]
    alph = ['a','b','c','d','e','f','g','h']
    S = []
    k = alph.index(l)
    if  nm == 'R':
        L = [l]
        C = [ch]
        chp = int(ch)+1
        chm = int(ch)-1
        if chp <=8 : C.append(str(chp))
        if chm >0 : C.append(str(chm))
        if k+1 <8 : L.append(alph[k+1])
        if k-1 >=0 : L.append(alph[k-1])
        for c in L :
            for n in C :
                ps = c+n
                if ps != l+ch : S.append(ps)
    elif nm == 'D':
        for i in range(1,9):
            ps = l+str(i)
            if ps != l+ch : S.append(ps)
        for e in alph :
            ps = e+ch
            if ps != l+ch : S.append(ps)
        c = k
        n = int(ch)
        while True :
            c+=1
            n+=1
            if c<8 and n <=8 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c-=1
            n-=1
            if c>=0 and n>0 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c+=1
            n-=1
            if c<8 and n >0 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c-=1
            n+=1
            if c>=0 and n <=8 : S.append(alph[c]+str(n))
            else : break
    elif nm == 'T':
        for i in range(1,9):
            ps = l+str(i)
            if ps != l+ch : S.append(ps)
        for e in alph :
            ps = e+ch
            if ps != l+ch : S.append(ps)
    elif nm == 'F':
        c = k
        n = int(ch)
        while True :
            c+=1
            n+=1
            if c<8 and n <=8 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c-=1
            n-=1
            if c>=0 and n>0 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c+=1
            n-=1
            if c<8 and n >0 : S.append(alph[c]+str(n))
            else : break
        c = k
        n = int(ch)
        while True :
            c-=1
            n+=1
            if c>=0 and n <=8 : S.append(alph[c]+str(n))
            else : break
    elif nm == 'C':
        c = int(ch)
        if c+2 <=8 :
            if k+1 < 8 : S.append(alph[k+1]+str(c+2))
            if k-1 >=0 : S.append(alph[k-1]+str(c+2))
        if c-2 >0 :
            if k+1 < 8 : S.append(alph[k+1]+str(c-2))
            if k-1 >=0 : S.append(alph[k-1]+str(c-2))
        if k+2 <8 :
            if c+1 <= 8 : S.append(alph[k+2]+str(c+1))
            if c-1 > 0 : S.append(alph[k+2]+str(c-1))
        if k-2 >=0 :
            if c+1 <= 8 : S.append(alph[k-2]+str(c+1))
            if c-1 > 0 : S.append(alph[k-2]+str(c-1))
    elif nm == 'P':
        clr = piece[1]
        c = int(ch)
        if clr == 'B':
            if c+1 <=8 : S.append(l+str(c+1))
            if c == 2 : S.append(l+str(c+2))
        else :
            if c-1 >0 : S.append(l+str(c-1))
            if c == 7 : S.append(l+str(c-2))
    return S

def afficher(piece):
    ''' permet d'afficher la pièce dans l'échiquier et les positions accessibles par celle-ci
    '''
    nm,cl,l,ch = piece[0],piece[1],piece[2],piece[3]
    alph = ['a','b','c','d','e','f','g','h']
    k = alph.index(l)
    Ech = []
    for i in range(8):
        L = []
        for j in range(8):
            L.append('_')
        Ech.append(L)
    if nm == 'R':
        if cl == 'B': n=9812
        else : n =9818
    elif nm == 'D':
        if cl == 'B': n= 9813
        else : n = 9819
    elif nm == 'T':
        if cl == 'B': n=9814
        else : n = 9820
    elif nm == 'F':
        if cl == 'B': n=9815
        else : n = 9821
    elif nm == 'C':
        if cl == 'B': n=9816
        else : n = 9822
    elif nm == 'P':
        if cl == 'B': n= 9817
        else : n = 9823
    c = int(ch)
    Ech[8-c][k]=chr(n)
    Pos = deplacer(piece)
    for e in Pos :
        n,p = int(e[1])-1,alph.index(e[0])
        Ech[7-n][p] = 'x'
    return Ech
