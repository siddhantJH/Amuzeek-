from setuptools import setup, find_packages

setup(
    name="AMUZEEK_BACKEND",
    version="0.1.0",
    description="Audio streaming backend utilities",
    author="Siddhant Jha",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
    ],
    python_requires=">=3.11",
)