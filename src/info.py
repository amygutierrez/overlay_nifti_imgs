# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 1
_version_minor = 0
_version_micro = 0
_version_extra = ''

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

description = 'Overlay nifti images'

long_description = """
==========================================
Overlay Nifti Images
==========================================

Open source package that allows user to overlay various
nifti masks over an antomical nifti image. You can add 
multiple masks at a time, which will each be overlayed
over the anatomical image provided.
An html file will automically open in your browser with 
all the overlayed plots.

Documentation
-------------
User documentation can be found here: https://github.com/amygutierrez/overlay_nifti_imgs
"""

NAME = 'overlay_nifti'
MAINTAINER = "C-PAC developers"
MAINTAINER_EMAIL = "CNL@childmind.org"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/amygutierrez/overlay_nifti_imgs"
DOWNLOAD_URL = "https://github.com/amygutierrez/overlay_nifti_imgs"
AUTHOR = "Amy Gutierrez"
AUTHOR_EMAIL = "amy.gutierrez@childmind.org"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
ISRELEASE = _version_extra == ''
VERSION = __version__
PYTHON_REQUIRES = ">= 3.5"
REQUIREMENTS = [
    "matplotlib>=3.7.1",
    "mpld3>=0.5.9",
    "nilearn>=0.10.1",
    "click>=8.1.3",
]