import json
import psycopg2


db_info = {
    'database': 'info',
    'user': 'postgres',
    'password': 'Totem123',
    'host': 'localhost',
    'port': '5432'
}


def connect_db():
    connect = psycopg2.connect(**db_info)
    return connect


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS short_info(
                    id SERIAL PRIMARY KEY,
                    vn VARCHAR(1000), -- vn
                    vfn VARCHAR(1000), -- vfn
                    vnaim VARCHAR(1000), -- vnaim
                    nksost INTEGER, -- nksost
                    vnsostk VARCHAR(1000), -- vnsostk
                    nsi00219 VARCHAR(1000), -- nsi00219
                    vfio VARCHAR(1000), -- vfio если клиент ип, то будет заполненно, если нет то будет пусто
                    ngrn VARCHAR(20), -- ngrn УНП клиента
                    dto DATE, -- dto пока не понятно, что это
                    dfrom DATE -- dfrom это вроде бы дата регистрации клиента
                );
            """
        )

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS ved_info(
                    id SERIAL PRIMARY KEY,
                    ngrn VARCHAR(20), -- ngrn УНП клиента
                    cact VARCHAR(10), -- + и - в данных, пока не понятно что это, как будто бы актуальность записи
                    dto DATE, -- dto пока не понятно, что это
                    dfrom DATE, -- dfrom это вроде бы дата регистрации клиента
                    vkvdn VARCHAR(20), -- vkvdn код сферы деятельности
                    vnvdnp VARCHAR(300), -- vnvdnp наименование сферы деятельности
                    nsi00114 VARCHAR(50) -- nsi00114 какой-то код
                );
            """
        )

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS address_info(
                    id SERIAL PRIMARY KEY,
                    vtels VARCHAR(1000),
                    vnsfull VARCHAR(1000),
                    vregion VARCHAR(1000),
                    vpom VARCHAR(1000),
                    nsi00226 VARCHAR(1000),
                    vdistrict VARCHAR(1000),
                    vnp VARCHAR(1000),
                    vntnpk VARCHAR(1000),
                    nkvpom VARCHAR(1000),
                    vkorp VARCHAR(1000),
                    dfrom DATE,
                    vntulk VARCHAR(1000),
                    vdom VARCHAR(1000),
                    vemail VARCHAR(1000),
                    nkstran VARCHAR(1000),
                    vfax VARCHAR(1000),
                    nsi00234 VARCHAR(1000),
                    nindex VARCHAR(1000),
                    nktpom VARCHAR(1000),
                    vntpomk VARCHAR(1000),
                    vulitsa VARCHAR(1000),
                    nsi00201 VARCHAR(1000),
                    vnstranp VARCHAR(1000),
                    vadrprim VARCHAR(1000),
                    dto DATE,
                    vsite VARCHAR(1000),
                    ngrn VARCHAR(1000),
                    objectnumber VARCHAR(1000),
                    nsi00202 VARCHAR(1000),
                    nsi00227 VARCHAR(1000),
                    cact VARCHAR(1000),
                    nksoato VARCHAR(1000),
                    nktnp VARCHAR(1000),
                    nktul VARCHAR(1000),
                    vnvpom VARCHAR(1000),
                    nsi00239 VARCHAR(1000)
                );
            """
        )


def get_all_keys(dict_data):
    keys = []

    if isinstance(dict_data, dict):
        for key, value in dict_data.items():
            keys.append(key)
            keys.extend(get_all_keys(value))

    elif isinstance(dict_data, list):
        for item in dict_data:
            keys.extend(get_all_keys(item))

    return keys


def columns_uniq(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        columns = set(get_all_keys(data))
        return columns

