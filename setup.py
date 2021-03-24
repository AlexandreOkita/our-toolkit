VERSION = '0.16'
from distutils.core import setup
setup(
  name = 'ourtoolkit',
  packages = ['ourtoolkit'],
  version = VERSION,
  license='MIT',
  description = 'A bundle with useless and funny modules',
  author = 'AlexandreOkita',
  author_email = 'xande.okita@gmail.com',
  url = 'https://github.com/AlexandreOkita/our-toolkit',
  download_url = f'https://github.com/AlexandreOkita/our-toolkit/archive/{VERSION}.tar.gz',
  keywords = ['funny', 'useless', 'general', 'miscelaneous', "open", 'source'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
