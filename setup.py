from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
   

   ## this function will return the list of requirements
   requirements = []
   with open(file_path) as file_obj:
      requirements = file_obj.readlines()
      requirements =[req.replace("\n", "") for req in requirements] ##  whenever the packages are getting read from the requirements file-
      ## their is a \n for every line which we need to replace it with the blank_space

      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)

   return requirements


setup(

    name= 'StudentPerformancePrediction',
    version= '0.0.1',
    author= 'Augustin',
    author_email='augustin7766@gmail.com',
    packages = find_packages(), ## this find_packages function actually looks for the __init__.py command in all the folders and makes--
    ## -- those particular folders as a package. for ex: __init__.py in 'src' folder.

    # install_requires = ['pandas', 'numpy', 'seaborn']     ##--writing the packages manually is a hectic work, so we want our--
    ## get_requirements() function to automatically detect the packages in requirements.txt file and install them.

    install_requires = get_requirements('requirements.txt')

)