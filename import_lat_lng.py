import psycopg2 
from opencage.geocoder import OpenCageGeocode


# Connection to Posgresql
try:
    conn = psycopg2.connect("dbname='your_db_name' user='your_user_name' host='serv_adr' password='password'")
except:
    print ("Connection failed")

cur = conn.cursor()


# API KEY OpenCage
key = '<your api key>'
geocoder = OpenCageGeocode(key)


# SQL query 
cur.execute("TRUNCATE TABLE  <table where data will be insert>;")
cur.execute("<query to colect address from your db>")
rows = cur.fetchall()


# Address conversion -> lat, lng and insert query
for elem in rows:
    if None in elem:
        pass
    else:
        try:
            # Address conversion -> lat, lng
            results = geocoder.geocode(str(elem))
            pos = u'%f;%f' % (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
            data = pos.split(";")
            
            # Insert query
            insert_query = "INSERT INTO <your table>(<collumns name>) Values (%s, %s)"
            data_to_insert = (data[0], data[1])
            cur.execute(insert_query, data_to_insert)
            conn.commit()

        except:
            print('/!\ incorect address: ' + str(elem))

print("\n'pos' collection finished")