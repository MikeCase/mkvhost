from setuptools import setup

setup(
    name='mk-vhost',
    version='0.01',
    py_modules=['mkvhost', 'mkvhost.cflare', 'mkvhost.sysconfig'],
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