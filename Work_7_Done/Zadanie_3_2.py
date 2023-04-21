#Регрессор
import pandas as pd
from sklearn.model_selection import train_test_split

urls = {
    'class': r'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv',
    'reg': r'https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv'
}
print('Classifier\n')
df = pd.read_csv(urls['class'])
df.head(5)
df
df = df.rename(columns={'variety': 'target'})
X_df, Y_df = df.drop(['target'], axis=1), df.target
print('Dataset Size: ', X_df.shape, Y_df.shape)
X_train, X_test, Y_train, Y_test = train_test_split(X_df, Y_df, train_size=0.80, test_size=0.20, stratify=Y_df,
                                                    random_state=123)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
from sklearn.neural_network import MLPClassifier

mlp_classifier = MLPClassifier(random_state=123)
mlp_classifier.fit(X_train, Y_train)
Y_preds = mlp_classifier.predict(X_test)

print(Y_preds[:15])
print(Y_test[:15])
print('Test Accuracy: %.3f' % mlp_classifier.score(X_test, Y_test))
print('Training Accuracy: %.3f' % mlp_classifier.score(X_train, Y_train))

print('Loss: ', mlp_classifier.loss_)
print('Number of Coefs: ', len(mlp_classifier.coefs_))
print('Number of Intercepts: ', len(mlp_classifier.intercepts_))
print('Number of Iteration for Which Estimator Ran: ', mlp_classifier.n_iter_)
print('Name of Output Layer Activation Function: ', mlp_classifier.out_activation_, '\n')



df = pd.read_csv(urls['reg'])
df.head(5)

df = df.rename(columns = {'Salary' : 'target'})
X_df, Y_df = df.drop(['target'], axis = 1), df.target
print('Dataset Size: ', X_df.shape, Y_df.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X_df, Y_df, train_size = 0.80, test_size = 0.20,
													random_state = 123)
print('Train/Test size: ', X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)													
from sklearn.neural_network import MLPRegressor

mlp_regressor = MLPRegressor(random_state = 123)
mlp_regressor.fit(X_train, Y_train)

Y_preds = mlp_regressor.predict(X_test)

print (Y_preds[:10])
print (Y_test[:10])
print ('Test R^2 Score: %.3f'%mlp_regressor.score(X_test, Y_test))
print ('Training R^2 Score: %.3f'%mlp_regressor.score(X_train, Y_train))
print ('Loss: ', mlp_regressor.loss_)
print ('Number of Coefs: ', len(mlp_regressor.coefs_))
print ('Number of Intercepts: ', len(mlp_regressor.intercepts_))
print ('Number of Iteration for Which Estimator Ran: ', mlp_regressor.n_iter_)
print ('Name of Output Layer Activation Function: ', mlp_regressor.out_activation_)

