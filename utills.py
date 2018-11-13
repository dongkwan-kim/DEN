import tensorflow as tf
from pprint import pprint


def print_all_vars(prefix: str = None):
    all_variables = tf.get_collection_ref(tf.GraphKeys.GLOBAL_VARIABLES)
    if prefix:
        print(prefix)
    pprint(all_variables)


def print_ckpt_vars(model_path, prefix: str = None):
    vars_in_checkpoint = tf.train.list_variables(model_path)
    if prefix:
        print(prefix)
    pprint(vars_in_checkpoint)
