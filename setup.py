from setuptools import setup, find_packages

version = "1.0.0"

setup(name="maahinkainen.portlet.googlecalendar",
    version=version,
    description="Simple Google Calendar events portlet.",
    long_description=open("README.txt").read() + "\n" +
                     open("HISTORY.txt").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords="",
    author="Asko Soukka",
    author_email="asko.soukka@iki.fi",
    url=("https://github.com/datakurre/"
        "maahinkainen.portlet.googlecalendar/"),
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["maahinkainen", "maahinkainen.portlet"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-'
        'PyXML', # for googlecalendar.py
        'icalendar', # for googlecalendar.py
        'gdata', # for googlecalendar.py and me
    ],
    extras_require={
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
    )
