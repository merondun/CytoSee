from setuptools import setup, find_packages

setup(
    name='cytoseen',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.R', '*.Rmd', 'examples/*'],  # Include all R and Rmd files in any package directory
    },
    description='Methylation reproducibility metrics from Bismark coverage files',
    author='Merondun',
    entry_points={
        'console_scripts': [
            'cytoseen=cytoseen.cytoseen:main',
        ],
    },
    install_requires=[],
)

