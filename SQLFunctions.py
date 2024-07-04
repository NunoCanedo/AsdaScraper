## IMPORT LIBRARIES


import mysql.connector

import csv



## Function to connect Python to MYSQL and save the TAXONOMY TREE data
    
def sql_save_taxonomy(table_name, tree_data):

    ## Define parametrs to connect python to MYSQL

    db = mysql.connector.connect(
        host = 'localhost',    ## IN MY CASE IS A LOCAL DATABASE
        user = 'YourUserName',    ##INPUT YOUR OWN USERNAME
        passwd = 'YourPasswor',    ## INPUT YOUR OWN PASSWORD
        database = 'SuperMarketScraper'
    )
    
    mycursor = db.cursor()
    

    ## Create table taxonomy


    query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, date DATE, department_name VARCHAR(50) NOT NULL, department_ID int NOT NULL, department_hierarchy_id VARCHAR(50) NOT NULL, department_type VARCHAR(50) NOT NULL, department_url VARCHAR(50) NOT NULL, category_name VARCHAR(50) NOT NULL, category_ID int NOT NULL, category_hierarchy_ID VARCHAR(50) NOT NULL, category_type VARCHAR(50) NOT NULL, category_url VARCHAR(50) NOT NULL, category_legislative_ID VARCHAR(50) NOT NULL, category_legislative_name VARCHAR(50) NOT NULL, aisle_name VARCHAR(50) NOT NULL, aisle_ID VARCHAR(50) NOT NULL, aisle_hierarchy_ID VARCHAR(50) NOT NULL, aisle_type VARCHAR(50) NOT NULL, aisle_url VARCHAR(50) NOT NULL, shelve_name VARCHAR(50) NOT NULL, shelve_ID int NOT NULL, shelve_hierarchy_ID VARCHAR(50) NOT NULL, shelve_type VARCHAR(50) NOT NULL, shelve_url VARCHAR(50) NOT NULL )'

    mycursor.execute(query)
    db.commit()

#def save_data( tree_data):
    ## Loop the values scraped from the webpage and insert in to the table
    for value in tree_data:
        #x = value.get('shleve_ID')

        #query = "INSERT IGNORE INTO " + table_name + " (ID, department, category, aisle, shelve, web_page_ID) VALUES ( %(shleve_ID)s, %(department_name)s, %(category_name)s, %(aisle_name)s, %(shelve)s, %(web_ID)s), value)

        mycursor.execute("INSERT IGNORE INTO " + table_name + " (date, department_name, department_ID, department_hierarchy_id, department_type, department_url, category_name, category_ID, category_hierarchy_ID , category_type, category_url, category_legislative_ID, category_legislative_name, aisle_name, aisle_ID, aisle_hierarchy_ID, aisle_type, aisle_url, shelve_name, shelve_ID, shelve_hierarchy_ID, shelve_type, shelve_url) VALUES (%(date)s, %(department_name)s, %(department_ID)s, %(department_hierarchy_id)s, %(department_type)s, %(department_url)s, %(category_name)s, %(category_ID)s, %(category_hierarchy_ID)s, %(category_type)s, %(category_url)s, %(category_legislative_ID)s, %(category_legislative_name)s, %(aisle_name)s, %(aisle_ID)s, %(aisle_hierarchy_ID)s, %(aisle_type)s, %(aisle_url)s, %(shelve_name)s, %(shelve_ID)s, %(shelve_hierarchy_ID)s, %(shelve_type)s, %(shelve_url)s)", value)
    db.commit()
    
      
      
def save_taxonomy(table_name, csv_file):
    

    db = mysql.connector.connect(
        host = 'localhost',    ## IN MY CASE IS A LOCAL DATABASE
        user = 'YourUserName',    ##INPUT YOUR OWN USERNAME
        passwd = 'YourPasswor',    ## INPUT YOUR OWN PASSWORD
        database = 'SuperMarketScraper'
    )
    
    mycursor = db.cursor()
    
    query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, date DATE, department_name VARCHAR(50) NOT NULL, department_ID int NOT NULL, department_hierarchy_id VARCHAR(50) NOT NULL, department_type VARCHAR(50) NOT NULL, department_url VARCHAR(50) NOT NULL, category_name VARCHAR(50) NOT NULL, category_ID int NOT NULL, category_hierarchy_ID VARCHAR(50) NOT NULL, category_type VARCHAR(50) NOT NULL, category_url VARCHAR(50) NOT NULL, category_legislative_ID VARCHAR(50) NOT NULL, category_legislative_name VARCHAR(50) NOT NULL, aisle_name VARCHAR(50) NOT NULL, aisle_ID VARCHAR(50) NOT NULL, aisle_hierarchy_ID VARCHAR(50) NOT NULL, aisle_type VARCHAR(50) NOT NULL, aisle_url VARCHAR(50) NOT NULL, shelve_name VARCHAR(50) NOT NULL, shelve_ID int NOT NULL, shelve_hierarchy_ID VARCHAR(50) NOT NULL, shelve_type VARCHAR(50) NOT NULL, shelve_url VARCHAR(50) NOT NULL )'

    mycursor.execute(query)
    db.commit()
    
    
    with open(csv_file, 'r') as f:
        
        reader = csv.reader(f)
        next(reader)
        for value in reader:
            
            mycursor.execute("INSERT IGNORE INTO " + table_name + " (date, department_name, department_ID, department_hierarchy_id, department_type, department_url, category_name, category_ID, category_hierarchy_ID , category_type, category_url, category_legislative_ID, category_legislative_name, aisle_name, aisle_ID, aisle_hierarchy_ID, aisle_type, aisle_url, shelve_name, shelve_ID, shelve_hierarchy_ID, shelve_type, shelve_url) VALUES (%(date)s, %(department_name)s, %(department_ID)s, %(department_hierarchy_id)s, %(department_type)s, %(department_url)s, %(category_name)s, %(category_ID)s, %(category_hierarchy_ID)s, %(category_type)s, %(category_url)s, %(category_legislative_ID)s, %(category_legislative_name)s, %(aisle_name)s, %(aisle_ID)s, %(aisle_hierarchy_ID)s, %(aisle_type)s, %(aisle_url)s, %(shelve_name)s, %(shelve_ID)s, %(shelve_hierarchy_ID)s, %(shelve_type)s, %(shelve_url)s)", value)
        db.commit()
    
    mycursor.close()
    
    db.close()
    
    
    
## Function to create and insert data into table

def insert_values(product_data, table_name):

    db = mysql.connector.connect(
        host = 'localhost',    ## IN MY CASE IS A LOCAL DATABASE
        user = 'YourUserName',    ##INPUT YOUR OWN USERNAME
        passwd = 'YourPasswor',    ## INPUT YOUR OWN PASSWORD
        database = 'SuperMarketScraper'
    )


    mycursor = db.cursor()

    query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID INT AUTO_INCREMENT primary key NOT NULL, Date DATE, product_ID int, product_name VARCHAR(250), Price Varchar(50), Price_per VARCHAR(50), saver_banner VARCHAR(50), saver_link VARCHAR(250), quantity VARCHAR(50), label VARCHAR(50), Product_Link VARCHAR(250), product_image VARCHAR(250), URL VARCHAR(250))'

    mycursor.execute(query)
    db.commit()

    mycursor = db.cursor()

    for value in product_data:
    
        mycursor.execute("INSERT IGNORE INTO " + table_name + " (Date, product_ID, product_name, Price, Price_Per, saver_banner, saver_link, quantity, label, product_link, product_image, URL) VALUES ( %(extration_date)s, %(product_ID)s, %(product_name)s, %(price)s, %(price_per)s, %(saver_banner)s, %(saver_banner_link)s, %(quantity)s, %(label)s, %(product_link)s, %(product_image)s, %(url)s)", value)
        

        db.commit()
        
    mycursor.close()
    
    db.close()
    
    
    
    
