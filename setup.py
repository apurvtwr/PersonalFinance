from setuptools import setup, find_packages

DEV_REQUIREMENTS = ["jupyterlab"]
TEST_REQUIREMENTS = ["nose"]
setup(
    name="market-analysis",
    version="1.0.0",
    packages=find_packages(".", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.7.0",
    install_requires=["yfinance>=0.1.72"],
    scripts=["analysis"],
    extras_require={"dev": DEV_REQUIREMENTS, "test": TEST_REQUIREMENTS},
)
