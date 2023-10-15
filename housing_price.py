from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
q = input('Enter City of U.S of Your Choice: ')
q2 = float(input('How many months into the future do you want to forecast?: '))
city = pd.read_csv('Sale_Prices_City.csv')
city = city.drop(columns=['RegionID', 'StateName', 'SizeRank'])
city.set_index('RegionName', inplace=True)
city = city.loc[q]
city.dropna(inplace=True)
city = city.astype(int)
try:                        #This is used to extract the prices
    city = city.iloc[0,:]
except:
    city = city.to_numpy()
w = 1
xs = []
ys = []
while w <= len(city): #Extracts x values as numbers
    xs.append([w])
    w += 1
for value in city: #Extracts y values
    ys.append([value])
X = np.array(xs)
y = np.array(ys)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, train_size=0.9)
clf = LinearRegression()
clf.fit(X_train, y_train)
X_predict = [[len(ys) + q2]]
pred = clf.predict(X_predict)
diff = pred - ys[-1]
print('The average house price', q2, 'months into the future is:', '$' + str(int(pred)))
if diff < 0:
    print('The prices decreased by:', '$' + str(int(abs(diff))))
else:
    print('The prices increased by:', '$' + str(int(diff)))