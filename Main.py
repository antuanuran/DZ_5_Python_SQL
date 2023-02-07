from Client import Client


# Переменные

dsn = "dbname=Home_5 user=postgres password=postgres"

operat = 'MTS'
operat2 = 'Beeline'

numb = '8-916-272-06-59'
numb2 = '8-960-222-00-58'

first_name = 'Уранов'
first_name2 = 'Иванов'
first_name3 = 'Петров'

last_name = 'Антон'
last_name2 = 'Денис'
last_name3 = 'Жора'

email = 'anton@ya.ru'
email2 = 'denis@ya.ru'
email3 = 'gora@ya.ru'

# Методы

client = Client(dsn)

client.create_db()

client.add_phones(operat, numb)
client.add_phones(operat2, numb2)

client.add_clients(first_name, last_name, email, 1)
client.add_clients(first_name2, last_name2, email2, 1)
client.add_clients(first_name3, last_name3, email3, 2)

client.update_client('Uranov', 'Anton', 'ura@ya.ru', 2, 2)

client.remove_phone(2)

client.remove_client('1')

client.find_client('Петров', '', '', '')























