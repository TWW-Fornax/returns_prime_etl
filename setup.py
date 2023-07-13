from setuptools import find_packages, setup

setup(
    name="returns_prime_etl",
    packages=find_packages() + ["returns_prime_etl"],
    package_dir={"returns_prime_etl": "returns_prime_etl"},
    version="1.0.0",
    description="returns prime etl (drive to bigquery) pipeline",
    author_email="shubham@fornaxhq.co",
    author="Shubham Kawade",
    license="fornaxhq.co",
    include_package_data=True,
    install_requires=[
        "gspread == 5.10.0",
        "pandas == 1.3.5",
        "datetime == 5.1",
        "google == 3.0.0",
        "google-cloud-bigquery == 3.4.0",
    ],
    long_description=open("README.md").read(),
    setup_requires=[],
    zip_safe=True,
)