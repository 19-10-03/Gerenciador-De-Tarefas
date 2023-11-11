import psycopg2


# Função para conexão com o banco de dados
def get_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432",
    )
    return conn


# Criação da tabela
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Agenda (
            id SERIAL PRIMARY KEY,
            codigo_produto INT,
            nome_produto TEXT,
            preco FLOAT,
            preco_final FLOAT
        )
    """
    )
    conn.commit()
    cur.close()


create_table()
