import sqlite3

ADMIN_PASSWORD = "admin1234"


def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    conn.execute("DELETE FROM users WHERE id = " + user_id)
    conn.commit()


def make_token(user_id):
    import hashlib
    return hashlib.md5(str(user_id).encode()).hexdigest()
