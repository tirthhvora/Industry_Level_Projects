from setuptools import find_packages, setup
from typing import List
'''
By importing find_packages from setuptools, we use this in our setup.py script to automatically discover and include all the packages in your project when building distributions
or installing the project. 
It saves you from manually specifying each package in the setup.py file, especially in larger projects with multiple nested packages.
'''


variable_Hypen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this function takes a string, and returns a list of strings
    it will return a list of requirements used in the setup function
    """
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    # -e . shouldn't be counted
        if variable_Hypen_e_dot in requirements:
            requirements.remove(variable_Hypen_e_dot)

    return requirements





#this is the metadata version
setup(name = "Industry_Level_Projects",
    version = '0.0.1',
    author = 'Tirth',
    author_email="tirthdatascience@gmail.com",
    packages=find_packages(), #This will dynamically discover and include all the packages within the project when building the distribution.
    install_requires = get_requirements('requirements.txt')#['pandas', 'numpy', 'seaborn', 'scipy', 'sklearn']
)
