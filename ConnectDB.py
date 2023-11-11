import psycopg2

class Db:
      
    def getLastRollId(self,query):
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="55555",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="knitting")
            cursor = connection.cursor()
            postgreSQL_select_Query = query
            
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            print(mobile_records[0])
            return mobile_records[0][0]

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
         
    def connectionDB(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="55555",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="knitting")
            # cursor =        
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        return connection

    def giveTheUpdateQuery(self,query):
        connection = self.connectionDB()
        cursor = connection.cursor() 
        cursor.execute(query)
        connection.commit()
        print("Inserted") 
        
    def giveTheUpdateQueryWithVal(self,query,value):
        connection = self.connectionDB()
        cursor = connection.cursor() 
        cursor.execute(query,value)
        connection.commit()
        print("Inserted") 
    
    def LastRevalution(self):
        connection = self.connectionDB()
        cursor = connection.cursor() 
        cursor.execute("select revolution from roll_details where roll_sts_id= 1")
        mobile_records = cursor.fetchall()
        return mobile_records[0][0]

    def UpdateRollStsTo(self, value):
        query = "UPDATE roll_details SET revolution = %s WHERE roll_sts_id = %s"
        val = (str(value),1)
        connection = self.connectionDB()
        cursor = connection.cursor() 
        # record = cursor.fetchone()
        # print(record)
        cursor.execute(query,val)
        connection.commit()
        
        




