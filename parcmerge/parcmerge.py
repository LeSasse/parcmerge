from warnings import warn

import numpy as np
from nilearn.image import load_img, new_img_like

from .utils import detect_and_fill_nan, parse_args, resample_if_needed


def merge(parc_one, parc_two):

    parc_one, parc_two = resample_if_needed(parc_one, parc_two)

    # get both parcs as arrays + replace nan's if any
    parc_one_array = detect_and_fill_nan(np.array(parc_one.dataobj))
    parc_two_array = detect_and_fill_nan(np.array(parc_two.dataobj))

    n_roi_one = len(np.unique(parc_one_array[parc_one_array != 0]))
    n_roi_two = len(np.unique(parc_two_array[parc_two_array != 0]))

    # combine the parcellations
    if n_roi_one < n_roi_two:
        print("its schaefer")
        parc_one_array[parc_one_array != 0] += n_roi_two
        parc_one_array[parc_one_array == 0] += parc_two_array[
            parc_one_array == 0
        ]
        merged_array = parc_one_array
    else:
        parc_two_array[parc_two_array != 0] += n_roi_one
        parc_two_array[parc_two_array == 0] += parc_one_array[
            parc_two_array == 0
        ]
        merged_array = parc_two_array

    # check how much overlap there is
    overlap = (parc_one_array != 0) & (parc_two_array != 0)
    overlap_sum = overlap.sum()
    warn(f"The parcellations overlap for {overlap_sum} voxels!")

    return new_img_like(parc_one, merged_array)


def main():

    # load both parcellations
    args = parse_args()
    parc_one, parc_two = load_img(args.parc_one), load_img(args.parc_two)

    # perform the merge
    merged_parc = merge(parc_one, parc_two)

    merged_parc.to_filename(args.outname)
