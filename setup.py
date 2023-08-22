from setuptools import setup, find_packages

setup(
    name='my-library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'docx',
        'pdf2docx',
        'pdf2image',
        'pytesseract',
        'Pillow'
    ],
)
