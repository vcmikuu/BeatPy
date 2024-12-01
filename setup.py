from setuptools import setup, find_packages

setup(
    name="beatpy",
    version="0.1.1",
    description="A Python wrapper for the BeatSaver API",
    author="laynia",
    author_email="vc.mikuu@outlook.jp",
    url="https://github.com/vcmikuu/BeatPy",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
