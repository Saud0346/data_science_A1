import pandas as pd

read_data = pd.read_csv('/home/saud/Downloads/Pakistani_Traffic_Accidents.csv')

data4 =[1,2,3,4,5,6]



mask2 = read_data['Place'] == 'Pakistan'
data3  = read_data[mask2]
data4[0]  = ['Pakistan',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]


mask2 = read_data['Place'] == 'Punjab'
data3  = read_data[mask2]
data4[1]  = ['Punjab',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]


mask2 = read_data['Place'] == 'Sindh'
data3  = read_data[mask2]
data4[2]  = ['Sindh',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]

mask2 = read_data['Place'] == 'Khyber Pakhtunkhwa'
data3  = read_data[mask2]
data4[3]  = ['Khyber Pakhtunkhwa',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]

mask2 = read_data['Place'] == 'Balochistan'
data3  = read_data[mask2]
data4[4]  = ['Balochistan',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]

mask2 = read_data['Place'] == 'Islamabad'
data3  = read_data[mask2]
data4[5] = ['Islamabad',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]

mask2 = read_data['Place'] == 'Islamabad'
data3  = read_data[mask2]
data4[5] = ['Islamabad',data3['Total number of accidents'].sum(),data3['Injured'].sum(),data3['Killed'].sum()]


data5 = pd.DataFrame(data4,columns=['Places','Total number of Accidents','Total number of Injured','Total number of Killed'])

print(data5.to_string())

print("Maximum Accidents Date \n")
mask = read_data['Total number of accidents'] == read_data['Total number of accidents'].max()
data2 = read_data[mask]
print(data2[['Year','Total number of accidents']],"\n")

print("Menimmum Accidents Date \n")
mask = read_data['Total number of accidents'] == read_data['Total number of accidents'].min()
data2 = read_data[mask]
print(data2[['Year','Total number of accidents']],"\n","\n")









































