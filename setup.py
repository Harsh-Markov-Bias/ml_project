from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # requirements = [req.replace('\n', '') for req in requirements] 
        requirements = [req.strip() for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harsh',
    author_email='harsh.pratap.singh1307@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)