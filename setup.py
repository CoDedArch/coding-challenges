from setuptools import setup

setup(
    author="Kelvin aka CoDed",
    author_email="kelvingbolo98@gmail.com",
    description="""A cli tool written in python which mimic linux/unix command wc behaviour.
    more info visit: https://codingchallenges.fyi/challenges/challenge-wc
    """,
    version="0.0.1",
    name="word_count",
    py_modules=["main", "getopt", "pyinstaller"],
    install_requires=[
        "getopt", "pyinstaller"
    ],
    entry_points={
        "console_scripts": [
            "py_wc = main:word_count",
        ],
    },
)