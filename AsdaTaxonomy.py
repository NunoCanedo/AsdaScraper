## Import Libraries

import requests
import pandas as pd
import datetime

import AuxFunctions
import SQLFunctions

## define date

today = datetime.date.today()



## Variable to save later in CSV and SQL DATABASE

Asda_taxonomy = []


api_url = "https://groceries.asda.com/api/bff/graphql"      ## Using API URL to get Taxonomy Tree to get all DATA ID for each individual page


## Define payload and headers to be able to scrape the data or will get ERROR

payload={"requestorigin":"gi","contract":"web/cms/taxonomy","variables":{"ship_date":1697414400000,"store_id":"4565","special_offer":True,"user_segments":["1007","1019","1020","1023","1024","1027","1038","1041","1042","1043","1047","1053","1055","1057","1059","1067","1070","1082","1087","1097","1098","1099","1100","1102","1105","1107","1109","1110","1111","1112","1116","1117","1119","1123","1124","1126","1128","1130","1140","1141","1144","1147","1150","1152","1157","1159","1160","1165","1166","1167","1169","1170","1172","1173","1174","1176","1177","1178","1179","1180","1182","1183","1184","1186","1189","1190","1191","1194","1196","1197","1198","1201","1202","1204","1206","1207","1208","1209","1210","1213","1214","1216","1217","1219","1220","1221","1222","1224","1225","1227","1231","1233","1236","1237","1238","1239","1241","1242","1245","1247","1249","1256","1259","1260","1262","1263","1264","1269","1271","1278","1279","1283","1284","1285","1288","1291","test_4565","4565_test","1293","1294","1295","1296","1298","1299","dp-false","wapp","store_4565","vp_L","anonymous","clothing_store_enabled","homepage_spotlight_ab_test","checkoutOptimization","NAV_UI","T003","T014","rmp_enabled_user"]}}
headers={
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'request-origin': 'gi'
}


data = requests.post(api_url,headers=headers,json=payload).json()
taxonomy = data['data']['tempo_taxonomy']['categories']



## Function do define each Shelve, assign a ID and get child from eacho 
## Maybe come back later to simplify all the data


def shelve(aisle_data):
    
    d = 10
    
    for shelve in aisle_data.get('aisle_child'):
        
        shelve_data = {
            'date': datetime.date.today(),
            'department_name': aisle_data.get('department_name'),
            'department_ID': aisle_data.get('department_ID'),
            'department_hierarchy_id': aisle_data.get('department_hierarchy_id'),
            'department_type': aisle_data.get('taxonomy_type'),
            'department_url': aisle_data.get('department_url'),
            #'department_child': department_data.get('department_child'),
            'category_name': aisle_data.get('category_name'),
            'category_ID': aisle_data.get('category_ID'),
            'category_hierarchy_ID': aisle_data.get('category_hierarchy_ID'),
            'category_type': aisle_data.get('category_type'),
            'category_url': aisle_data.get('category_url'),
            'category_legislative_ID': aisle_data.get('category_legislative_ID'),
            'category_legislative_name': aisle_data.get('category_legislative_name'),
            #'category_child': category_data.get('category_child'),
            'aisle_name': aisle_data.get('aisle_name'),
            'aisle_ID': aisle_data.get('aise_ID'),
            'aisle_hierarchy_ID': aisle_data.get('aisle_hierarchy_ID'),
            'aisle_type': aisle_data.get('aisle_type'),
            'aisle_url': aisle_data.get('aisle_url'),
            #'aisle_child': aisle_data.get('aisle_child'),
            'shelve_name': shelve.get('taxonomy_name'),
            'shelve_ID': AuxFunctions.product_code(aisle_data.get('aisle_ID'), d),
            'shelve_hierarchy_ID': shelve.get('hierarchy_id'),
            'shelve_type': shelve.get('taxonomy_type'),
            'shelve_url': shelve.get('canonical_url')
            }



# (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, date DATE, department_name VARCHAR(50) NOT NULL, department_ID int NOT NULL, department_hierarchy_id VARCHAR(50) NOT NULL, department_type VARCHAR(50) NOT NULL, department_url VARCHAR(50) NOT NULL, category_name VARCHAR(50) NOT NULL, category_ID int NOT NULL, category_hierarchy_ID , category_type VARCHAR(50) NOT NULL, category_url VARCHAR(50) NOT NULL, category_legislative_ID VARCHAR(50) NOT NULL, category_legislative_name VARCHAR(50) NOT NULL, aisle_name VARCHAR(50) NOT NULL, aisle_ID int NOT NULL, aisle_hierarchy_ID VARCHAR(50) NOT NULL, aisle_type VARCHAR(50) NOT NULL, aisle_url VARCHAR(50) NOT NULL, aisle_legislative_ID VARCHAR(50) NOT NULL, shelve_name VARCHAR(50) NOT NULL, shelve_ID int NOT NULL, shelve_hierarchy_ID VARCHAR(50) NOT NULL, shelve_type VARCHAR(50) NOT NULL, shelve_url VARCHAR(50) NOT NULL)


        taxonomy_asda = []
        taxonomy_asda.append(shelve_data)
       
        Asda_taxonomy.append(shelve_data)
        
        #print('%%%%%%%%%%%%%%%%%%%%%%%%%%')
        
        #SQLFunctions.sql_save_taxonomy('AsdaTaxonomy7', shelve_data)
        
        
        
        d+=1
        
        ## Save all teh data in a CSV file (taking the easy route with pandas instead of CVSDictWriter)
        ## Should create a function to save the data
        
        df = pd.DataFrame(Asda_taxonomy)
        df.to_csv(f'Asda_Taxonomy{today}.csv', index=False)
            
#       
    
    
## Function do define each Aisle, assign a ID and get child from eacho 

def aisle(category_data):
    
    c = 10
    e = 99
    
    for aisle in category_data.get('category_child'):
        
        aisle_data = {
            'date': datetime.date.today(),
            'department_name': category_data.get('department_name'),
            'department_ID': category_data.get('department_ID'),
            'department_hierarchy_id': category_data.get('department_hierarchy_id'),
            'department_type': category_data.get('taxonomy_type'),
            'department_url': category_data.get('department_url'),
            #'department_child': department_data.get('department_child'),
            'category_name': category_data.get('category_name'),
            'category_ID': category_data.get('category_ID'),
            'category_hierarchy_ID': category_data.get('category_hierarchy_ID'),
            'category_type': category_data.get('category_type'),
            'category_url': category_data.get('category_url'),
            'category_legislative_ID': category_data.get('category_legislative_ID'),
            'category_legislative_name': category_data.get('category_legislative_name'),
            #'category_child': category_data.get('category_child'),
            'aisle_name': aisle.get('taxonomy_name'),
            'aisle_ID': AuxFunctions.product_code(category_data.get('category_ID'), c),
            'aisle_hierarchy_ID': aisle.get('hierarchy_id'),
            'aisle_type': aisle.get('taxonomy_type'),
            'aisle_url': aisle.get('canonical_url'),
            'aisle_child': aisle.get('child_taxonomies'),
            'shelve_name': '',                              ## Leave it empty to avoid miss data, may come back later 
            'shelve_ID': AuxFunctions.product_code(AuxFunctions.product_code(category_data.get('category_ID'), c), e),                                ## Leave it empty to avoid miss data, may come back later 
            'shelve_hierarchy_ID': '',                      ## Leave it empty to avoid miss data, may come back later 
            'shelve_type': '',                              ## Leave it empty to avoid miss data, may come back later 
            'shelve_url': aisle.get('canonical_url')        ## Not sure if is the right data, need to check and come back later
                
            }
        
        c+=1
        
        
        if aisle.get('child_taxonomies') == []:
            
            Asda_taxonomy.append(aisle_data)
            #print('====================')
            
        else:
            
            shelve(aisle_data)
        
            
        

## Function do define each Category, assign a ID and get child from eacho 

def category(department_data):
    
    b = 10
    
    for category in department_data.get('department_child'):
    
        category_data = {
                'department_name': department_data.get('department_name'),
                'department_ID': department_data.get('department_ID'),
                'department_hierarchy_id': department_data.get('department_hierarchy_id'),
                'department_type': department_data.get('taxonomy_type'),
                'department_url': department_data.get('department_url'),
                #'department_child': department_data.get('department_child'),
                'category_name': category.get('taxonomy_name'),
                'category_ID': AuxFunctions.product_code(department_data.get('department_ID'), b),
                'category_hierarchy_ID': category.get('hierarchy_id'),
                'category_type': category.get('taxonomy_type'),
                'category_url': category.get('canonical_url'),
                'category_legislative_ID': category.get('legislative_id'),
                'category_legislative_name': category.get('legislative_category'),
                'category_child': category.get('child_taxonomies')
                
            }
        #print(category_data)
        #print('===========================')
        b+=1
        aisle(category_data)





## Function do define each department, assign a ID and get child from eacho 

def department (taxonomy):
    
    a = 10
    
    for name in taxonomy:
        
        department_data = {
            'department_name': name.get('taxonomy_name'),
            'department_ID': a,
            'department_hierarchy_id': name.get('hierarchy_id'),
            'department_type': name.get('taxonomy_type'),
            'department_url': name.get('canonical_url'),
            'department_child': name.get('child_taxonomies')
            
        }
        #print(department_data)
        category(department_data)
        
        a+=1
        


## Run code as main

if __name__ == '__main__':                          
    department(taxonomy)   
    
    
csv_file = f'Asda_Taxonomy{today}.csv'
    
#SQLFunctions.sql_save_taxonomy('AsdaTaxonomy2', csv_file)

SQLFunctions.save_taxonomy('asdataxonomy88', csv_file)