import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
 ## A data class is a class that is designed to only hold data values--They aren't different from regular classes-
 #  but they usually don't have any other methods.
## they are typically used to store information that will be passed between different parts of a program or a system.
## In simple words dataclasses is used to create class variables


##To define class variables inside a class, we basically use __init__ constructor. But instead here we are using dataclass decorator-
## --so that we can directly define our class variables without using __init__ constructor.

# declaring DataIngestionConfig class to store train, test and raw data
@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'raw.csv')
    ## train_data_path, test_data_path, raw_data_path are the class variables defined using dataclass decorator


## If our class only contains  variables than we can go with dataclass decorator--
## But If our class also contains methods/functions better to go with the __init__ constructor as in the DataIngestion class below.
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## ingestion_config is my variable which stores all the three paths that are-
        ## --present inside the DataIngestionConfig class

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook\\Data\\Raw_data.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info('Train Test split initiated')
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
            
