import setuptools

setuptools.setup(

    name="Master_thesis",
    version="0.1",
    description="Applications of machine learning algorithms to remove noise and artifacts present in brain MRI records",
    author=['Tomasz Sachanowski'],
    packages=setuptools.find_packages(),
    install_requires=['numpy','dataframe', 'nibabel', 'pysimplegui']
)