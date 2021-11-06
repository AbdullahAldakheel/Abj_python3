from distutils.core import setup
setup(
  name = 'Abj',         # How you named your package folder (MyLib)
  packages = ['Abj'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='OpenSource',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Abj Platform.',   # Give a short description about your library
  author = 'Abdullah',                   # Type in your name
  author_email = 'a.dakheek@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/AbdullahAldakheel/Abj_python3',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'python-decouple',
          'requests',
          'minio'
      ],
  entry_points={
    'console_scripts': ['Abj=Abj.abj:main']
  },
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    # 'License ::  OpenSource',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
