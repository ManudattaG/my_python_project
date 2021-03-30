import setuptools

setuptools.setup(name="client-api",
      version="0.0.1",
      python_requires=">=3.6",
      author="Manudatta G",
      package_dir={"": "src"},
      packages=setuptools.find_packages("src"),
      include_package_data=True,
      install_requires=["flask"],
      setup_requires=["pytest-runner"],
      tests_require=["pytest", "coverage"])