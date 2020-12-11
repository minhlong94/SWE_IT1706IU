import sqlite3


def insert(connection, shop_id, shop_name):
    """Add a new shop to the database.

    Args:
        connection (sqlite3.Connection)
        shop_id (str)
        shop_name (str)
    """

    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")
    if not shop_name:
        raise TypeError("Argument 'shop_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Shop (shopID, shopName) VALUES (?,?)''', (shop_id, shop_name))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Shop WHERE shopID = ?''', (shop_id,))
    cur.execute('''DELETE FROM Shop WHERE shopID = ?''', (shop_id,))
    connection.commit()
    return removed


def search_by_id(connection, shop_id=0, show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Shop WHERE shopID = ?''', (shop_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Shop WHERE shopID = ?''', (shop_id,)).fetchall()


def search_by_name(connection, shop_name="", show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Shop WHERE shopName LIKE ?''', ('%' + shop_name + '%',)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Shop WHERE shopName LIKE ?''', ('%' + shop_name + '%',)).fetchall()


def get_all(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Shop''')
    return cur.fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (shopID) FROM Shop''')
    return cur.fetchone()[0]


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Shop LIMIT 0''')
    names = [i[0] for i in cur.description]
    return names
