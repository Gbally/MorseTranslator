#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
#            MorseTranlator Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : MorseTranlator.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2019/02/25     Creation - Words to morse
0.2.0     2019/02/26     Added: Morse to words
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import re
import sys

from MorseCode import MorseCode
mc = MorseCode()

# from SoundMaker import SoundMaker
# sm = SoundMaker()

from wavebender import *

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2019/02/25'
__version__ = '0.2.0'
__maintainer__ = 'Guillaume'

# [GLOBALS]---------------------------------------------------------------------


# [Functions]-------------------------------------------------------------------
class MorseTranlator:

    def __init__(self):
        self.morse_dic = mc.morse

        # Dictionary has letter as key and code morse as value,
        # it is reversed to translate from morse to words
        try:
            # For python2
            self.morse_dic_reversed = {v: k for k, v in self.morse_dic.iteritems()}
        except AttributeError:
            # For python3
            self.morse_dic_reversed = {v: k for k, v in self.morse_dic.items()}

        # self.generate_sound("test.wav", 440.0, 44100, 0.5, 2, 5, 16)
        self.generate_sound()

    def translate(self, s):
        """
        Check first charater to define if s has to be translated to morse or
        decoded to a string.
        :param s: Input to translate
        """
        try:
            if s[0].isalpha():
                return self.words_to_morse(s)

            elif s[0] is "-" or ".":
                return self.morse_to_words(s)

        except TypeError:
            print("ERROR")

    def words_to_morse(self, s):
        """
        Will translate every letter to its morse code
        :param s: Words
        :return: Morse code
        """
        # Force element to be lower
        elements = [e.lower() for e in s]
        output = " ".join(self.morse_dic.get(e) for e in elements)

        print("DEBUG:Output words_to_morse: {}".format(output))
        return output

    def morse_to_words(self, s):
        """
        Will stack morse code and then translate to words
        :param s: Morse code
        :return: English
        """
        elements = re.split(" ", s)
        output = "".join([self.morse_dic_reversed.get(e) for e in elements])

        print("DEBUG: Output morse_to_words: {}".format(output))
        return output

    # def generate_sound(self, filename, frequency, rate, amplitude, channels,
    #                    time, bits):
    #     # each channel is defined by infinite functions which are added
    #     # to produce a sample.
    #     channels = ((sm.sine_wave(frequency, rate, amplitude),) for i in
    #                 range(channels))
    #
    #     # convert the channel functions into waveforms
    #     samples = sm.compute_samples(channels, rate * time)
    #
    #     # write the samples to a file
    #     if filename == '-':
    #         filename = sys.stdout
    #     else:
    #         filename = filename
    #         sm.write_wavefile(filename, samples, rate * time,
    #                             channels, bits / 8, rate)


    def generate_sound(self):
        file = "test.wav"
        # channels = (self.violin(),)
        # samples = compute_samples(channels, 44100 * 60 * 1)
        # file = "test.wav"
        # write_wavefile(file, samples, 44100 * 60 * 1, nchannels=1)

        channels = ((sine_wave(500.0, amplitude=0.1),),
                    (sine_wave(500.0, amplitude=0.1),))

        samples = compute_samples(channels, 44100 * 10)
        write_wavefile(file, samples)
