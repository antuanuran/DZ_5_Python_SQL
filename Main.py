from Client import create_db, add_clients, add_phones, update_client, remove_phone
import psycopg2 as pg


conn = pg.connect("dbname=Home_5 user=postgres password=postgres")
create_db(conn)

add_phones(conn, "МТС", "8-916-272-06-58")
add_phones(conn, "Билайн", "8-908-252-06-59")

add_clients(conn, "Python", "Ураноvv_python", "antoha@mail.ru", 1)
add_clients(conn, "Python", "Иванов_python", "ivan@mail.ru", 2)
add_clients(conn, "Python", "Петров_python", "petrov@mail.ru", 1)

update_client(conn, "SQL", "Доржиев", "Почта", "2", 1)

remove_phone(conn, 2)












