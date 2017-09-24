from setuptools import setup

setup(
    name='shell-vcr',
    description='Shell-VCR is a tool to intercept, record and replay shell commands.',
    url='https://github.com/HerrSpace/shell-vcr',
    author='Patrick <HerrSpace> Meyer',
    license='MIT',
    version='0.1',
    scripts=['shell-vcr'],
    install_requires=[
        'Fabric',
    ],
)
