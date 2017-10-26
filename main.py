import argparse

from encoder import MyOnlineCoder
from decoder import MyOnlineDecoder


def get_args():
    """
    This method parses and returns the arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--action',
        choices=["encode", "decode"],
        required=True,
        help="Action to perform. Takes either of the values `encode` or `decode`"
    )

    parser.add_argument(
        '--input_file',
        required=True,
        help="Input file to be used."
    )

    parser.add_argument(
        '--output_file',
        required=True,
        help="Output file to be used."
    )

    parser.add_argument(
        '--debug',
        choices=['0', '1'],
        required=False,
        default=0,
        help="Run in debug mode. 1 Denotes True and 0 denotes False."
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = get_args()

    debug_mode = True if args.debug == '1' else False

    if args.action == "encode":
        print "******** ENCODING IN PROCESS ********"
        MyOnlineCoder(input_file=args.input_file, output_file=args.output_file).encode(debug_mode)
        print "******** ENCODING COMPLETED ********"
    else:
        print "******** DECODING IN PROCESS ********"
        MyOnlineDecoder(input_file=args.input_file, output_file=args.output_file).decode(debug_mode)
        print "******** DECODING COMPLETED ********"
