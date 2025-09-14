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
                    INSERT INTO short_info (vn, vfn, vnaim, nksost, vnsostk, nsi00219, vfio, ngrn, dto, dfrom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """, (
                          client.get('vn'),
                          client.get('vfn'),
                          client.get('vnaim'),
                          client.get('nsi00219.nksost'),
                          client.get('nsi00219.vnsostk'),
                          client.get('nsi00219.nsi00219'),
                          client.get('vfio'),
                          client.get('ngrn'),
                          client.get('dto'),
                          client.get('dfrom')
                          )
                )
                print(f"{en} - {client.get('vfn')} - загружен")
            except Exception as e:
                print(f"Ошибка с клиентом УНП {client.get('ngrn', 'неизвестен')}: {e}")
                errors += 1

        conn.commit()
    print(f"Данные загружены. Количество ошибок: {errors}. Затрачено времени: {datetime.now() - now_date}")


load_data_short_info('short_info_not_duplicates.json')
