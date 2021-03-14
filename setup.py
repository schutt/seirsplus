import setuptools

setuptools.setup(
    packages=setuptools.find_packages(),
    name="seirsplus",
    version="1.0.9",
    description="Models of SEIRS epidemic dynamics with extensions, including network-structured populations, testing, contact tracing, and social distancing.",
    url="https://github.com/ryansmcgee/SEIRS-network-model",
    author="Ryan Seamus McGee",
    author_email="ryansmcgee@gmail.com",
    license="MIT",
    install_requires=["numpy", "scipy", "networkx"],
    zip_safe=False,
)
