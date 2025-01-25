from distutils.core import setup

setup(name='BalChemEq',
      version='1.0',
      description='Tools to Balance Chemical Equations',
      author='Federico B,',
      author_email='fede.j.ba10@gmail.com',
      packages=['methods'],
      py_modules=['BCE'],
      install_requires=['numpy']
     )