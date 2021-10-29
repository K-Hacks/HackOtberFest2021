#IRIS DATASET MODEL KMEAN REGRESSION
#GRIP SEPTEMBER2021

'IMPORTING PACKAGES'
import matplotlib.pyplot as plt
import pandas as pd

'IMPORTING REQUIRED PACKAGES FROM SCIKIT-LEARN'
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the iris dataset
iris = datasets.load_iris()
'creating dataFRAME'
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)

'KMEAN DATA PROCESSING'
knn= KNeighborsClassifier(n_neighbors=1)
X=iris.data
y=iris.target

'fitting the model'
knn.fit(X,y)  

'predictor'
def predictor(z):
    print(iris.target_names[z])
    
predictor(knn.predict([ [6.1,2.9,4.7,1.4] ]))

'training datas'

"""Control the size of the subsets with the parameters train_size and test_size. 
Determine the randomness of your splits with the random_state parameter """

X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.30,random_state=40)

'fitting the training model set'
knn.fit(X_train,y_train)

'predictions'
predictions=knn.predict(X_test)
performance=metrics.accuracy_score(y_test,predictions)
#print(str(int(performance*100))+"%")

'change test size value and random state so that the accuracy =100%'


'Finding the optimum number of clusters for k-means classification'

x = iris_df.iloc[:, [0, 1, 2, 3]].values

from sklearn.cluster import KMeans
kmn = [] 

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter = 300, n_init = 10,random_state=0)
    kmeans.fit(x)
    kmn.append(kmeans.inertia_)
    
'Plotting the graph'
plt.plot(range(1,11), kmn)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') # Within cluster sum of squares
plt.show()

'Applying kmeans to the dataset / Creating the kmeans classifier'
kmeans = KMeans(n_clusters=3,init='k-means++',max_iter =300,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(x)

'Visualising the clusters - On the first two columns'
plt.scatter(x[y_kmeans==0,0], x[y_kmeans== 0,1],s =100, c ='red', label='Setosa')
plt.scatter(x[y_kmeans==1,0], x[y_kmeans== 1,1],s =100, c ='blue', label='Versicolour')
plt.scatter(x[y_kmeans==2,0], x[y_kmeans== 2,1],s =100, c ='green', label='Virginica')

'Plotting the centroids of the clusters'
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1],s = 100, c = 'yellow', label = 'Centroids')
plt.legend()