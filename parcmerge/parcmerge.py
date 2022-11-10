"""Provide entry point for command line tool."""

from nilearn.image import load_img

from . import merge_parcellations
from .utils import parse_args


def main():
    """Run the command line tool."""
    # load both parcellations
    args = parse_args()
    parc_one, parc_two = load_img(args.parc_one), load_img(args.parc_two)

    # perform the merge
    merged_parc = merge_parcellations(parc_one, parc_two)

    merged_parc.to_filename(args.outname)
