from setuptools import find_packages, setup

setup(
    name="orchestrate",
    packages=find_packages(exclude=["orchestrate_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
