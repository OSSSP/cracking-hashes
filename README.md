# Cracking Hashes
## Goal
The goal of this project is to crack the hashes contained in the file
puzzle.txt

## Solving the puzzle
Taking a look at puzzle.txt, we can see that the file contains 100072 hashed
lines. Due to the file containing this many number of lines, brute forcing is
really not a viable solution. Examining the file more closely, we can see that
each line contains 32 hexadecimal digits (128 bits), which probably means its
an MD5 hash.

Let us see if the website crackstation.net can crack the hashes for us.
Entering the first 20 lines of puzzle.txt on crackstation.net:
![Image of crackstation 1](https://github.com/haseebT/cracking-hashes/blob/master/screenshots/Screen%20Shot%202018-07-24%20at%208.45.50%20PM.png)

Unfortunately, the website is only able to crack the first 4 lines. But,
observing more closely, we can see that the plaintext of the 4th line (Who)
is the plaintext of the 3rd line (Wh) plus an additional character. The same
holds true for the 3rd and 2nd line, and for the 2nd and 1st line.

Knowing this, we can write a python script cracking_hashes.py to solve the
puzzle. The script takes in 3 command line arguments (file name of puzzle,
hashing algorithm used by the puzzle file, and the name of the output file),
and uses the fact that the plaintext of a line is the plaintext of the
previous line plus an additional character to crack the hashes.

Running the script:
![Gif 1](https://github.com/haseebT/cracking-hashes/blob/master/gifs/2018-07-24%2021.38.24.gif)

After running the script, we see that the first line outputted by our script
is `Who designed both RC5 and MD5?` (Answer: Ronald Rivest).
The rest of the lines were written to output.txt

Opening up output.txt, we see that it is another file containing hashed lines,
but instead of each line being 32 hexadecimal digits, each line is actually
40 hexadecimal digits (160 bits). This makes it likely that each line was 
hashed using SHA-1.

Again, entering the first 20 lines of output.txt on crackstation.net, we get:
![Image of crackstation 2](https://github.com/haseebT/cracking-hashes/blob/master/screenshots/Screen%20Shot%202018-07-24%20at%2010.03.25%20PM.png)

Like last time, the website is only able to crack the first few lines. But,
again like last time, the plaintext of each line is the plaintext of the
previous line plus an additional character. This means that we can again use
our script, but this time instead of giving the command line argument 'md5'
we give 'sha1' since that is the hashing algorithm used in this file.

Running the script for output.txt:
![Gif 2](https://github.com/haseebT/cracking-hashes/blob/master/gifs/2018-07-24%2022.15.30.gif)

This time we see that the first line outputted by our script is
`What organization designed SHA-1?` (Answer: NSA).
The rest of the lines were written to output2.txt

Doing the same thing we've previously been doing, opening the output2.txt file
shows hashed lines, with each line containing 64 hexadecimal digits (256 bits).
This likely means the lines were hashed using either SHA2-256 or SHA3-256.

Entering the first 20 lines of output2.txt on crackstation.net, we get:
![Image of crackstation 3](https://github.com/haseebT/cracking-hashes/blob/master/screenshots/Screen%20Shot%202018-07-24%20at%2010.35.03%20PM.png)

This time, the website is unable to crack any of the lines. Since
crackstation.net only supports SHA2-256 between SHA2-256 and SHA3-256, let us
see if our script will work on output2.txt using SHA3-256.

Running the script for output2.txt:
![Gif 3](https://github.com/haseebT/cracking-hashes/blob/master/gifs/2018-07-24%2022.47.35.gif)

The first line outputted by our script is
`Who co-developed both AES and SHA-3?` (Answer: Joan Daemen).

Opening output3.txt shows that it is an empty file, which means that we have
finally solved the puzzle :)
