import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grammatical",
    version="0.2.0",
    author="Parth Parikh",
    author_email="parthparikh1999p@gmail.com",
    description="Corrects the spelling and grammar of your text using ChatGPT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["grammatical"],
    url="https://github.com/pncnmnp/grammatical",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "openai", "pyperclip", "rich", "setuptools"],
    entry_points={
        "console_scripts": [
            "grammatical=grammatical:grammatical",
        ],
    },
    python_requires=">=3.7",
    include_package_data=True,
)
