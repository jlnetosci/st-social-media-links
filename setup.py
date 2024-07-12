from setuptools import setup, find_packages

# Read the contents of your README file to use as the long description
with open("README_for_pypi.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="st-social-media-links",
    version="0.1.3",
    description="A Python package designed to assist in displaying social media links within Streamlit apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="João L. Neto",
    url="https://github.com/jlnetosci/st_social_media_links",
    keywords = "streamlit social media links",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.32.0",
        "beautifulsoup4>=4.12.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
