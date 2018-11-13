#!/bin/bash

# download_data.sh
# Created by Vivek Gopalakrishnan on 2018-11-13.
# Email: vgopala4@jhu.edu
# Copyright (c) 2018. All rights reserved.

# Size: ~5 GB
aws s3 cp s3://neurodatadesign/hbn/derivatives/graphs/ ../../data/raw/hbn/ --no-sign-request --recursive

# Size: ~10 GB
# aws s3 cp s3://mrneurodata/data/HNU1/ndmg_0-0-48/graphs/ ../../data/raw/hnu1/ --no-sign-request --recursive
