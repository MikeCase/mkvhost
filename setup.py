from setuptools import setup

setup(
    name='mk-vhost',
    version='0.01',
    py_modules=['mkvhost', 'cloudflare.cflare', 'cloudflare.sysconfig'],
    include_package_data=True,
    install_requires=[
        'requests',
        'pystache'
    ],
    entry_points='''
        [console_scripts]
        mkvhost=mkvhost:cli
    ''',
)