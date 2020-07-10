from lib.sqlframe import SQL

dados = [
    ('Anastácio', '997-164-750'),
    ('Maria', '123-421-123'),
    ('Cassiano', '321-567-234'),
    ('Ana', '890-765-564')
]

obj = SQL("agenda")

# CREATE
obj.create("CREATE TABLE agenda(nome TEXT, telefone TEXT)")

# INSERT
obj.insert("INSERT INTO agenda(nome, telefone) VALUES(?,?)", dados)
obj.commit()

# SELECT
resultados = obj.select("SELECT * FROM agenda")

obj.close()

for resultado in resultados:
    print("Nome: %s\nTelefone: %s\n\n" %(resultado))
