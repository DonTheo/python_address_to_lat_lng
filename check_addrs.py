import psycopg2 
from opencage.geocoder import OpenCageGeocode


# Connection to Posgresql
try:
    conn = psycopg2.connect("dbname='<your_db_name>' user='<your_user_name>' host='<serv_adr>' password='<password>'")
except:
    print ("Connection failed")

cur = conn.cursor()


# API KEY OpenCage
key = '<your api key>'
geocoder = OpenCageGeocode(key)


# SQL query 
cur.execute("<query to colect address from your db>")
rows = cur.fetchall()


# Address conversion -> lat, lng
list_pos = []
for elem in rows:
    if None in elem:
        pass
    else:
        try:
            results = geocoder.geocode(str(elem))
            pos = u'%f;%f' % (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
            list_pos.append(pos)
            print(pos + " " + str(elem))
        except:
            print('/!\ incorect address: ' + str(elem))

print("\n'pos' collection finished")