from django.shortcuts import render
from .models import sql_human_Persons
import simplejson as json
import json
from django.http import JsonResponse

#to get data in front end table from sql server 
import pyodbc
def dispsqldata(request):
	conn=pyodbc.connect('Driver={sql server};'
						 'Server=LAPTOP-6ESE1JO3;'
						 'Database=master;'
						 'Trusted_Connection=yes;')
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM human.Persons')
	result=cursor.fetchall()
	#below code connect this file and models.py class
	return render(request,'BasicApp/table_sql.html',{'sql_human_Persons':result}) #huamn_persons is class in models.py

#API mainpage
def API_mainpage(request):
	return render(request,'BasicApp/API.html')

#API Get request
def GET_sql(request):
	conn=pyodbc.connect('Driver={sql server};'
						 'Server=LAPTOP-6ESE1JO3;'
						 'Database=master;'
						 'Trusted_Connection=yes;')
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM human.Persons')
	data=[]
	rows = cursor.fetchall()
	for row in rows:
	    data.append({
	    	'Persons_id': row[0],
	    	'city' : row[1],
	    	'Persons_name': row[2],
	    	'assets': row[3],
	    	'is_alien': row[4],
	    	'age': row[5],
	    	'month_expense': row[6],
	    	'discount': row[7],
	    	'email': row[8],
	    	'active': row[9],
	    	'order_date': row[10]
	    })
	return JsonResponse({'human_Persons':data}, status=200)

#API POST request
def post_Insertsql(request):

	if (request.method == 'POST'):
		data = json.loads(request.body)  #for payload
		#d = request.POST.get('Persons_id')

	Persons_id = data['Persons_id']
	city = data['city']
	Persons_name = data['Persons_name']
	assets = data['assets']
	is_alien = data['is_alien']
	age = data['age']
	month_expense = data['month_expense']
	discount = data['discount']
	email = data['email']
	active = data['active']
	order_date = data['order_date']

	conn=pyodbc.connect('Driver={sql server};'
						 'Server=LAPTOP-6ESE1JO3;'
						 'Database=master;'
						 'Trusted_Connection=yes;')
	cursor=conn.cursor()
	cursor.execute("SET IDENTITY_INSERT human.Persons OFF INSERT INTO human.Persons (city,Persons_name,assets,is_alien,age,month_expense,discount,email,active,order_date) values(?,?,?,?,?,?,?,?,?,?)",(city,Persons_name,assets,is_alien,age,month_expense,discount,email,active,order_date))
	conn.commit()

	return JsonResponse({'key':'data loaded'}, status=200)

#API UPDATE request
def post_Updatesql(request):

	if (request.method == 'POST'):
		data = json.loads(request.body)  #for payload

	Persons_id = data['Persons_id']
	city = data['city']
	Persons_name = data['Persons_name']
	assets = data['assets']
	is_alien = data['is_alien']
	age = data['age']
	month_expense = data['month_expense']
	discount = data['discount']
	email = data['email']
	active = data['active']
	order_date = data['order_date']

	conn=pyodbc.connect('Driver={sql server};'
						 'Server=LAPTOP-6ESE1JO3;'
						 'Database=master;'
						 'Trusted_Connection=yes;')
	cursor=conn.cursor()
	cursor.execute("UPDATE human.Persons SET CITY=(?) WHERE Persons_id=(?)",(city,Persons_id))
	conn.commit()

	return JsonResponse({'key':'data loaded'}, status=200)

#API DELETE request
def post_Deletesql(request):

	if (request.method == 'POST'):
		data = json.loads(request.body)  #for payload

	Persons_id = data['Persons_id']
	city = data['city']
	Persons_name = data['Persons_name']
	assets = data['assets']
	is_alien = data['is_alien']
	age = data['age']
	month_expense = data['month_expense']
	discount = data['discount']
	email = data['email']
	active = data['active']
	order_date = data['order_date']

	conn=pyodbc.connect('Driver={sql server};'
						 'Server=LAPTOP-6ESE1JO3;'
						 'Database=master;'
						 'Trusted_Connection=yes;')
	cursor=conn.cursor()
	cursor.execute("Delete from human.Persons WHERE Persons_id=(?)",(Persons_id))
	conn.commit()

	return JsonResponse({'key':'data loaded'}, status=200)

