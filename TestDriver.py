import pandas as pd

import csv

Tesco_Taxonomy = csv.DictReader(open("Asda_Taxonomy.csv"))

df = pd.DataFrame(Tesco_Taxonomy)

value = df.loc[(df['department_name'] == 'Fruit, Veg & Flowers') & (df['category_name'] == 'Fruit') & (df['aisle_name'] == 'View All Fruit'), ['aise_ID']]
a = (value.values[0])
print(str(a).replace("['", "").replace("']", ""))

## .replace("[']", "")