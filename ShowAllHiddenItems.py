import os
import re
directory = 'C:\Program Files (x86)\Steam\steamapps\common\Halo Infinite\package\pc\en-US\gamecms'

# Provided by codeape on stack overflow: https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte
def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        file_bytes = list(bytes_from_file(filepath))
        quote_byte_found = False

        #print(bytes(file_bytes))
        #print(filepath)
        for index, byte in enumerate(file_bytes):
            if quote_byte_found and byte == 1:
                # If we found the quote byte in our previous run and \x01 in this run.
                file_bytes[index] = 0
                print('Found desired pattern in ' + filepath + ' at index ' + str(index))
                
            elif byte == 34: # If the byte we found is a double-quote.
                #print('found quote byte at ' + str(index))
                quote_byte_found = True

            else: # If we didn't find the correct byte sequence, reset our flag.
                quote_byte_found = False 

        with open(filepath, 'wb') as file:
            file.write(bytes(file_bytes))

        #print(bytes(file_bytes))
        #break
