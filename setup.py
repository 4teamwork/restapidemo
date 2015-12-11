from setuptools import setup, find_packages


version = '1.0.0.dev0'


tests_require = []


setup(name='restapidemo',
      version=version,
      url='https://github.com/4teamwork/restapidemo',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'plone.restapi',
        'plone.app.contenttypes',
        'ftw.inflator',
        'ftw.upgrade',
        'setuptools',
        ],

      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
