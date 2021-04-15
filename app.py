import numpy as np
import pandas as pd
import pickle
from sklearn import metrics

data = pd.read_csv("rainfall in india 1901-2015.csv")
# data.head()

data = data.fillna(data.mean())

group = data.groupby('SUBDIVISION')['YEAR','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
data=group.get_group(('TAMIL NADU'))
# data.head()

df=data.melt(['YEAR']).reset_index()
# df.head()

df= df[['YEAR','variable','value']].reset_index().sort_values(by=['YEAR','index'])
# df.head()

df.columns=['Index','Year','Month','Avg_Rainfall']
Month_map={'JAN':1,'FEB':2,'MAR' :3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,
   'OCT':10,'NOV':11,'DEC':12}
df['Month']=df['Month'].map(Month_map)
# df.head(12)

df.drop(columns="Index",inplace=True)

X=np.asanyarray(df[['Year','Month']]).astype('int')
y=np.asanyarray(df['Avg_Rainfall']).astype('int')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

from sklearn.ensemble import RandomForestRegressor
random_forest_model = RandomForestRegressor(max_depth=100, max_features='sqrt', min_samples_leaf=4,
                      min_samples_split=10, n_estimators=800)
random_forest_model.fit(X_train, y_train)

# y_predict = random_forest_model.predict(X_test)

# print('MAE:', metrics.mean_absolute_error(y_test,y_predict))
# print('MSE:', metrics.mean_squared_error(y_test, y_predict))

# print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_predict)))
# print("-----------Training Accuracy------------")
# print(round(random_forest_model.score(X_train,y_train),3)*100)
# print("-----------Testing Accuracy------------")
# print(round(random_forest_model.score(X_test,y_test),3)*100)

file = open("model.pkl","wb")
pickle.dump(random_forest_model,file)
file.close()
# print(y_predict)