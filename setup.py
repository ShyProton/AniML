from setuptools import find_packages, setup

setup(
    name='animl',
    packages=find_packages(include=['animl']),
    version='0.1',

    author='Shayan Rashid',
    url='https://github.com/SaiProton/AniML',

    description='Visualize ML models with Manim',
    keywords=['ML', 'Visualization', 'Machine Learning', 'Manim'],

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],

    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=['manim', 'sklearn']
)
