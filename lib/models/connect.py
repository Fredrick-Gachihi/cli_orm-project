#lib/connect.py
import sqlite3

conn = sqlite3.connect("database/shop.db")


cursor = conn.cursor()
