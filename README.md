## Compression of Unix Timestamps with microseconds accuracy.
This problem arises in the context of disseminating large amounts of real time data efficiently.

The design of such a system has a few priorities and constraints.
1. One would want to minimize the amount of data that needs to be transferred
2. One would want to keep the decoding logic relatively simple so that decoding process is very efficient.
3. The coding/decoding algorithm needs to be an online algorithm (i.e. neither the coding nor the decoding logic knows in advance what data is going to be seen in future.) This rules out a lot of the standing data compression / decompression algorithms which rely on lookahead.

### Correctness of program:
timestamps -----> Coder -----> coded_timestamps -----> Decoder -----> decoded_timestamps

*decoded_timestamps should be identical to timestamps*

### Compiling instructions:

(Using python v2.7.10)

__Encoding__:
          
        python main.py --action=encode --input_file=timestamps.txt --output_file=encoded_data.bin --debug=1
      
__Decoding__:
        
        python main.py --action=decode --input_file=encoded_data.bin --output_file=decoded_data.txt --debug=1


### Options:

Option | Values | Purpose
-------|--------|-----
action | encode / decode | Action to perform. Takes either of the values `encode` or `decode`
input_file | <input_file> | Input file to be used.
output_file | <output_file> | Output file to be used.
debug | 0 / 1 | Run in debug mode. 1 Denotes True and 0 denotes False.

### Analysis:
For sample input located [here](https://goo.gl/PjFCri),

Total timestamps : 4,51,210

After compression,

File size : 722KB

Size per timestamp : 12.7815606924 bits

### What's next ?

You are welcome if you like to contribute. I believe the compression degree can still be improved.

Also, in case of any queries with the code here, feel free to drop me an email on aliaskar1024@gmail.com. 

Always happy to help ! :)
