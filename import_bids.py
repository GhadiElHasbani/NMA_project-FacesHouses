import os.path as op
import numpy as np
import shutil
import scipy as sp

import nibabel as nib
from nilearn.plotting import plot_anat

import mne
from mne_bids import (BIDSPath, write_raw_bids, write_anat,
                      get_anat_landmarks, read_raw_bids,
                      search_folder_for_text, print_dir_tree,
                      template_to_head)

bids_root = "./data/BIDS"
subject = "ap"
session = "clean"
datatype= "ieeg"

bids_path = BIDSPath(root=bids_root, subject=subject, session=session, datatype=datatype)
print(bids_path)