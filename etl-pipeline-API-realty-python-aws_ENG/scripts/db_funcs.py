import pandas as pd


def insert_into_mysql(cursor, df, table):
    record = tuple(df.to_records(index=False))
    for item in range(len(df)):
        
        query = f'''
                INSERT INTO {table} VALUES {record[item]};
        '''

        cursor.execute(query)
        

