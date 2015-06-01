__author__ = 'ralph'

"""A module for dealing with BMP bitmap image files."""

# Dealing with 8-bit grayscale images because the have the nice principle of
# accepting one byte per pixel
def write_grayscale(filename, pixels):
    # Each inner-list is row of pixels from left to right
    # Outer list is a list of pixel rows from top to bottom

    """Creates and writes a grayscale BMP files.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of intergers in the range 0-255.

    Raises:
        OSError: If the file couldn't be written.
    """
    # Get the size of the image. Assumed that all rows have the same length.
    # In production code, this should be checked.
    height = len(pixels)    # number of rows
    width = len(pixels[0])  # items in the zero row to get the width

    with open(filename, 'wb') as bmp:   # File opened in binary mode. Encoding makes no sense for raw binary files
        #BMP Header
        bmp.write(b'BM')    # BM identifies it as a BMP file. Magic header.

        size_bookmark = bmp.tell()      # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.
        # 'little-endian' means least significant byte is written first

        bmp.write(b'\x00\x00')      # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')      # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next four bytes hold the integer offset
        bmp.write(b'\x00\x00\x00\x00')      # to the pixel data. Zero placeholder for now.

        # Image Header
        # First thing is to write the length as a 32-bit integer
        bmp.write(b'\x28\x00\x00\x00')  # Image header size in bytes - 40 decimal; hardwire - 0x28 == 40
        bmp.write(_int32_to_bytes(width))   # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')          # Number of image planes
        bmp.write(b'\x08\x00')          # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))      # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):    # BMP files are bottom to top
            row_data = bytes(row)      # bytes constructor will raise a ValueError if argument is outside of the 0 - 255 range
            bmp.write(row_data)
            # Each row of pixel data must be a multiple of 4 bytes long irrespective of the image width
            #
            padding = b'\x00' * (4 - (len(row) % 4))    # Pad row to multiple of four bytes
            bmp.write(padding)

        #End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

    def dimensions(filename):
        """Determine the dimensions in pixels of a BMP image.

        Args:
            filename: The filename of a BMP file.

        Returns:
            A tuple containing two integers with the width of height in pixels.

        Raises:
            ValueError: If the file was not a BMP file.
            OSError: If there was a problem reading the file.
        """
        with open(filename, 'rb') as f:
            magic = f.read(2)
            if magic != b'BM':  # Simple validation check by looking at the header
                raise ValueError("{} is not a BMP file".format(filename))

            f. seek(18)
            width_bytes = f.read(4)
            height_bytes = f.read(4)

            return (_bytes_to_int32(width_bytes),
                    _bytes_to_int32(height_bytes))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    return bytes((i & 0xff,     # bitwise and uses & rather than logical AND
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff,))



