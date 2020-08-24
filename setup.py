from setuptools import find_packages, setup

setup(
    name='volunteer-example',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='An example volunteering site',
    url='https://github.com/howardosborne/volunteer_example.git',
    author='Howard Osborne',
    author_email='howardosborneconsulting@gmail.com',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'flask',
        'lxml',
    ],
)