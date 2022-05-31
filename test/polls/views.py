from django.shortcuts import render
from django.contrib.auth.models import User
from models import Booking
import mysql.connector

# Create your views here.

def auth_data():
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='localhost',
                                         password='root')
    return connection

def register(request):
    connection = auth_data()
    query = User.objects.raw('INSERT INTO user(name, surname, email, password) VALUES (%s, %s, %s, %s) '[User.u_name, User.u_surname, User.u_email, User.u_password])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def create_book(request):
    connection = auth_data()
    query = User.objects.raw('INSERT INTO booking(date, start, end, name, user_id) VALUES (%s, %s, %s, %s) '[Booking.date, Booking.start, Booking.end, Booking.name,request.id])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def modify(request):
    connection = auth_data()
    query = User.objects.raw("UPDATE booking SET date = ?, start = ?, end = ?, name_id = ? WHERE user_id = ${request.user_id}", Booking.date, Booking.start, Booking.end, Booking.name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def delete(request):
    connection = auth_data()
    query = User.objects.raw("DELETE FROM booking WHERE name = ${request.name}")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def show_book(request):
    connection = auth_data()
    query = User.objects.raw("SELECT * FROM booking WHERE user_id = ${request.user_id}")
    for p in query:
        print("%s %s %s %s" % (p.date, p.start, p.end, p.name))
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
