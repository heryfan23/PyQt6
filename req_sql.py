import sqlite3


def Inserer_pers(nom, pseudo, age, contact, email, date, password, sexe, images, nationalites, matricule,postes_id):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "INSERT INTO personnels(nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,postes_id,matricule) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    valeur = (nom, pseudo, age, contact, email, date,
              password, sexe, images, nationalites,postes_id,matricule)
    
    cu.execute(sql, valeur)

    connection.commit()
    connection.close()


def affficher_pers():
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "SELECT id,nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,matricule FROM personnels"
    data = cu.execute(sql)
    res = data.fetchall()

    connection.close()

    return res

# print(affficher_pers())


def suppression(id):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "DELETE FROM personnels WHERE id = ?"
    cu.execute(sql, (id,))
    connection.commit()
    connection.close()


def modifier(id, nom, pseudo, age, contact, email, date, sexe, nationalites, matricule):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()

    sql = f"UPDATE personnels SET nom = ?,pseudo = ?,age = ?,contact = ?,email=?,date = ?,sexe = ?,nationalites = ?,matricule = ? WHERE id = {id}"

    val_modif = (nom, pseudo, age, contact, email,
                 date, sexe, nationalites, matricule)

    cu.execute(sql, val_modif)
    connection.commit()
    connection.close()


def faire_rechercher(mot):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()

    sql = "SELECT id,nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,matricule FROM personnels WHERE nom LIKE ? OR pseudo LIKE ? OR matricule LIKE ?"
    data = cu.execute(sql,(f"%{mot}", f"%{mot}",f"%{mot}"))
    
    res = data.fetchall()
    connection.close()
    return res

def inserer_postes(nom,description):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    
    sql = "INSERT INTO postes(nom_poste,description) VALUES (?,?)"
    valeur = (nom,description)
    
    cu.execute(sql,valeur)
    connection.commit()
    connection.close()
    
# inserer_postes("Informaticien","Postes Python")
# inserer_postes("Mecanicien","Specialises Moteur")

def prend_postes():
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    
    sql = "SELECT DISTINCT nom_poste FROM postes"
    
    data = cu.execute(sql)
    res = data.fetchall()
    connection.close()
    return res

# print(prend_postes())

def prend_idposte(nom_poste):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    
    sql = f"SELECT id FROM postes WHERE nom_poste = ?"
    
    nom = (nom_poste)
    
    data = cu.execute(sql,(nom,))
    resu = data.fetchone()
    
    connection.close()
    
    return resu

# print(prend_idposte("Mecanicien")[0])