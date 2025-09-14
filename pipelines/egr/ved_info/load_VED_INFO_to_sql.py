from database import init_db, connect_db
import json
from datetime import datetime


def load_data_short_info(filename):
    now_date = datetime.now()
    init_db()

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with connect_db() as conn, conn.cursor() as cur:
        errors = 0
        for en, client in enumerate(data, start=1):
            try:
                cur.execute(
                    """
                    INSERT INTO ved_info (ngrn, dfrom, dto, cact, vkvdn, vnvdnp, nsi00114) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, (
                          client.get('ngrn'),
                          client.get('dfrom'),
                          client.get('dto'),
                          client.get('cact'),
                          client.get('nsi00114.vkvdn'),
                          client.get('nsi00114.vnvdnp'),
                          client.get('nsi00114.nsi00114')
                          )
                )
                print(f"{en} - {client.get('ngrn')} - загружен")
            except Exception as e:
                print(f"Ошибка с клиентом УНП {client.get('ngrn', 'неизвестен')}: {e}")
                errors += 1

        conn.commit()
    print(f"Данные загружены. Количество ошибок: {errors}. Затрачено времени: {datetime.now() - now_date}")


load_data_short_info('ved_info_not_duplicates.json')
