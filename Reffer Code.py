def GiveTheQuery(self,query):
        count = 0
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="55555",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="knitting")
            cursor = connection.cursor()
            postgreSQL_select_Query = query

            cursor.execute(postgreSQL_select_Query)
            # print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall()

            # print("Print each row and it's columns values")
            # print("RollId   RollNo   RollName   Description   RollStartDate   Revalution   RollStsId   timestamp   defectmapid   machineprgdtlID   OrderNo   ShiftNo   ")
            for row in mobile_records:
                print()
                count+=1
                for i in range(0, 12, 1):
                    print(row[i] , end = " ")  
                if count==20:
                    break
                

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")