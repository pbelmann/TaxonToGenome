__author__ = 'root'

import shutil
import os.path


def cleanup(context):
    output_dir = os.path.join(context._config.base_dir, "output")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)


def before_scenario(context, scenario):
    cleanup(context)


def after_scenario(context, scenario):
    print("fa")
  #  cleanup(context)