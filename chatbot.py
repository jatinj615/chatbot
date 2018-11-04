# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import re
import time

## Import Dataset
lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
lines = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
