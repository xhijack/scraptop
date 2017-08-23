import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {
    "packages": ["pkg_resources","os","sys", "lxml","xmlrpclib", "collections", "scrapy","zope.interface"],
    "excludes":['collections.abc'],
    "include_msvcr":True,
    "namespace_packages": ['zope'],
    "include_files": [
        ("C:\\Users\\ramdani\\scraptop\\scrapy.cfg","scrapy.cfg"),
        ("C:\\Users\\ramdani\\scraptop\\env\\Lib\\site-packages\\Scrapy\\VERSION","VERSION"),
        ("C:\\Users\\ramdani\\scraptop\\env\\Lib\\site-packages\\Scrapy\\mime.types","mime.types")
    ],
    "includes": ["pkg_resources", "os", "Flask", "twisted", "SQLAlchemy","scrapy", 'zope', 'zope.interface', 'pkgutil', 'lxml',
                         'lxml._elementpath', 'email.mime.multipart', 'email.mime.text',
                         ],
    }

executables = [
    Executable('main.py', base=base)
]

setup(name='Scraptop',
      version='0.1',
      description='Scraping Tokopedia',
      options = {"build_exe": build_exe_options},
      executables=executables
      )
