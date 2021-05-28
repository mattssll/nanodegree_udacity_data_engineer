import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    i=0
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()
        i=i+1
        print(f"log: loaded table {i}")


def insert_tables(cur, conn):
    i=0
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
        i=i+1
        print(f"log: inserted table {i}")


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['DWH'].values()))
    cur = conn.cursor()
    print("log: inserting data from s3 to staging area in redshift")
    load_staging_tables(cur, conn)
    print("log: inserting data into DWH Tables")
    # insertind data into tables
    insert_tables(cur, conn)
    print("log: ETL is done")

    conn.close()


if __name__ == "__main__":
    main()
