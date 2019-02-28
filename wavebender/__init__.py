#!/usr/bin/env python
"""
An audio synthesis library for Python.

It makes heavy use of the `itertools` module.
Good luck! (This is a work in progress.)
"""
import sys
import math
from . import wave
import struct
import random
from itertools import count, islice

try:
    from itertools import zip_longest
except ImportError:
    from itertools import imap as map
    from itertools import izip as zip
    from itertools import izip_longest as zip_longest

try:
    stdout = sys.stdout.buffer
except AttributeError:
    stdout = sys.stdout

# metadata
__author__ = 'Zach Denton'
__author_email__ = 'zacharydenton@gmail.com'
__version__ = '0.4'  # Modification made to fit the MorseTranslator project
__url__ = 'http://github.com/zacharydenton/wavebender'
__longdescr__ = '''An audio synthesis library for Python.'''
__classifiers__ = ['Topic :: Multimedia :: Sound/Audio :: Sound Synthesis']


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5,
        skip_frame=0):
    '''
    Generate a sine wave at a given frequency of infinite length.
    '''
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    for i in count(skip_frame):
        sine = math.sin(2.0 * math.pi * float(frequency) * (float(i) / float(framerate)))
        yield float(amplitude) * sine


def square_wave(frequency=440.0, framerate=44100, amplitude=0.5):
    for s in sine_wave(frequency, framerate, amplitude):
        if s > 0:
            yield amplitude
        elif s < 0:
            yield -amplitude
        else:
            yield 0.0


def damped_wave(frequency=440.0, framerate=44100, amplitude=0.5, length=44100):
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    return (math.exp(-(float(i%length)/float(framerate))) * s for i, s in enumerate(sine_wave(frequency, framerate, amplitude)))


def white_noise(amplitude=0.5):
    '''
    Generate random samples.
    '''
    return (float(amplitude) * random.uniform(-1, 1) for i in count(0))


def compute_samples(channels, nsamples=None):
    '''
    create a generator which computes the samples.

    essentially it creates a sequence of the sum of each function in the channel
    at each sample in the file for each channel.
    '''
    return islice(zip(*(map(sum, zip(*channel)) for channel in channels)), nsamples)


def write_wavefile(w, samples, nframes=None, nchannels=2, sampwidth=2,
                   framerate=44100, bufsize=2048):
    "Write samples to a wavefile."
    if nframes is None:
        nframes = 0

    # w = wave.open(f, 'wb')
    w.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    # split the samples into chunks (to reduce memory consumption and improve
    # performance)
    for chunk in grouper(bufsize, samples):
        return b''.join(b''.join(struct.pack('h', int(max_amplitude * sample))
                                for sample in channels) for channels in chunk if channels is not None)
        # w.writeframesraw(frames)
    
    # w.close()


def init_wave(f):
    return wave.open(f, 'wb')


def write_frames(w, frames):
    w.writeframesraw(frames)


def close_wave(w):
    w.close()
