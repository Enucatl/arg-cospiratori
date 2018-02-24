from setuptools import setup, find_packages
setup(
    name="cospiratoribot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "decorator",
        "python-telegram-bot",
        "numpy",
        "click",
    ]
)
