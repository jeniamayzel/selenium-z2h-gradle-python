import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium-z2h-pkg-jeniamayzel", # Replace with your own username
    version="0.0.1",
    author="Mayzel, Evgeny",
    author_email="jenia.mayzel@gmail.com",
    description="A Selenium automation bootstrap",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeniamayzel/selenium-z2h-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'selenium',
    'pyyaml',
    'html-testRunner'
    ],
    python_requires='>=3.6',
)