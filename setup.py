import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='dwl_router',
    version='0.0.1',
    url='http://github.com/slyboots/dwl_router',
    license='MIT',
    maintainer='slyboots',
    maintainer_email='dwl@dakotalorance.com',
    description='simple app for the Real Geeks Outgoing Leads API.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)