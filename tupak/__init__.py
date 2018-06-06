"""
tupak
=====

Tupak is The User friendly Parameter estimAtion Kode

The aim of tupak is to provide user friendly interface to perform parameter
estimation. It is primarily designed and built for inference of compact
binary coalesence events in interferometric data, but it can also be used for
more general problems.

For installation instructions see https://git.ligo.org/Monash/tupak

"""


from __future__ import print_function, division, absolute_import

# import local files, utils should be imported first
import tupak
from tupak.gw import detector, conversion, source, waveform_generator
from tupak.core import likelihood, prior, result, sampler, utils

# import a few often-used functions and classes to simplify scripts
from tupak.core.likelihood import Likelihood
from tupak.gw.likelihood import GravitationalWaveTransient
from tupak.gw.waveform_generator import WaveformGenerator
from tupak.core.sampler import run_sampler
