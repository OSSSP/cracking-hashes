import hashlib
import sys
import string

#Make sure user gives correct number of command line arguments
if(len(sys.argv) != 4):
  print("Usage:")
  print("python3 cracking_hashes.py [puzzle_name] [hashing_alg] [output_name]")
  sys.exit(1)

else:
  file_name = sys.argv[1]
  hash_alg = sys.argv[2]
  output_name = sys.argv[3]

  f = open(file_name, 'r')

  """
  lines contains each line of the file(w/o newlines character) starting from
  the 2nd line. 2nd line because plaintext of first line is empty string
  """
  lines = f.read().splitlines()[1:]
  plaintext = ""
  chars = []
  count = 0

  #Appends each printable character to chars
  for letter in string.printable:
    chars.append(letter)

  """
  The plaintext of each line is the plaintext of the previous line plus an
  additional character. This for loop goes thru each line and appends different
  characters to the plaintext until the hashed plaintext equals to the current
  line in the puzzle file
  """
  for line in lines:
    guess = plaintext
    for char in chars:
      guess = plaintext + char

      #The specified hashing algorithm is called from the hashlib library
      hash_object = getattr(hashlib, hash_alg)(guess.encode())
      hash_string = hash_object.hexdigest()

      if hash_string == line:
        plaintext = guess

        #This block of code is used to print out a progress bar
        count += 1
        percentage = int((count / len(lines)) * 20)
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*percentage, 5*percentage))
        sys.stdout.flush()

        #break since character found for line
        break

  f.close()

  #Puts each line at a separate index
  lines_plaintext = plaintext.splitlines()

  out_file = open(output_name, 'w')

  #Writes hash values to output file. Skips first line, since it is not hashed
  for line in lines_plaintext[1:]:
    out_file.write("%s\n" % line)

  out_file.close()

  #Prints out the first line
  print('\n',lines_plaintext[0])

