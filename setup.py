from setuptools import find_packages,setup
from typing import List
Hypen_E_Dot="-e ."
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  # this will read line at a time
        requirements=[req.replace("\n","") for req in requirements] # this will repalce \n by empty space each time created using readline()

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
        return requirements
    

setup(
name='mlProject',
version='0.0.1',
author='Aadil',
author_email='hussainaadil378@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)