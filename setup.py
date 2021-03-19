import setuptools


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='weird-converter',
    version='0.2',
    author='AlbertSuarez',
    author_email='alsumo95@gmail.com',
    description='Strange combinations converter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlbertSuarez/weird-converter',
    license='Apache-2.0',
    packages=['weird_converter'],
    install_requires=[
        'numpy==1.18.4',
        'Pillow==8.1.1',
        'scipy==1.4.1'
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    keywords='converter audio image audio-to-image image-to-audio',
)
