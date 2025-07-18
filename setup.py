
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="vibecheck",
    version="0.1.0",
    author="Chase Hudson",
    author_email="chase.w.hudson@gmail.com",
    description="A linter for good vibes only.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chasehudson/vibecheck", # Replace with your GitHub repo URL
    py_modules=["vibecheck"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "vibecheck=vibecheck:main",
        ]
    },
)
