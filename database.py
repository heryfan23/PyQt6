import sqlite3

creation_base = sqlite3.connect("base.db")

sql_2 = "ALTER TABLE personnels RENAME TO personnels_2"

creation_table = """CREATE TABLE IF NOT EXISTS personnels(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    pseudo VARCHAR (50) NOT NULL UNIQUE,
    age INTEGER ,
    contact TEXT,
    email TEXT NOT NULL UNIQUE,
    date DATE NOT NULL,
    password TEXT NOT NULL CHECK(length(password) >= 8),
    sexe TEXT NOT NULL,
    images TEXT NOT NULL,
    nationalites TEXT NOT NULL,
    postes_id INTEGER,
    matricule VARCHAR(50),
    FOREIGN KEY (postes_id) REFERENCES postes(id)
    )"""

req_3 = "INSERT INTO personnels(id,nom,pseudo,age,contact,email,date,password,sexe,images,nationalites,postes_id,matricule) SELECT * FROM personnels_2"

req_4 = "DROP TABLE personnels_2"

cursor = creation_base.cursor()
cursor.execute(req_4)
creation_base.commit()
creation_base.close()

sql = "ALTER TABLE postes RENAME TO postes_pers"

creation_poste = """CREATE TABLE IF NOT EXISTS postes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_poste VARCHAR(100),
    description TEXT
)"""

# req_2 = "INSERT INTO postes(id,nom_poste,description) SELECT id, nom_poste,description FROM postes_pers"
effacer = "DROP TABLE postes_pers"


ajout_1 = "ALTER TABLE personnels ADD COLUMN postes_id INTEGER"
ajout_2 = "ALTER TABLE personnels ADD COLUMN matricule VARCHAR(50)"

ajout_3 = "ALTER TABLE personnels ADD FOREIGN KEY (postes_id) REFERENCES postes(id)"

# cursor.execute(ajout_3)
# creation_base.commit()
# creation_base.close()

