from setuptools import find_packages, setup

setup(
    name='animl',
    packages=find_packages(),
    version='0.1.0',
    description='Visualize ML models with Manim',
    author='SaiProton',
    license='MIT',
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pandas'],
    install_requires=['manim', 'sklearn', 'numpy']
)
