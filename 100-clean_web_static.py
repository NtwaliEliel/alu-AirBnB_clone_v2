#!/usr/bin/python3
# script to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["54.82.5.102", "3.94.103.18"]


