from setuptools import setup, find_packages

setup(name="guitesting", version='1.0', description=" GUI TESTING FRAMEWORK",
      packages=find_packages(),
      author="Shraddha Gupta",
      zip_safe=False,
      install_requires=[
          'setuptools',
          "pytest",
          "pytest-html",
          "requests",
          "requests-oauthlib",
          "pandas"
          "pytest-xdist"
          "lxml"

      ]
      )


