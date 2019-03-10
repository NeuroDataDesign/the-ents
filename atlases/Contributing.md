### Contributing to Neuroparc
For those who wish to contribute an atlas to this repository, you must submit the following in a PR:
* Nifti file containing a parcellated image
* JSON file containing the number, center, and name of each region. Please refer to the /atlases/labels for sample JSON files
* An updated atlas table with the information about the proposed atlas filled in

Before we approve the PR, we will run the atlas through our scripts to ensure the format is followed. We would appreciate it if you checked your atlas with the following scripts before submitting:
* Atlas_statistics.py
*Convert_to_[insert_name]_space.py
