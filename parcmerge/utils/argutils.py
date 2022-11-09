import argparse


def parse_args():
    """Parse arguments for the CLI."""

    parser = argparse.ArgumentParser(
        description=(
            "Merge two parcellation nifti files in volumetric space. This is "
            "intended to be used for combination of subcortical (i.e. TIAN) "
            "and cortical (i.e. Schaefer) parcellations."
        )
    )

    parser.add_argument(
        "parc_one",
        metavar="parc_one",
        type=str,
        help=("The first parcellation."),
    )
    parser.add_argument(
        "parc_two",
        metavar="parc_two",
        type=str,
        help=("The second parcellation."),
    )
    parser.add_argument(
        "outname", help=("The path/filename for the output file")
    )

    return parser.parse_args()
