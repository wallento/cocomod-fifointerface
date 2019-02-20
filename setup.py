import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cocomod-fifointerface",
    use_scm_version={
        "relative_to": __file__,
        "write_to": "cocomod/fifointerface/version.py",
    },
    author="Stefan Wallentowitz",
    author_email="stefan@wallentowitz.de",
    description="Cocotb FIFO interface modules",
    long_description=long_description,
    url="https://github.com/wallento/cocomod-fifointerface",
    packages=["cocomod.fifointerface"],
    setup_requires=[
        'setuptools_scm',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
)
