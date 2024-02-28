from setuptools import setup, find_packages

setup(
    name="fincalc2",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
        "numpy",
        "scipy"
    ],
    # Additional metadata about your package
    author="Mattia Biancaterra",
    author_email="mattia.biancaterra@usi,ch",
    description="A simple example package",
    keywords="interest, finance, present value",
    url="https://github.com/mattybianca/FinanceCalc",  # Project home page
)
