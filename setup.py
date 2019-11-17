import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fanfiction-apis-eladrinwizard1",  # Replace with your own username
    version="0.1.4",
    author="Abhishek Vijayakumar",
    author_email="vijayakumar.abhishek@gmail.com",
    description="A package for scraping stories from fanfiction websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eladrinwizard1/fanfiction-apis",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
