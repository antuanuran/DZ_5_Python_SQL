from Client import create_db, add_clients, add_phones, update_client, remove_phone, remove_client, find_client
import psycopg2 as pg


conn = pg.connect("dbname=Home_5 user=postgres password=postgres")
create_db(conn)

add_phones(conn, "МТС", "8-916-272-06-66")
add_phones(conn, "Билайн", "8-908-252-06-55")

add_clients(conn, "Уранов", "Антон", "antoha@mail.ru", 2)
add_clients(conn, "Иванов", "Денис", "ivan@mail.ru", 2)
add_clients(conn, "Петров", "Женя", "petrov@mail.ru", 1)

update_client(conn, "Уранов 2", "Антон 2", "Почта 2", "2", 2)

remove_phone(conn, 1)

remove_client(conn, "1")

find_client(conn, "УраноЖ", "", "petrov@mail.ru", "")


















