# python3 -m build 
# python3 -m twine upload dist/*

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='dynbike_helper_functions',
    version='0.1.4',
    description='A small package with collection of useful functions for the Dynamic Bike',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    license='MIT',
    packages=find_packages(),
    author="Peter Gates",
    author_email="pgate89@gmail.com",
    url="https://github.com/pomkos",
)

install_requires = [
    'numpy',
    'sqlalchemy',
    'pandas',
    'matplotlib',
    'seaborn'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, python_requires=">=3.8")