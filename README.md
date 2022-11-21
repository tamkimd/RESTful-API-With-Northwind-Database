#  RESTful-API-With-Northwind-Database

##  Northwind database schema 
![image](https://user-images.githubusercontent.com/63099899/202976369-5d4a9c36-8565-4b71-bd2e-a3117e764620.png)
 [Mysql script from wiki](https://en.wikiversity.org/wiki/Database_Examples/Northwind/MySQL)

## API
### PARAMETERS: 
 - {table_name}: categories , customers , employees , orders , orderdetails , products , suppliers
 - {field} : example fields of customers {CustomerID}, {CustomerName}, {ContactName}, {Address}, {City}, {PostalCode}, {Country}
 - {value} : value of field
 - {id} : id field
 ### Function:
 #### CRUD all tables
##### **URL:** : /{table_name}/
 - `GET`  : return all data in  table_name
 - `POST` : insert row
##### **URL:** : /{table_name}/{id}/
 - `GET`  : return a row with id ={id} in table_name
 - `POST` : insert row
 - `PUT`: Update a now with id ={id} in table_name
 - `DELETE` : Delete a now with id ={id} in table_name
   #### SORT 
##### **URL:** : /{table_name}/sort/{field}
##### **URL:** : /{table_name}/sort/{field1}&{field2}
 - `GET`  : Returns all data arranged according to the fields table_name
   #### SEARCH
##### **URL:** : /{table_name}/search/{field}={value}
 -  `GET`  : Returns all data has field in table_name = value
  #### Analysis
  
##### **URL:** : /{table_name}/analysis/{field}
 - `GET`  : count the field in table_name . Return data and base64 image
  
