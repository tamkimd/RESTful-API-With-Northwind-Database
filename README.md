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
### CRUD all tables
##### **URL** : /{table_name}/
 - `GET`  : return all data in  table_name
  ![image](https://user-images.githubusercontent.com/63099899/202987741-cce6f293-4e71-4adf-9094-429aceb32852.png)

 - `POST` : insert row
 ![image](https://user-images.githubusercontent.com/63099899/202987981-1c42d340-32cc-4bf1-90a2-753f3792e8f3.png)

##### **URL** : /{table_name}/{id}/
 - `GET`  : return a row with id ={id} in table_name
 ![image](https://user-images.githubusercontent.com/63099899/202987534-8265488d-fd20-4a9d-b190-ad8ae1a47edc.png)

 - `POST` : insert row
 ![image](https://user-images.githubusercontent.com/63099899/202987462-571695b4-f7f0-476a-bc65-58d2ca85054e.png)

 - `PUT`: Update a now with id ={id} in table_name
 ![image](https://user-images.githubusercontent.com/63099899/202987298-acba7edb-4f5d-4372-89cd-beb0fa7e4945.png)

 - `DELETE` : Delete a now with id ={id} in table_name
 ![image](https://user-images.githubusercontent.com/63099899/202986955-27233d28-6c87-4f44-8f32-400f59907307.png)

### SORT 
##### **URL** : /{table_name}/sort/{field}
##### **URL** : /{table_name}/sort/{field1}&{field2}
![image](https://user-images.githubusercontent.com/63099899/202987644-6657bb0e-7e81-4337-998b-0f47e5b274fd.png)

 - `GET`  : Returns all data arranged according to the fields table_name
 ![image](https://user-images.githubusercontent.com/63099899/202986659-7c1edef5-025f-4134-9cb6-1e82cd1294b5.png)

### SEARCH
##### **URL** : /{table_name}/search/{field}={value}
 -  `GET`  : Returns all data has field in table_name = value
### Analysis
 ![image](https://user-images.githubusercontent.com/63099899/202986571-2a630ca9-7ac0-4973-9ae8-e3e87fb2466f.png)

  
##### **URL** : /{table_name}/analysis/{field}
 - `GET`  : count the field in table_name . Return data and base64 image
![image](https://user-images.githubusercontent.com/63099899/202986344-c9da8210-a34c-49b6-a3a3-e1a4917d0e16.png)

  
