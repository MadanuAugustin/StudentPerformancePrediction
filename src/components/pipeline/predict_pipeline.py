import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object ## this is for loading out pickle files


class PredictPipeline:
    def __init__(self):
        pass
    
    # this function is used for predicting the output
    def predict(self, features):
        #  importing the model pickle file to predict the output
         try:
            model_path = 'artifacts\\model.pkl'
            preprocessor_path = 'artifacts\\preprocessor.pkl'
            #  load_object function loads the model pkl file
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            #  after loading the pkl files we need to scaled down our features
            data_scaled = preprocessor.transform(features)
            #  predicting
            preds = model.predict(data_scaled)
            return preds
         except Exception as e:
              raise CustomException(e, sys)

# CustomData class is responsible for mapping all the values given by the user in html page in the backend

class CustomData:
        def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
             self.gender = gender
             self.race_ethnicity = race_ethnicity
             self.parental_level_of_education = parental_level_of_education
             self.lunch = lunch
             self.test_preparation_course = test_preparation_course
             self.reading_score = reading_score
             self.writing_score = writing_score

        
        def get_data_as_data_frame(self):
            #  this function returns the input data as dataframe
             try:
                  custom_data_input_dict = {
                       "gender" : [self.gender],
                       "race_ethnicity" : [self.race_ethnicity],
                       "parental_level_of_education" : [self.parental_level_of_education],
                       "lunch" : [self.lunch],
                       "test_preparation_course":[self.test_preparation_course],
                       "reading_score":[self.reading_score],
                       "writing_score":[self.writing_score],
                  }
                  return pd.DataFrame(custom_data_input_dict)
             
             except Exception as e:
                  raise CustomException(e, sys)
            