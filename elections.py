# ===== 1. DONNÉES (S45) =====
# A : lireUnCandidat, lireListeCandidats, affichePrefs
# B : genererUnVotant, genererListeVotants, programme principal

# ===== 1. DONNÉES (S45) - partie A =====

def lireUnCandidat(cands): #cands est une liste de noms des candidats qui ont déja été choisis
    #Demande un nom de candidat jusqu'à ce qu'il soit non vide et absent de cands, puis le renvoie.
    nom = input("Nom du candidat : ")
    while nom == "" or nom in cands:
        nom = input("Nom vide ou déjà saisi, recommencez : ")
    return nom


def lireListeCandidats(n):
    #Crée et renvoie une liste de n noms de candidats non vides et tous différents.
    cands = []
    for i in range(n):
        cands.append(lireUnCandidat(cands))
    return cands


def affichePrefs(prefs, cands, v):
    #Affiche les noms des candidats dans l'ordre de préférence du votant numéro v.
    texte = "Prefs du votant " + str(v) + " :"
    for c in prefs[v]:
        texte += " " + cands[c] + " ;"
    print(texte)

# ===== 2. SCRUTIN MAJORITAIRE (S46) =====
# A : compterVoix, gagnant, scrutinMaj1Tour





# B : compterVoixSel, deuxPremiers, scrutinMaj2Tours

# ===== 3. VOTE ALTERNATIF ET BORDA (S47) =====
# A : perdant, voteAlternatif
# B : compterPoints, voteBorda

# ===== 4. TESTS ET ANALYSE (S48) =====
# A : compterBulletins, afficheClassement
# B : tests automatisés (3.3)

# ===== 5. STATISTIQUES (S49) =====
# A : mesElecteurs, genererAges, genererGenres, statsElectorat
# B : graphiques matplotlib

