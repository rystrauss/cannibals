import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='cannibals',
    version='0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/rystrauss/cannibals',
    license='LICENSE',
    author='Ryan Strauss',
    author_email='ryanrstrauss@icloud.com',
    description='Search strategies for problem-solving agents.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6'
)
