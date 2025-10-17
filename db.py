import psycopg2
from parsing import product_list

connect = psycopg2.connect(
    host='localhost',
    user='postgres',
    database="db",
    password='1234'
)
cursor = connect.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE products (
    id SERIAL,
    Kampyuter_nomi VARCHAR(255),
    Image VARCHAR(255),
    Kampyuter_narxi VARCHAR(30),
    Kredit CHAR(255)
    )
    """)

    connect.commit()

create_table()

def insert_into(Kampyuter_nomi, Image, Kampyuter_narxi, Kredit):
    cursor.execute("""
    INSERT INTO products (Kampyuter_nomi, Image, Kampyuter_narxi, Kredit) VALUES (%s, %s, %s, %s)
    """, (Kampyuter_nomi, Image, Kampyuter_narxi, Kredit))

    connect.commit()

for product in product_list:
    insert_into(product["Kampyuter_nomi"], product["Image"], product["Kampyuter_narxi"], product["Kredit"])

print("Ma'lumot qo'shildi")
