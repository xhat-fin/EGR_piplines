from database import init_db, connect_db
import json
from datetime import datetime


def load_data_base_info(filename):
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
                    INSERT INTO base_info 
                    (
                        dfrom, dto, ngrn, vnrcrt, vnrlkv, nsi00208_nkscrt, nsi00208_nsi00208,
                        nsi00208_vnscrtp, nsi00211_nkvob, nsi00211_nsi00211, nsi00211_vnvobp, nsi00212_nkuz,
                        nsi00212_nsi00212, nsi00212_vnuzp, nsi00212CRT_nkuz, nsi00212CRT_nsi00212, nsi00212CRT_vnuzp,
                        nsi00212LKV_nkuz, nsi00212LKV_nsi00212, nsi00212LKV_vnuzp, nsi00219_nksost, nsi00219_nsi00219,
                        nsi00219_vnsostk, nsi00228_nkslkv, nsi00228_nsi00228, nsi00228_vnslkvp
                    ) 
                    VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s
                     );
                    """, (
                          client.get('dfrom'),
                          client.get('dto'),
                          client.get('ngrn'),
                          client.get('vnrcrt'),
                          client.get('vnrlkv'),
                          client.get('nsi00208.nkscrt'),
                          client.get('nsi00208.nsi00208'),
                          client.get('nsi00208.vnscrtp'),
                          client.get('nsi00211.nkvob'),
                          client.get('nsi00211.nsi00211'),
                          client.get('nsi00211.vnvobp'),
                          client.get('nsi00212.nkuz'),
                          client.get('nsi00212.nsi00212'),
                          client.get('nsi00212.vnuzp'),
                          client.get('nsi00212CRT.nkuz'),
                          client.get('nsi00212CRT.nsi00212'),
                          client.get('nsi00212CRT.vnuzp'),
                          client.get('nsi00212LKV.nkuz'),
                          client.get('nsi00212LKV.nsi00212'),
                          client.get('nsi00212LKV.vnuzp'),
                          client.get('nsi00219.nksost'),
                          client.get('nsi00219.nsi00219'),
                          client.get('nsi00219.vnsostk'),
                          client.get('nsi00228.nkslkv'),
                          client.get('nsi00228.nsi00228'),
                          client.get('nsi00228.vnslkvp'),
                    )
                )
                print(f"{en} - {client.get('ngrn')} - загружен")
            except Exception as e:
                print(f"Ошибка с клиентом УНП {client.get('ngrn', 'неизвестен')}: {e}")
                errors += 1

        conn.commit()
    print(f"Данные загружены. Количество ошибок: {errors}. Затрачено времени: {datetime.now() - now_date}")


load_data_base_info('base_info.json')
