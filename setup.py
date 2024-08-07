from setuptools import find_packages, setup
setup(
    name='mcqgenerator',
    version= '0.0.1',
    author='Ashis Khan',
    author_email= 'ashiskhan3@gmail.com',
    install_requires = ['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages() # this method is resposible for finding the local packages
)