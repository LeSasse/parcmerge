"""Provide utility functions to preprocess and manipulate parcellations."""

from warnings import warn

import numpy as np
from nilearn.image import new_img_like, resample_to_img


def detect_and_fill_nan(parc_array):
    """Find all NaN's and replace."""
    if np.isnan(parc_array).any():
        warn("Parcellation array contains NaN values, replacing with 0...")
        parc_array = np.nan_to_num(parc_array)

    return parc_array


def resample_if_needed(parc_one, parc_two):
    """Check image shapes and resample if not equal."""
    if parc_one.shape != parc_two.shape:
        warn(
            "Resampling the first parcellation according to the second "
            "due to different resolutions."
        )
        parc_one = resample_to_img(parc_one, parc_two, interpolation="nearest")

    return parc_one, parc_two


def merge_parcellations(parc_one, parc_two):
    """Merge two volumetric nifti parcellations.

    Parameters
    ----------
    parc_one : niimg
        First parcellation. This parcellation gets preference for voxels at
        which parcellations overlap.
    parc_two : niimg
        Second parcellation.

    Returns
    -------
    niimg
        The resulting parcellation after merging parc_one and parc_two.

    """
    parc_one, parc_two = resample_if_needed(parc_one, parc_two)

    # get both parcs as arrays + replace nan's if any
    parc_one_array = detect_and_fill_nan(np.array(parc_one.dataobj))
    parc_two_array = detect_and_fill_nan(np.array(parc_two.dataobj))

    n_roi_one = len(np.unique(parc_one_array[parc_one_array != 0]))
    n_roi_two = len(np.unique(parc_two_array[parc_two_array != 0]))

    # combine the parcellations
    if n_roi_one < n_roi_two:
        parc_one_array[parc_one_array != 0] += n_roi_two
    else:
        parc_two_array[parc_two_array != 0] += n_roi_one

    # parcellation one gets preference: only where it is 0 we overwrite values
    # from parcellation 1 with values from parcellation 2, ensuring that for
    # overlap, parcellation 1 stays the same.
    parc_one_array[parc_one_array == 0] += parc_two_array[parc_one_array == 0]

    # check how much overlap there is
    overlap = (parc_one_array != 0) & (parc_two_array != 0)
    overlap_sum = overlap.sum()
    warn(
        f"The parcellations overlap for {overlap_sum} voxels! For these "
        "voxels, labels are always set to the values from 'parc_one'."
        "If this is undesired, reverse the order of the arguments."
    )

    return new_img_like(parc_one, parc_one_array)
