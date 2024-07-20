import pymysql
import pymysql.cursors

from dotenv import dotenv_values



config = dotenv_values('.env')

#print(config)


class PyMYSQL():
    # instance variable class, called with self
    host = config['HOST']
    user = config['USER']
    password = config['PASSWORD']
    database = config['DATABASE']
    charset = config['CHARSET']
    #cursorclass = config['CURSORCLASS']
    
    """
    def __init__(self, host, user, password, database, charset, cursorclass):
        self.host = config['HOST']
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.database = config['DATABASE']
        self.charset = config['CHARSET']
        self.cursorclass = config['CURSORCLASS']
    """    
    @classmethod
    def Connection(cls):
        try:
            with pymysql.connect(host=cls.host, user=cls.user, password=cls.password, database=cls.database, charset=cls.charset) as cnx:
                if cnx:
                    print("Connected")
                return cnx
        except pymysql.Error as e:
            print(f'Database Error %s', e)
    
    #@classmethod
    #def closeConx(self):
    #    if PyMYSQL.Connection.is_conne
    
    
    @classmethod
    def getUsers(cls):
        try:
            with pymysql.connect(host=cls.host, user=cls.user, password=cls.password, database=cls.database, charset=cls.charset) as cnx:
                with cnx.cursor() as cur:
                    cur.callproc('gUsers')
                    rows = cur.fetchall()
                    return rows
            if cnx == True:
                #cur.close()
                #cnx.close()
                cls.closeConnection()
            else:
                print(cnx == True)
        except pymysql.Error as e:
            print(f'Error: %s', e)
            
    @classmethod
    def closeConnection(cls):
        try:
            #if cnx == True:
            cur.close()
            cnx.close()
        except pymysql.Error as e:
            print(f'Cnx was not finished')
    
    
                    

                
                
    
                
if __name__ == '__main__':
    #cn = PyMYSQL(host=config['HOST'], user=config['USER'], password=config['PASSWORD'], database=config['DATABASE'], charset=config['CHARSET'], cursorclass=config['CURSORCLASS'])
    cn = PyMYSQL()
    if cn:
        print(cn.host)
        print('Connected')
    cn.Connection()
    cn.getUsers()
    