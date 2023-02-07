import psycopg2 as pg


class Client:
    def __init__(self, dsn):
        self.dsn = dsn

    def create_db(self):
        conn = pg.connect(self.dsn)
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
    def add_phones(self, operator, number):
        self.operator = operator
        self.number = number
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        insert into phones (operator, number)
        values
        (%s,%s);
        """, (operator, number))
        conn.commit()

    # 2.Добавление клиента с телефоном
    def add_clients(self, first_name, last_name, email, phone_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_id = phone_id
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        insert into clients (firstname, lastname, email, phone_id)
        values
        (%s,%s,%s,%s);
        """, (first_name, last_name, email, phone_id))
        conn.commit()

    # 3.Изменение клиента
    def update_client(self, first_name, last_name, email, phone_id, id_client):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_id = phone_id
        self.id_client = id_client
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        update clients set  firstname=%s, lastname=%s, email=%s, phone_id=%s
        where clients.id =%s;
        """, (first_name, last_name, email, phone_id, id_client))
        conn.commit()

    # 4.Удаление телефона
    def remove_phone(self, id_client):
        self.id_client = id_client
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        update clients set phone_id=%s
        where clients.id =%s;
        """, (None, id_client))
        conn.commit()

    # 5. Удаление клиента
    def remove_client(self, id_client):
        self.id_client = id_client
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        delete from clients
        where clients.id =%s;
        """, id_client)
        conn.commit()

    # 6. Поиск клиента и вывод в новую таблицу Find
    def find_client(self, firstname, lastname, email, number):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.number = number
        conn = pg.connect(self.dsn)
        cur = conn.cursor()

        cur.execute("""
        insert into find (firstname, lastname, email, phone)
        select c.firstname, c.lastname, c.email, p.number from clients c
        join phones p on c.phone_id = p.id
        where c.firstname like %s or c.lastname like %s or c.email like %s or p.number like %s
        """, (firstname, lastname, email, number))
        conn.commit()





















