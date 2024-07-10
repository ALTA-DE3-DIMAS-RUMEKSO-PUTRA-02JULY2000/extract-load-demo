from google.cloud import bigquery
# import os


def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, rows_to_insert)
    if errors:
        print('Encountered errors while inserting rows: {}'.format(errors))
    else:
        print('Successfully insert data')


project_id = 'project-428209'
table_id = f'{project_id}.Project_MasGal.my_table'
rows_to_insert = [
    (1, 'Phred Phlyntstone', '2023-11-10 08:00:00'),
    (2, 'Wylma Phlyntstone', '2023-11-10 09:00:00'),
    (3, 'Wylma', '2023-11-10 10:00:00'),
    (4, 'Phlyntstone', '2023-11-10 11:00:00'),
    (5, 'maPhlyn', '2023-11-10 12:00:00')
]
write_to_bigquery(table_id, rows_to_insert)