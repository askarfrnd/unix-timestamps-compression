#!/usr/bin/env python
"""Decoding unix timestamps (with microseconds) effectively.

This problem arises in the context of disseminating large amounts of real time data
efficiently.
"""

from __future__ import division
import os
from numpy import binary_repr as convert_to_binary

__author__ = "Ali Askar A"
__copyright__ = "Copyright 2017, Planet Earth"
__credits__ = ["Ali Askar A"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ali Askar"
__email__ = "aliaskar1024@gmail.com"
__status__ = "Production"


class MyOnlineDecoder:
    """
    A Decoder class that perform decoding of data to timestamps.

    Args:
        input_file: This is the encoded data file.
        output_file: This is file to store timestamps.
    """

    CODE_BYTES_MAP = {"00": 1, "01": 2, "10": 3, "11": 4}

    def __init__(self, input_file, output_file):
        self.inputFile = open(input_file, "rb")
        self.outputFile = open(output_file, "w")

    def __perform_write(self, data):
        """
        Writes given data to file.
        """

        self.outputFile.write(data)

    def __perform_padding(self, s):
        """
        Perform padding on given data to 8 bits (if required).
        """

        return s.zfill(8)

    def __clean_timestamp(self, timestamp):
        """
        Performs cleaning of timestamp.
        """

        return str(timestamp)[:-6] + "." + str(timestamp)[-6:]

    def __on_success(self, debug):
        """
        Trigger to perform various actions on decoding completion.
        """

        if debug:
            print "File size (output) : ", os.fstat(self.outputFile.fileno()).st_size

        self.inputFile.close()
        self.outputFile.close()

    def decode(self, debug=False):
        """
        Decodes the data to timestamps and write those to output file.
        """

        previous_timestamp = int(self.inputFile.read(16))

        flag = False
        temp = ""

        for ind, decimal in enumerate(bytearray(self.inputFile.read())):
            binary_repr = self.__perform_padding(convert_to_binary(decimal))

            if not flag:
                # Get to know what byte current timestamp is stored.
                byte_size = self.CODE_BYTES_MAP.get(binary_repr[:2])
                ind_timestamp_end = ind + byte_size
                flag = True

            if ind < ind_timestamp_end:
                # Append all bytes of timestamp to `temp`.
                temp += binary_repr

                if ind + 1 == ind_timestamp_end:
                    # Generate each timestamp by difference.
                    difference = int(temp[2:], 2)
                    timestamp = previous_timestamp + difference
                    self.__perform_write("%s\n" % self.__clean_timestamp(timestamp))
                    previous_timestamp = timestamp
                    flag = False
                    temp = ""

        self.__on_success(debug)