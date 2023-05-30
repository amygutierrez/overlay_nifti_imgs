from .info import __version__
version = __version__

#from .overlay_nifti import *
#__all__ = ['overlay_nifti']
from .overlay_nifti import overlay_nifti

if __name__ == '__main__':
    overlay_nifti()
