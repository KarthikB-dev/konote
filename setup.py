import sys
import setuptools

# Thank you @r2dev2 (Ronak Badhe) and @KentoNishi for this setup.py

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = "A notetaking application using evidence based study techniques"

try:
    with open("requirements.txt", "r") as reqs:
        requirements = reqs.read().split("\n")
except:
    requirements = ""

try:
    if "refs/tags/v" in sys.argv[1]:
        versionName = sys.argv[1].replace("refs/tags/v", "")
        del sys.argv[1]
    else:
        raise Exception
except:
    versionName = "0.1.0"

setuptools.setup(
    name="konote",
    version=versionName,
    author="Karthik Bhattaram",
    author_email="saberlight35@gmail.com",
    description=long_description.split("\n")[1],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KarthikB-dev/konote.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: GNU/Linux",
    ],
    entry_points={"console_scripts": ["konote=konote:main"]},
    python_requires=">=3.7",
    install_requires=requirements,
)
