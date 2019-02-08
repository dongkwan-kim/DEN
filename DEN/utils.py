import tensorflow as tf
from pprint import pprint
from termcolor import cprint


def print_all_vars(prefix: str = None, color=None):
    all_variables = tf.get_collection_ref(tf.GraphKeys.GLOBAL_VARIABLES)
    if prefix:
        cprint(prefix, color)
    pprint(all_variables)


def print_ckpt_vars(model_path, prefix: str = None, color=None):
    vars_in_checkpoint = tf.train.list_variables(model_path)
    if prefix:
        cprint(prefix, color)
    pprint(vars_in_checkpoint)
