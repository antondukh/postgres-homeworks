"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='ghbdtn666')

with connect:
    with connect.cursor() as cursor:
        with open('north_data/customers_data.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                cursor.execute("insert into customers values (%s, %s, %s)", row)


with connect:
    with connect.cursor() as cursor:
        with open('north_data/employees_data.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                cursor.execute("insert into employees values (%s, %s, %s, %s, %s, %s)", row)

with connect:
    with connect.cursor() as cursor:
        with open('north_data/orders_data.csv', 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                cursor.execute("insert into orders values (%s, %s, %s, %s, %s)", row)
