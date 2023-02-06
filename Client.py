
def create_db(conn) -> None:
    cur = conn.cursor()
    cur.execute("""
    drop table if exists phones cascade;
    drop table if exists clients cascade;

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
