import pandas as pd

data = pd.read_excel (r'Example File (Vehicles).xlsx')
df = pd.DataFrame(data, columns= ['Vehicle Number:','Vehicle Type:','Attributes:'])

#df[df['Attributes:'].str.contains("5MT")]
#print(df.head())

search_list = ['5MT','6MT']

for i in search_list:
    print(df[df["Attributes:"].str.contains(i)][['Vehicle Number:','Attributes:']])


