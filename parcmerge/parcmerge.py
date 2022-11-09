from nilearn.image import load_img

from .utils import parse_args


def merge(parc_one, parc_two):
    pass


def main():

    # load both parcellations
    args = parse_args()
    parc_one, parc_two = load_img(args.parc_one), load_img(args.parc_two)

    # perform the merge
    merged_parc = merge(parc_one, parc_two)

    merged_parc.to_filename(args.outname)
