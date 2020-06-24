import sqlite3
from sqlite3 import Error
import base64
import webbrowser


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def parse_table_schema(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()

    cur.execute("PRAGMA table_info({})".format("week5"))
    print(cur.fetchall())


def retrive_entry(conn, user_input):
    entry = None
    result = False

    if 1 <= int(id) <= 24:
        cur = conn.cursor()
        cur.execute("SELECT * FROM week5 WHERE id=?;", (int(id),))
        entry = cur.fetchall()
        result = True
    else:
        pass

    return entry, result


def update_entry(conn, city, country, id):
    cur = conn.cursor()
    cur.execute("UPDATE week5 set City=? where id=?", (city, int(id),))
    conn.commit()
    cur.execute("UPDATE week5 set Country=? where id=?", (country, int(id),))
    conn.commit()

    cur = conn.cursor()
    cur.execute("SELECT * FROM week5")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    conn = create_connection("week5.db")
    # parse_table_schema(conn)

    while True:
        id = input("Enter Option from 1 to 24 and Q to Quit Program: ")

        if id == 'q':
            break

        entry, result = retrive_entry(conn, id)

        if result:
            entry_url = base64.b64decode(entry[0][1])

            webbrowser.open_new(entry_url)

            city = input("Enter City Name: ")
            country = input("Enter Country Name: ")

            update_entry(conn, city, country, id)

    conn.close()