# coding: utf-8


from setuptools import setup


setup(
    name="apt_mirror_check",
    version="1.0.3",
    description="Check corrupted files downloaded by apt-mirror",
    license="MIT",
    author="Openov Sergey",
    author_email="openov_s@mail.ru",
    py_modules=["apt_mirror_check"],
    url="https://github.com/konelav/apt_mirror_check",
    entry_points={
        "console_scripts": [
            "apt-mirror-check = apt_mirror_check:cli"
        ]
    }
)
