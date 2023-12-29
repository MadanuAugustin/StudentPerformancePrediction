#### Python Utils is a collection of small Python functions and classes which make common patterns shorter and easier.

### In simple words utils will have a common functionalities which the entire project can use.

import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

## the below function is used for saving the object as pickel file in the hardiskpy
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3) ##we can also apply randomized_search_cv instead of grid_search_cv
            gs.fit(X_train,y_train)

            ## after finding the best model and params we are going to fit to the model as shown in the below code.
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train, y_train) ## training the model
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
            
            return report
    except Exception as e:
        raise CustomException (e, sys)

    # load_object function is responsible for loading the pkl file
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj: # opening the file_path in readbyte mode and loading the pkl file
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)