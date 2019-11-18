x=[]
d = input("Souhaitez vous enregistrer un livre?(oui/non)")
if d == "oui":
    z = "e"
    while z != "non":
        n = input("insere titre")
        p = input("insere auteur")
        q = input("insere genre")
        r = int(input ("insere prix"))
        z = input("Voulez vous enregistrer un nouveau livre?")
        dict = {"titre":n, "auteur":p,"genre":q,"prix": r }
        x.append(dict)
print(x)
rc = input("Souhaitez vous recherher un livre ?(oui/non)")
rcc = input("Comment voulez vous rechercher votre livre? Par auteur,titre ou genre?")
if rcc == "auteur":
    rca = input("Quel est le nom de l'auteur?")
    rep = "a"
    i = 0
    while rep != rca:
        for i in x:
            rep = x[i]["auteur"]
            print(rep)

            print(i)
