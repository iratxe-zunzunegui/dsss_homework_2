from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires
        # e.g., 'numpy', 'pandas',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz', 
        ],
    },
    author='Iratxe',
    author_email='iratxe.zunzunegui@gmail.com',
    description='A simple math quiz game.',
    license='Apache License 2.0',
    url='https://github.com/iratxe-zunzunegui/dsss_homework_2',  
)
