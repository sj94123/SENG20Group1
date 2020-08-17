from setuptools import setup, find_packages

# import the README
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

# package metadata
setup(
    name='SE20_HW1',
    version='0.1',
    description='SE HW1: Setting a Git Repo',
    author='Mita Gavade',
    author_email='magavade@ncsu.edu',
    url='https://github.com/sj94123/SENG20Group1',
    packages=find_packages(),
    long_description="""\
        Setting up a GitHub repository
      """,
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    keywords='software engineering',
    license='GNU',
    install_requires=[
        'pytest>=6.0.1',
    ],
)
