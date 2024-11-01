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
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Adjust the entry point if the function name changes
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='A simple math quiz game.',
    license='Apache License 2.0',
    url='https://github.com/iratxe-zunzunegui/dsss_homework_2',  # Replace with your repo URL
)
