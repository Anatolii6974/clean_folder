from setuptools import setup, find_namespace_packages

setup(
    name="Clean folder",
    version="0.0.2",
    description="Clean and sort folder",
    url="",
    author="A. Perfilov",
    author_email="anatolii.perfilov@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)