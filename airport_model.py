
import mysql.connector
import configuration as c
import airport_controller as cnt
import airport_view as v

def clicked1():
    cursor = cnx.cursor()
    
    query = ("SELECT city, country, latitude, longitude FROM airports "
             "WHERE latitude BETWEEN %s AND %s AND longitude BETWEEN %s AND %s")
    
    cursor.execute(query, (float(v.min_lat.get()), float(v.max_lat.get()), float(v.min_lon.get()), float(v.max_lon.get())))
    
    lst = []
    for (city, country, latitude, longitude) in cursor:
      lst.append((city, country, latitude, longitude))
    
    cursor.close()
    global t
    if t is not None:
        t.destroy(v.bottom_frame)
    t = cnt.Table(v.bottom_frame, lst)


def clicked2():
    cursor = cnx.cursor()

    query = (f"SELECT  r.src_airport, ai.airport,  ai.city, ai.country, r.dst_airport, air.airport, air.city, air.country \
     FROM airports AS ai INNER JOIN routes AS r ON ai.iata=r.src_airport INNER JOIN airports AS air ON air.iata=r.dst_airport \
    WHERE ai.city LIKE '%{v.depart.get()}%' AND air.city LIKE '%{v.arr.get()}%'")


    cursor.execute(query)
    lst = []
    for (iata_d, airport_d, city_d, country_d, iata_a, airport_a, city_a, country_a) in cursor:
        lst.append((iata_d, airport_d, city_d, country_d, iata_a, airport_a, city_a, country_a))

    cursor.close()
    global t
    if t is not None:
        t.destroy(v.bottom_frame)
    t = cnt.Table(v.bottom_frame, lst)
    
t = None


cnx = mysql.connector.connect(user=c.user, password= c.password,
                              host=c.host,
                              database=c.database)


