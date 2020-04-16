import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InowasFlopyAdapter",
    version="1.0.0a2",
    author="Ralf Junghanns",
    author_email="ralf.junghanns@gmail.com",
    description="A FLOPY wrapper for the INOWAS-platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inowas/InowasFlopyAdapter",
    packages=setuptools.find_packages(),
    install_requires=[
        'flopy==3.3.0',
        'numpy>=1.9'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)