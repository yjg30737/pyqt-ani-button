from setuptools import setup, find_packages

setup(
    name='pyqt-ani-button',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QPushButton for animation',
    url='https://github.com/yjg30737/pyqt-ani-button.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-ani-abstractbutton>=0.0.1'
    ]
)