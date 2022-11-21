
from flask import Flask , request 
import json
from flask_restful import Api, Resource
import pandas as pd
import plotly.express as px
import plotly.io as pio


# connect to mysql
import mysql.connector
db=mysql.connector.connect(user="root",password="uento123",host="localhost",database="northwind")
cursor=db.cursor(dictionary=True,buffered=True)

# get name field of table
tables=['categories','customers','employees','orders','orderdetails','products','suppliers']
all_tables={} 
for table in tables:
    query = "SELECT * from northwind."+table +";"
    cursor.execute(query)
    field_name = [field[0] for field in cursor.description]
    all_tables[table] = field_name

# check data exist or not
    # if the values of all fields are the same as the data then return true
def check_data_exist(table_name,data):
    fields= ""
    for field in all_tables[table_name][1:]: # skip id
        fields += field + " = '" + str(data[field]) + "' and " 
    fields = fields[:-4] # remove last "and"
    query = "SELECT * from northwind."+table_name +" where "+fields+" ;"
    cursor.execute(query)
    check = cursor.fetchall()
    if check == []:
        return False
    else:
        return True
# CRUD functions 
class All_rows(Resource):
    def get(self,table_name):
        # get all rows
        if table_name in tables:
            query="select * from northwind."+table_name +";"
            cursor.execute(query)

            # rows=cursor.fetchall()
            name=cursor.fetchall()
            # print(values)
            jsonObj = json.dumps(name,  default=str)
            return json.loads(jsonObj)
        else:
            return {"error":"table not found"} , 400
    def post(self,table_name):
        # insert row
        if table_name in tables:
            data=request.json
            check=check_data_exist(table_name,data)
            if check:
                return {"error":"data exist"},400
            else:
                fields= ""
                values= ""
                for field in all_tables[table_name][1:]:
                    fields += field + ","
                    values += " '"+str(data[field])+"' ,"
                fields = fields[:-1] # remove last ","
                values = values[:-1] # remove last ","
                query = "INSERT INTO northwind."+table_name+" ("+fields+") VALUES ("+values+");"
                cursor.execute(query)
                db.commit()
                return {"success":"data inserted"},201
        else:
            return {"error":"table not found"} , 400

class Row(Resource):
    def get(self,table_name,id):
        # get row by id 
        if table_name in tables:
            # get row by id ( all_tables[table_name][0] is the id field name )
            query="select * from northwind."+table_name + " where " +all_tables[table_name][0] +" = %s;"
            cursor.execute(query,(id,))
            rows=cursor.fetchall()
            jsonObj = json.dumps(rows,  default=str)
            return json.loads(jsonObj)
        else:
            return {"error":"table not found"} , 400
    def post(self,table_name,id):
        # insert row
        if table_name in tables:
            data=request.json
            check=check_data_exist(table_name,data)
            if check:
                return {"error":"data exist"},400
            else:
                fields= ""
                values= ""
                for field in all_tables[table_name][1:]:
                    fields += field + ","
                    values += " '"+str(data[field])+"' ,"
                fields = fields[:-1] # remove last ","
                values = values[:-1] # remove last ","
                query = "INSERT INTO northwind."+table_name+" ("+fields+") VALUES ("+values+");"
                cursor.execute(query)
                db.commit()
                return {"success":"data inserted"},201
        else:
            return {"error":"table not found"} , 400
    def put(self,table_name,id):
        # update row by id ( all_tables[table_name][0] is the id field name )
        if table_name in tables:
            data=request.json
            # check data exist by id
            query="select * from northwind."+table_name + " where " +all_tables[table_name][0] +" = %s;"
            cursor.execute(query,(id,))
            rows=cursor.fetchall()
            if rows == []:
                return {"error":"data not found"},400
            else:
                fields= ""
                for field in all_tables[table_name][1:]:
                    fields += field + " = '" + str(data[field]) + "' , " 
                fields = fields[:-2] # remove last ","
                query = "UPDATE northwind."+table_name+" SET "+fields+" where "+all_tables[table_name][0]+" = %s;"
                cursor.execute(query,(id,))
                db.commit()
                return {"success":"data updated"},200
        else:
            return {"error":"table not found"} , 400
    def delete(self,table_name,id):
        # delete row by id ( all_tables[table_name][0] is the id field name )
        if table_name in tables:
            query="delete from northwind."+table_name + " where " +all_tables[table_name][0] +" = %s;"
            cursor.execute(query,(id,))
            db.commit()
            return {"success":"data deleted"},200
        else:
            return {"error":"table not found"} , 400

# sort by fields
class Sort(Resource):
    def get(self,table_name,field):
        # if field has & then it is a sort by two fields
        if table_name in tables:
            if "&" in field:
                field=field.split("&")
                # check if the fields exist in the table
                if field[0] and field[1] in all_tables[table_name]:
                    query="select * from northwind."+table_name +" order by "+field[0]+","+field[1]+";"
                else:
                    return {"error":"field not found"} , 400
            else:
                if field in all_tables[table_name]:
                    query="select * from northwind."+table_name +" order by "+field+";"
                else:
                    return {"error":"field not found"} , 400
            cursor.execute(query)
            name=cursor.fetchall()
            jsonObj = json.dumps(name,  default=str)
            return json.loads(jsonObj)
        else:
            return {"error":"table not found"} , 400

# search by fields
class Search(Resource):
    def get(self,table_name,field,value):
        if table_name in tables:
                if field in all_tables[table_name]:
                    query="select * from northwind."+table_name +" where "+field+" = %s;"
                    cursor.execute(query,(value,))
                    name=cursor.fetchall()
                    jsonObj = json.dumps(name,  default=str)
                    return json.loads(jsonObj)
                else:
                    return {"error":"field not found"} , 400
        else:
            return {"error":"table not found"} , 400
# analysis by fields and draw a chart
class Analysis(Resource):
    def get(self,table_name,field):
        if table_name in tables:
            if field in all_tables[table_name]:
                query="select "+field+",count(*) from northwind."+table_name +" group by "+field+";"
                cursor.execute(query)
                name=cursor.fetchall()  
                jsonObj = json.dumps(name,  default=str)
                # draw pie chart with plotly
                dp=pd.DataFrame(name,columns=[field,'count'])
                fig = px.pie(dp, values='count', names=field)
                pio.renderers.default = "browser"
                pio.write_image(fig, file='image.png', format='png', engine='kaleido')
                # convert to base64
                import base64
                with open("image.png", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                return {"data":json.loads(jsonObj),"image":encoded_string.decode('utf-8')}

              
            else:
                return {"error":"field not found"} , 400


        else:
            return {"error":"table not found"} , 400





