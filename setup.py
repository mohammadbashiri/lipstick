from setuptools import setup, find_packages

setup(
    name="lipstick",
    version="0.0.6",
    author="Mohammad Bashiri",
    author_email="mohammadbashiri93@gmail.com",
    description="A collection of plotting functions.",
    url="https://github.com/mohammadbashiri/lipstick",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib>=3.3.0", "pillow>=7.2.0"],
)
