def create_db(conn) -> None:
    cur = conn.cursor()
    cur.execute("""
    drop table if exists phones cascade;
    drop table if exists clients cascade;
    drop table if exists find cascade;

    create table if not exists phones (
        id SERIAL primary key,
        operator varchar (60),       
        number varchar (60) unique
        );

    create table if not exists clients (
        id SERIAL primary key,
        firstname varchar (60) not null,
        lastname varchar (60) not null,
        email varchar (60) not null unique,
        phone_id integer references phones (id));

    create table if not exists find (
        id SERIAL primary key,
        firstname varchar (60) not null,
        lastname varchar (60) not null,
        email varchar (60) not null unique,
        phone varchar (60) not null unique
        );  
            """)
    conn.commit()


# 1.Добавление телефона
def add_phones(conn, operator, number) -> None:
    cur = conn.cursor()
    cur.execute("""
    insert into phones (operator, number) 
    values
    (%s,%s);
    """, (operator, number))
    conn.commit()


# 2.Добавление клиента с телефоном
def add_clients(conn, first_name, last_name, email, phone_id) -> None:
    cur = conn.cursor()
    cur.execute("""
    insert into clients (firstname, lastname, email, phone_id) 
    values
    (%s,%s,%s,%s);
    """, (first_name, last_name, email, phone_id))
    conn.commit()


# 3.Изменение клиента
def update_client(conn, first_name, last_name, email, phone_id, id_client):
    cur = conn.cursor()
    cur.execute("""
    update clients set  firstname=%s, lastname=%s, email=%s, phone_id=%s
    where clients.id =%s;
    """, (first_name, last_name, email, phone_id, id_client))
    conn.commit()


# 4.Удаление телефона
def remove_phone(conn, id_client):
    cur = conn.cursor()
    cur.execute("""
    update clients set phone_id=%s
    where clients.id =%s;
    """, (None, id_client))
    conn.commit()


# 5. Удаление клиента
def remove_client(conn, id_client):
    cur = conn.cursor()
    cur.execute("""
    delete from clients
    where clients.id =%s;
    """, id_client)
    conn.commit()


# 6. Поиск клиента и вывод в новую таблицу Find
def find_client(conn, firstname, lastname, email, number):
    cur = conn.cursor()
    cur.execute("""
    insert into find (firstname, lastname, email, phone)
    select c.firstname, c.lastname, c.email, p.number from clients c 
    join phones p on c.phone_id = p.id 
    where c.firstname like %s or c.lastname like %s or c.email like %s or p.number like %s 
    """, (firstname, lastname, email, number))
    conn.commit()



