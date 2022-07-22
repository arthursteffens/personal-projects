import pandas as pd


def insert_into_mysql(cursor, df, table):
    df = pd.DataFrame(df)
    rec = tuple(df.to_records(index=False))
    for item in range(len(df)):
        
        query = f'''
                INSERT INTO {table} VALUES {rec[item]};
        '''
 
        cursor.execute(query)
        

