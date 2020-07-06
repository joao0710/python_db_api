import cliente, cliente_repositorio

# try:
#     db.begin()
#     cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Marx', 28)")
#     cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Jose', 30)")
#     db.commit()
# except:
#     db.rollback()
#
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())

# print('conexão realizada com sucesso')
# cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Zacarias', 25)")
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())
# print(cursor.lastrowid)                      #lastrowid retorna o último id inserido

cliente = cliente.Cliente("Isaac", 17)
cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente)
cliente_repositorio.ClienteRepositorio.listar_clientes()

