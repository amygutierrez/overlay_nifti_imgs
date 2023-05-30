Overlay Nifti Images
=====================
Tool to overlay multiple masks over nifti image

Instead of using viewers for overlaying nifti images, you can add multiple masks to overlay on an anatomical brain. Each nifti mask will be plotted over the anatomical brain nifti image in an html file.

<b>Installation</b>
---------------
To pip install:
```
pip install git+https://github.com/amygutierrez/overlay_nifti_imgs.git
```

If you cannot pip install, you can clone the repo:
```
git clone git@github.com:amygutierrez/overlay_nifti_imgs.git
```
<b>Options</b>
---------------
Usage: `overlay_nifti [OPTIONS]`

Options:
```
  -a, --anat TEXT     Path to anatomical nifti image that will be the underlay
                      brain image. This image is usuallu in MNI152 template
                      space  [required]
  -o, --overlay TEXT  Path to nifti image that will overlay the anatimcal
                      image.  [required]
  --nobrowser         Please add this flag if you are not on a system that has
                      a web broweser.
  --save TEXT         If you would like to save the html report automatically,
                      supply the name and path name for the report.
  --help              Show this message and exit.
  ```

<b>Usage Exampels</b>
---------------
- This tool creates an html report of the various mask overlays provided. By default, it will open the html report in your browser (preferably Chrome). 
```
overlay_nifti \
--anat /home/username/space-MNI152NLin6ASym_desc-head_T1w.nii.gz \
--overlay /home/username/space-MNI152NLin6ASym_desc-brain_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-CSF_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-WN_mask.nii.gz
```
 ** Notice, if you want to add multiple overlays, make sure each image is separated by a comma (,) and **no** spaces. **

- If you are not on a system with a broswer, here is an example of how to use the tool:
```
overlay_nifti \
--anat /home/username/space-MNI152NLin6ASym_desc-head_T1w.nii.gz \
--overlay /home/username/space-MNI152NLin6ASym_desc-brain_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-CSF_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-WN_mask.nii.gz \
--nobroswer \
--save /home/username/overlay_report.html
```
 ** Notice, if you will need to add the flags `--nobrowser` *and* `--save /path/to/file.html` 

- If you cannot pip install on system and have decided to clone this repo instead, you can still use the tool:
```
python3 /path/to/repo/overlay_nifti_imgs/overlay_nifti.py \
--anat /home/username/space-MNI152NLin6ASym_desc-head_T1w.nii.gz \
--overlay /home/username/space-MNI152NLin6ASym_desc-brain_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-CSF_mask.nii.gz,/home/username/space-MNI152NLin6ASym_label-WN_mask.nii.gz
```

<b>Uninstall</b>
---------------
To uninstall, simply
```
pip uninstall overlay_nifti_imgs
```
