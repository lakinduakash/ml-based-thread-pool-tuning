import numpy as np
from sklearn import tree
from sklearn import model_selection

def hyperparameter_tuning(tr_features , tr_labels):
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start = 200, stop =2000, num = 1000)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(5, 150, num = 50)]
    max_depth.append(None)
    # Minimum number of samples required to split a node min_samples_split = [x for x in range(1,51)]
    # Minimum number of samples required at each leaf node min_samples_leaf = [x for x in range(1,51)]
    # Method of selecting samples for training each tree bootstrap = [True, False]
    # Create the random grid
    random_grid = {
    'max_features': max_features ,
    'max_depth': max_depth ,
    'min_samples_split': min_samples_split ,
    'min_samples_leaf': min_samples_leaf ,
    }
    rf_hyper = tree.DecisionTreeRegressor()
    rf_random = model_selection.RandomizedSearchCV(estimator = rf_hyper , param_distributions = random_grid , n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    # Fit the random search model
    rf_random.fit(tr_features , tr_labels)
    return rf_random.best_params_
    a = hyperparameter_tuning(X_train ,y_train)
    return a