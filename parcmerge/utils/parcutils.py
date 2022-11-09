"""Provide utility functions to clean and preprocess parcellation data."""

from warnings import warn

import numpy as np
from nilearn.image import resample_to_img


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
