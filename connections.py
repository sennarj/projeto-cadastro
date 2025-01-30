import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='funcionarios',
    port=3306

)

if __name__ == '__main__':
    db.criarTabela(
      nomeTabela='funcionarios',
      Colunas=['nome','cargo','departamento','email'],
      ColunasTipo=['VARCHAR(255)','VARCHAR(255)','VARCHAR(255)','VARCHAR(255)']
)
