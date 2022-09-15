
import mysql.connector;
from claves import clave;




class Carreras:

    def __init__(self):
        self.cnn = mysql.connector.connect(host = "localhost", user= "root", passwd =clave, database = "pi");

    
    
    def consulta(self):
        # cur es el cursor siempre que quiera acceder a la BD que es el bojeto cnn(conección)
        cur = self.cnn.cursor()
        #execute(): ejecutar una consulta
        cur.execute("SELECT * FROM pi.circuits;")
        #fetchall(): es para recuperar todos las filas de la BD, es una tupla
        datos = cur.fetchall()
        cur.close()    
        return datos
    def consultaAño(self):
            # cur es el cursor siempre que quiera acceder a la BD que es el bojeto cnn(conección)
        cur = self.cnn.cursor()
        #execute(): ejecutar una consulta
        cur.execute("SELECT Year,count(Year) FROM pi.races group by Year order by Year desc limit 1 ; ")
        #fetchall(): es para recuperar todos las filas de la BD, es una tupla
        datos = cur.fetchone()
        cur.close()    
        aux= ""
        aux = datos
        return aux
   
    
    def consultacamp(self):
            # cur es el cursor siempre que quiera acceder a la BD que es el bojeto cnn(conección)
        cur = self.cnn.cursor()
        #execute(): ejecutar una consulta
        cur.execute("SELECT count(A.Position), B.Name from results A inner join drivers B on A.`Driver Id` = B.`Driver Id` where A.position = 1 group by B.Name limit 1;")
        #fetchall(): es para recuperar todos las filas de la BD, es una tupla
        datos = cur.fetchone()
        cur.close()    
        
        aux = ""
        aux=datos
        return aux
    
    def consultaCircuito(self):
            # cur es el cursor siempre que quiera acceder a la BD que es el bojeto cnn(conección)
        cur = self.cnn.cursor()
        #execute(): ejecutar una consulta
        cur.execute("SELECT count(A.Round) as Rondas ,B.Name FROM  pi.races A inner join pi.circuits B on Circuitld = `circuit Id` group by B.Name order by Rondas desc limit 1;")
        #fetchall(): es para recuperar todos las filas de la BD, es una tupla
        datos = cur.fetchone()
        cur.close()    
        aux= ""
        aux = datos
        return aux
    
    def consultaMayorPuntos(self):
            # cur es el cursor siempre que quiera acceder a la BD que es el bojeto cnn(conección)
        cur = self.cnn.cursor()
        #execute(): ejecutar una consulta
        cur.execute("SELECT B.Name, sum(Points) as Puntos, C.Nacionality as NacionalidadConstructor FROM pi.results A JOIN pi.drivers B on (A.`Driver Id` = B.`Driver Id`) JOIN pi.constructors C on (A.`Constructor Id` =  C.`Constructor Id`) where C.Nacionality = 'American' or C.Nacionality ='British'  group by B.Name order by Puntos desc limit 1;")
        #fetchall(): es para recuperar todos las filas de la BD, es una tupla
        datos = cur.fetchone()
        cur.close()    
        aux= ""
        aux = datos
        return aux
    
    
