# parcmerge

A command line tool to merge two distinct nifti parcellations. 
It is mainly intended to be used for combining cortical and subcortical parcellations.

# Set up

You may or may not want to set up a virtual environment. 

```sh
python3 -m venv .examplevenv
source .examplevenv/bin/activate
pip install -U pip
```
Then clone the repository to where you would like to install it.
```
git clone https://github.com/LeSasse/parcmerge.git
cd parcmerge
pip install -e .
```

# How to use

It is relatively simple. For help run `parcmerge --help`.

```
usage: parcmerge [-h] parc_one parc_two outname

Merge two parcellation nifti files in volumetric space.
This is intended to be used for combination of
subcortical (i.e. TIAN) and cortical (i.e. Schaefer)
parcellations.

positional arguments:
  parc_one    The first parcellation. This parcellation
              gets preference for voxels at which the
              two parcellations overlap. If there is
              overlap between the two parcellations,
              make sure this is the parcellation that
              is supposed to get preference.
  parc_two    The second parcellation.
  outname     The path/filename for the output file

optional arguments:
  -h, --help  show this help message and exit
```

You can also use the package to merge parcellations in python code:

```python3
from parcmerge import merge_parcellations

merged_parcellation = merge_parcellations(parc_one, parc_two)
```