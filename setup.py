from setuptools import setup

setup(
    name='myautomark',
    version='0.2',
    long_description=__doc__,
    packages=['myautomark'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask_sqlalchemy', 'waitress', 'cryptography']
)
