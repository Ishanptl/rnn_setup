import os, glob, random
import pretty_midi
import numpy as np
from keras.models import model_from_json
from multiprocessing import Pool as ThreadPool


def main():