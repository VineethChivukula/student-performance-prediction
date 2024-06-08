# find_packages() function is used to find all the packages in the current directory and its subdirectories
# setup() function is used to setup the package and install the required dependencies

from setuptools import find_packages, setup


HYPHEN_E = "-e ."


# This function reads the requirements.txt file and returns the list of requirements
def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
        return requirements


# This function is initializing the package and installing the required dependencies
setup(
    name='student_performance_prediction',
    version='0.0.1',
    author='Vineeth',
    author_email='vineethonsocialmedia@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
