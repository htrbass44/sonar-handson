import os
import sqlite3
import subprocess
import hashlib

# [問題1] ハードコードされた認証情報
DB_PASSWORD = "P@ssw0rd123"
API_KEY = "dummy-api-key-0123456789abcdef"


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # [問題2] SQLインジェクション（文字列連結でSQLを組み立て）
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def ping(host):
    # [問題3] コマンドインジェクション（shell=True に外部入力）
    return subprocess.call("ping -c 1 " + host, shell=True)


def calc(expression):
    # [問題4] eval による任意コード実行
    return eval(expression)


def hash_password(password):
    # [問題5] 弱いハッシュアルゴリズム
    return hashlib.md5(password.encode()).hexdigest()


def check_user(user):
    # [問題6] 未使用変数・冗長な比較（Code Smell）
    unused = 42
    if user == None:
        return False
    if user["active"] == True:
        return True
    else:
        return False


def read_config(path):
    # [問題7] ファイルを閉じていない／例外を握りつぶしている
    try:
        f = open(path)
        return f.read()
    except:
        pass
