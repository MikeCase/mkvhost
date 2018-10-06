from setuptools import setup

setup(
    name='mk-vhost',
    version='1.0',
    py_modules=['mkvhost'],
    include_package_data=True,
    install_requires=[
        'click',
        'CloudFlare',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        mkvhost=mkvhost:cli
    ''',
)