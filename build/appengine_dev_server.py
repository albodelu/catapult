#!/usr/bin/python
# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

from build import module_finder
from build import temp_deployment_dir


def DevAppserver(paths):
  """Starts a dev server for an App Engine app.

  Args:
    paths: List of paths to files and directories that should be linked
        (or copied) in the deployment directory.
  """
  try:
    import dev_appserver  # pylint: disable=unused-variable
  except ImportError:
    # TODO(qyearsley): Put the App Engine SDK in the path with the
    # binary dependency manager.
    print 'This script requires the App Engine SDK to be in PYTHONPATH.'
    sys.exit(1)
  with temp_deployment_dir.TempDeploymentDir(paths) as temp_dir:
    print 'Running dev server on "%s".' % temp_dir
    subprocess.call([
        module_finder.FindModule('dev_appserver'),
        temp_dir,
    ])
