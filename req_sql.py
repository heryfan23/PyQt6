import sqlite3

def Inserer_pers(nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,matricule):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "INSERT INTO personnels(nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,matricule) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    valeur = (nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,matricule)
    cu.execute(sql,valeur)

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
    cu.execute(sql,(id,))
    connection.commit()
    connection.close()
    
def modifier(id,nom,pseudo,age,contact,email,date,sexe,nationalites,matricule):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    
    sql = f"UPDATE personnels SET nom = ?,pseudo = ?,age = ?,contact = ?,email=?,date = ?,sexe = ?,nationalites = ?,matricule = ? WHERE id = {id}"
    
    val_modif = (nom,pseudo,age,contact,email,date,sexe,nationalites,matricule)
    
    cu.execute(sql,val_modif)
    connection.commit()
    connection.close()
    
    