import psycopg2


def connection():
	'''
	Tutorial reference from 
	http://www.postgresqltutorial.com/postgresql-python/connect/
	'''
	conn = psycopg2.connect(host="localhost",database="pythonprogrammingtutorial", user="postgres", password="Password1!")
	cur = conn.cursor()

	return cur,conn	