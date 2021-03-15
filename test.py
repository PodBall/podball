# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:41:29 2021

@author: Marshall.McDougall
"""
#import argparse
#import numpy as np
#import shlex
#import subprocess
#import sys
#import wave
#import json

from deepspeech import Model#, version
#from timeit import default_timer as timer

#try:
#    from shhlex import quote
#except ImportError:
#    from pipes import quote
# deepspeech --model deepspeech-0.9.3-models.pbmm --scorer deepspeech-0.9.3-models.scorer --audio audio/SimpleTest3.wav --json

ds = Model("deepspeech-0.9.3-models.pbmm")
desired_sample_rate = ds.sampleRate()
ds.enableExternalScorer("deepspeech-0.9.3-models.scorer")
ds.sttWithMetadata("audio/SimpleTest3.wav", "3")