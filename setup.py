from setuptools import setup, find_packages
setup(
    name='Deltacode',
    version='0.7.1',
    author='daisseur',
    author_email='daisseur@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/daisseur/Deltacode_project',
    description="Encoder et décoder du texte à l'aide de pluisieurs types d'encodages",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['os', 'base58', 'base64', 'time', 'sys', 'codecs', 'string'],
    keywords=['python', 'deltacode', 'code', 'coding', 'encoding'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
