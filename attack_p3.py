import sys
import time
L = []
def read_file(filename):
    """
    Reads the plaintext/ciphertext pairs from a file.

    Args:
        filename: The name of the file.

    Returns:
        A list of lists, where each sublist contains two 32-bit integers
        representing a plaintext/ciphertext pair.
    """
    filename = open(filename, 'r')
    for line in filename:
        #parse
        parsedLine = line.split("\t")
		
        plainText = parsedLine[0]
        ciphertext = parsedLine[1]
        plainText = plainText.split(' ')
        ciphertext = ciphertext.split(' ')
  
        #store
        y_plain = int(plainText[0])
        z_plain = int(plainText[1])
        y_cipher = int(ciphertext[0])
        z_cipher = int(ciphertext[1].strip())

        storedLine = [y_plain, z_plain, y_cipher, z_cipher]
        L.append(storedLine)
    print(L)
    print("File Found")

def attack(filename):
	print("> Guessing key")
	full_key_flag = False
	k0_guess = 0

	while not full_key_flag:
		delta = 0x9e3779b9		

		y = L[0][0]
		z = L[0][1]
		c = L[0][3]
		k1_compute_1 = ((c-y) ^ ((z<<4) + k0_guess) ^ (z + delta)) - (z>>5)

		y = L[1][0]
		z = L[1][1]
		c = L[1][3]
		k1_compute_2 = ((c-y) ^ ((z<<4) + k0_guess) ^ (z + delta)) - (z>>5)
		
		if k1_compute_1 == k1_compute_2:
			i = 2
			while i < 12:
				y = L[i][0]
				z = L[i][1]
				c = L[i][3]
				k1_compute_i = ((c-y) ^ ((z<<4) + k0_guess) ^ (z + delta)) - (z>>5)
				if k1_compute_i != k1_compute_1:
					break
				i += 1
			if k1_compute_i == k1_compute_1:
				full_key_flag = True

		#emergency loop abort
		if k0_guess > 9999999999:
			print("Guessing too high, assuming improper text pairs")
			break

		if not full_key_flag:
			k0_guess += 1

	if full_key_flag:
		print("> Keys found:\nK0 =",hex(k0_guess),"\nK1 =",hex(k1_compute_i))




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    start = time.time()

    filename = sys.argv[1]
    read_file(filename=filename)
    attack(filename)
    end = time.time()
    print("Time Elapsed: ", end - start)

'''	
Reads inputs in the format of two blocks of plaintext separated
by a space, then two blocks of corresponding ciphertext separated by space.
The plaintext and ciphertext are separated by a tab. Each line is expected
to be one pair of plaintext/ciphertext. The program reads in the lines to a
list, then it takes the first line and guesses a K0 value. It calculates the
K1 value based on that, then tests other plaintext/ciphertext pairs to see
if the K1 values match up. If they match up after 12 consecutive successes,
the K0 and K1 values are deemed to be the correct key values! If not, K0
increments until the correct values are found.
'''