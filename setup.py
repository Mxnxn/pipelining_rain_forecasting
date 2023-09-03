from setuptools import find_packages,setup
from typing import List

HYPE_E = '-e .'
def get_requirements(file_path) -> List[str]:
    '''
        This function will return all of the packages required for the project

        file_path :: str -> path of the file
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [lib.replace('\n',' ') for lib in requirements]
        if HYPE_E in requirements:
            requirements.remove(HYPE_E)

        return requirements


setup(
    name='ML Project',
    version='1.0',
    author='Manan Soni',
    author_email='soni.ma@northeastern.edu',
    packages=find_packages(),
    install_requires=get_requirements('./requirements.txt')
)