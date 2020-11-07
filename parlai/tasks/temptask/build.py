#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Download and build the data if it does not exist.

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data
import os

RESOURCES = [
    DownloadableFile(
        '1un69K0xVJMBZFUcFXd3A4SIN6S0XeWwb',
        'example.zip',  
        'b1ae68860782f21f2165f667fabc1372070abb2b2ad0a748a5c9ca454b4ea1b4',
        from_google=True,
    )
]

def build(opt):
    # get path to data directory
    dpath = os.path.join(opt['datapath'], 'example')
    # define version if any
    version = None

    # check if data had been previously built
    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')

        # make a clean directory if needed
        if build_data.built(dpath):
            # an older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # download the data.
        for downloadable_file in RESOURCES:
            downloadable_file.download_file(dpath)

        # mark the data as built
        build_data.mark_done(dpath, version_string=version)
