import os
from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Install colorama if using Windows
if os.name == 'nt':
   dependencies = ['riceprint', 'colorama']
else:
   dependencies = ['riceprint']

setup(
   name='ricekey',
   version='1.0.0',
   description='OS-agnostic threaded keypress event detector for killing loops.',
   long_description=long_description,
   author='Kevin Sacca',
   author_email='ssriceboat@gmail.com',
   url='https://github.com/ssriceboat/ricekey',
   license='MIT',
   classifiers=[
      'Development Status :: 4 - Beta',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
   ],
   packages=['ricekey'],
   package_dir={'ricekey': 'src/ricekey'},
   install_requires=dependencies,
   keywords='console terminal shell python key press keypress event'
)
