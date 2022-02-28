import pandas as pd

def import_csv_in_chunks(size=10):
    '''
    Imports CSV file in chunks of a defined size
    '''
    chunk_num = 0
    for chunk_num, chunk in enumerate(pd.read_csv('accounts.csv',
                                                  chunksize=size,
                                                  iterator=True)):
        print(f"CHUNK {chunk_num}")
        for index, row in chunk.iterrows():
            print(f"{row['USER_ID']} {row['EMAIL']} {row['NAME']} {row['LASTNAME']}")

if __name__ == "__main__":
    import_csv_in_chunks()