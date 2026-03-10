cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)