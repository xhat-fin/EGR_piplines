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
                    INSERT INTO address_info (
                        vtels, vnsfull, vregion, vpom, 
                        nsi00226, vdistrict, vnp, vntnpk, nkvpom, vkorp,
                        dfrom, vntulk ,vdom, vemail, nkstran, vfax, 
                        nsi00234, nindex, nktpom, vntpomk, vulitsa, 
                        nsi00201, vnstranp, vadrprim, dto, vsite, 
                        ngrn, objectnumber, nsi00202, nsi00227,
                        cact, nksoato, nktnp, nktul, vnvpom, nsi00239
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s
                        );
                    """, (

                        client.get('vtels'),
                        client.get('nsi00202.vnsfull'),  # vnsfull
                        client.get('vregion'),
                        client.get('vpom'),

                        client.get('nsi00226.nsi00226'),  # nsi00226
                        client.get('vdistrict'),
                        client.get('vnp'),
                        client.get('nsi00239.vntnpk'),  # vntnpk
                        client.get('nsi00234.nkvpom'),  # nkvpom
                        client.get('vkorp'),

                        client.get('dfrom'),
                        client.get('nsi00226.vntulk'),  # vntulk
                        client.get('vdom'),
                        client.get('vemail'),
                        client.get('nsi00201.nkstran'),  # nkstran
                        client.get('vfax'),

                        client.get('nsi00234.nsi00234'),  # nsi00234
                        client.get('nindex'),
                        client.get('nsi00227.nktpom'),  # nktpom
                        client.get('nsi00227.vntpomk'),  # vntpomk
                        client.get('vulitsa'),

                        client.get('nsi00201.nsi00201'),  # nsi00201
                        client.get('nsi00201.vnstranp'),  # vnstranp
                        client.get('vadrprim'),
                        client.get('dto'),
                        client.get('vsite'),

                        client.get('ngrn'),
                        client.get('nsi00202.objectnumber'),  # objectnumber
                        client.get('nsi00202.nsi00202'),  # nsi00202
                        client.get('nsi00227.nsi00227'),  # nsi00227

                        client.get('cact'),
                        client.get('nsi00202.nksoato'),  # nksoato
                        client.get('nsi00239.nktnp'),  # nktnp
                        client.get('nsi00226.nktul'),  # nktul
                        client.get('nsi00234.vnvpom'),
                        client.get('nsi00239.nsi00239')
                    )
                )
                print(f"{en} - {client.get('ngrn')} - загружен")
            except Exception as e:
                print(f"Ошибка с клиентом УНП {client.get('ngrn', 'неизвестен')}: {e}")
                errors += 1

        conn.commit()
    print(f"Данные загружены. Количество ошибок: {errors}. Затрачено времени: {datetime.now() - now_date}")


load_data_short_info('address_info_not_duplicates.json')
