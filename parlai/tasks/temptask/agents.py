#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import json
from parlai.core.teachers import FixedDialogTeacher
from parlai.core.teachers import ParlAIDialogTeacher
from parlai.utils.io import PathManager
from .build import build
import copy

def _path(opt, filtered):
    # build the data if it does not exist
    build(opt)
    print('11111111111111111')
    # set up path to data (specific to each dataset)
    dt = opt['datatype'].split(':')[0]
    return os.path.join(opt['datapath'], 'example', dt + '.tar.gz')
class DefaultTeacher(ParlAIDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)

        # get datafile
        opt['parlaidialogteacher_datafile'] = _path(opt, '')

        super().__init__(opt, shared)
    def num_episodes(self):
        return self.num_eps

    def num_examples(self):
        return self.num_exs
    

