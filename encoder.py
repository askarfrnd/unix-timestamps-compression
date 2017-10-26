#!/usr/bin/env python
"""Encoding unix timestamps (with microseconds) effectively.

This problem arises in the context of disseminating large amounts of real time data
efficiently.
"""

from __future__ import division
import os
import math
from numpy import binary_repr as convert_to_binary

__author__ = "Ali Askar A"
__copyright__ = "Copyright 2017, Planet Earth"
__credits__ = ["Ali Askar A"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ali Askar"
__email__ = "aliaskar1024@gmail.com"
__status__ = "Production"


class MyOnlineCoder:
    """
    A Encoder class that perform encoding of given timestamps.

    Args:
        input_file: This is the timestamps data file.
        output_file: This is file to store encoded data.
    """

    BITS_CODE_MAP = {8: "00", 16: "01", 24: "10", 32: "11"}

    def __init__(self, input_file, output_file):
        self.inputFile = open(input_file, "r")
        self.outputFile = open(output_file, "wb")

    def __read_next_line(self):
        """
        Returns one line at a time from the file.
        """

        return self.inputFile.readline().strip()

    def __perform_write(self, data):
        """
        Writes given data to file.
        """

        self.outputFile.write(data)

    def __get_size(self, number):
        """
        Returns the expected size (in bits) for given number.
        """

        return int(math.ceil(number / 8.0)) * 8

    def __binary_to_decimal(self, number):
        """
        Returns corresponding decimal number for given `number` (binary).
        """

        return int(number, 2)

    def __code_time_stamp(self, timestamp):
        """
        Encode a timestamp and store it to file.
        """

        timestamp = timestamp.replace(".", "")
        int_ts = int(timestamp)

        if not hasattr(self, 'counter'):
            self.counter = 0
            self.previous_timestamp = int_ts
            self.__perform_write(timestamp)

        # Calculating difference of the current timestamp from previous one.
        difference = int_ts - self.previous_timestamp
        self.previous_timestamp = int_ts

        binary_repr = convert_to_binary(difference)

        # Calculate required size in bits for the timestamp.
        bit_size = self.__get_size(len(binary_repr) + 2)

        # Add bit size as first 2 chars and perform padding with zeros until size is reached.
        bit_size_code = self.BITS_CODE_MAP.get(bit_size)
        remaining_bits = bit_size - (len(binary_repr) + 2)
        timestamp_sized = bit_size_code + ("0" * remaining_bits) + binary_repr

        # Splitting to various 1 byte strings
        one_byte_strings = [timestamp_sized[i:i + 8] for i in range(0, len(timestamp_sized), 8)]

        # Getting decimal corresponding to each byte.
        decimals = [self.__binary_to_decimal(byte) for byte in one_byte_strings]

        # Writing bytes into file
        self.__perform_write(bytearray(decimals))

        self.counter += 1

        return difference

    def __on_success(self, debug):
        """
        Trigger to perform various actions on encoding completion.
        """

        if debug:
            print "File size : ", os.fstat(self.outputFile.fileno()).st_size
            print "Size per timestamp (in bits)", os.fstat(self.outputFile.fileno()).st_size / self.counter * 8
        self.inputFile.close()
        self.outputFile.close()

    def encode(self, debug=False):
        """
        Encodes the timestamps and write it to output file.
        """

        while True:
            timestamp = self.__read_next_line()
            if timestamp:
                self.__code_time_stamp(timestamp)
                continue
            break

        self.__on_success(debug)