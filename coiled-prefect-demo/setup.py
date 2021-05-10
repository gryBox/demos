from setuptools import setup, find_packages

setup(
    name="prefect_coiled",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    setup_requires=['setuptools_scm']
)