from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="API_project",
    version="1.0.0",
    author="Filesi Gianluca, O'Donovan Luke",
    author_email="gianluca.filesi@edhec.com",
    description="Car price prediction API",
    packages=find_packages(),
    install_requires=requirements,
)