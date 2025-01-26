from setuptools import setup

from paystacks import version

setup(name='pypaystack',
      version=version.__version__,
      description='Python wrapper for Paystack API',
      url='https://github.com/Hafeezco75/paystacks',
      author=version.__author__,
      author_email='odunayeabdulhafeez@gmail.com',
      license=version.__license__,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['requests'],
      packages=['paystacks'],
      zip_safe=False
      )
