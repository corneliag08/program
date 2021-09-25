n=int(input('Dati numarul de elemente din vector='))
z=[]
print('Introduceti ',n,'elemente pentru vectorul creat')

if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        z.extend([x])
    q=z.copy()
    print(z)
    print('a)Afiseaza pe ecran componentele tabloului la un interval de 5 pozitii:',z[::5])
    print('b)Afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator:',z[::-1])
    c=sorted(z)
    c.sort(reverse=True)
    print('c)Sorteaza componentele in ordine descrescatoare:',c)
    d=[]
    for i in range(0,len(z)):
        if z[i]%2==0:
            n=z[i]
            d.extend([n])
    print('d)Afiseaza pe ecran doar componentele pare:',d)
    if len(d)>0:
        print('e)Afiseaza pe ecran media aritmetica a componentelor pare:',sum(d)/len(d))
    f=[]
    for i in range(0,len(z)):
        if z[i]%2!=0:
            h=z[i]
            f.extend([h])
    print('f)Afiseaza pe ecran doar componentele impare:',f)
    x=eval(input('x= '))
    y=eval(input('y= '))
    g=[]
    for i in range(0,len(z)):
        if z[i]>x and z[i]%y!=0:
            k=z[i]
            g.extend([k])
    print('g)Afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y',g)
    h=[]
    for i in range(0,len(z)):
        if z[i]>x and z[i]<y:
            l=z[i]
            h.extend([l])
    print('h)Afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y:',h)
    print("i)Afişează pe ecran poziţiile (indicii) componentelor impare negative;")
    w=[]
    for elemi in z:
        if elemi<0 and elemi%2!=0:
            elemi=z.index(elemi)
            w.extend([elemi])
    print(w)
    print(f'j) Afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative\n {n}')
    for i in range(0,len(z)):
        if (z[i] >9 and z[i]<100) or (z[i]>-100 and z[i] <-9):
            print(i)
    k = z.copy()
    k[0] = min(z)
    print(f'k) Inlocueste prima componenta a tabloului cu valoare minima din tabloul respectiv:\n {k}')
    l = z.copy()
    l[l.index(min(l))] = z[0]
    print(f'l) Inlocueste componenta cu valoare minima din tabloul respectiv cu prima valoare a tabloului:\n {l}')
    print("m)	Creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;")
    print(d)
    print("n)Creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;")
    newlist=[]
    for divtrei in q:
        if divtrei%3==0:
            newlist.extend([divtrei])
    print(newlist)
    print("o) Creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.")
    dvzori3=[]
    def divisors(num):
        result = []
        for v in range(1, num//2 + 1):
            if num % v == 0:
                result.append(v)
        result.append(num)
        return result
    for dvzori3 in z:
        if len(divisors(dvzori3))>=4:
            dvzori3.extend([dvzori])
    print(dvzori3)     
else:
         print("Numarul elementelor trebuie sa fie între 0 și 10 ")