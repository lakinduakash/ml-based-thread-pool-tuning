from numpy import loadtxt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

def cross_validation_r(model,X,Y):
    cv = train_test_split.ShuffleSplit(n_splits=5, test_size=0.3, random_state=1)
    scores = cross_validate(model, X, Y, cv=cv , scoring=['neg_mean_squared_error','neg_mean_absolute_percentage_error'])
    cv_mape = scores['test_neg_mean_absolute_percentage_error'] cv_mse = scores['test_neg_mean_squared_error']
    print("MAPEs: ", cv_mape)
    print("MSEs: ", cv_mse)
    print("MAPE: %0.2f%% with a standard deviation of %0.2f" % (abs(cv_mape.mean() * 100), cv_mape.std()))
    print("MSE: %0.2f with a standard deviation of %0.2f" % (abs(cv_mse.mean()), cv_mse.std()))
    # load data
    dataset = loadtxt('g_dataset_class_2.csv', delimiter = ",")  # split data into X and y
    X = dataset[:, 0:5]
    Y = dataset[:, 6]
    # split data into train and test sets
    seed = 6
    test_size = 0.3
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    # fit model no training data
    model = XGBRegressor()
    model.fit(X_train, y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    # Cross validation
    print("# cross validated evaluations")
    print(cross_validation_r(model, X, Y))
    # cross validated evaluations
    # MAPE: 8.45%
    # MSE: 1.83