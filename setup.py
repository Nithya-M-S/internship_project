from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements from the given file path.
    
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines() #read line from requirements.txt
        requirements = [req.replace("\n","")for req in requirements] #remove \n from each line
            #[req for req in requirements if req and not req.startswith('#')]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='internship_project',
    version='0.1.0',
    author='Nithya',
    author_email='nithyarani2730@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)