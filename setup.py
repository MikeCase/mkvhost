from setuptools import setup

setup(
    name='mk-vhost',
    version='1.01',
    py_modules=['mkvhost'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'python-cloudflare',
        'pystache'
    ],
    entry_points='''
        [console_scripts]
        mkvhost=mkvhost:cli
    ''',
)