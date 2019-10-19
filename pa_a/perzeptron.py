import random
import sys

def concat_string(string_vector):
	output = ""
	for x in string_vector:
		output += str(x) + " "
	return output

def weight_sum(input_vector):
	sumw = 0
	for i in input_vector:
		sumw += i*(random.randint(-5,5)/10)
	sumw += random.randint(-5,5)/10
	if sumw > 0:
		return 1
	else:
		return 0

def main(input_file):
	with open(input_file) as f:
		input_data = [lines.rstrip('\n') for lines in f]
		for line in input_data:
			if "#" not in line:
				inputs = line.split(" 	")
				x = inputs[0][1:].split(" ")
				y = inputs[1].split(" ")
				i = 0
				output = []
				while i < len(x):
					x[i] = int(x[i])
					i += 1
				i = 0
				while i < len(y):
					output.append(weight_sum(x))
					i += 1
				print("Generated Result: " + concat_string(output) + "Desired Result: " + concat_string(y))

if __name__ == '__main__':
	main(sys.argv[1])