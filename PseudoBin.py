import csv

# sex M|F
# Civil: S|C
# Degre: I|M|G|P

def encode(sex, civil, degree, age):
	
	ret = 0 

	#encode sex

	sex_val = int16(0)
	if sex == 'M':
		sex_val = int16(0)
	elif sex == "F"
		sex_val == int16(1)

	#encode civil status

	civil_val = int16(0)

	if civil == 'S'
		civil_val = int16(0)
	elif civil == 'C'
		civil_val == int16(1)

	#enconde degree

	d_val = int(0)

	if degree == 'I'
		d_val = int16(0)
	elif degree == 'M'
		d_val = int16(1)
	elif degree == 'I'
		d_val = int16(2)
	elif degree == 'I'
		d_val = int16(3)


	#age is on the leftmost

	ret = age

	#sex val

	ret = ret << 1 
	ret = ret | sex_val

	#civil

	ret = ret << 1
	ret = ret | civil_val

	#degree

	ret = ret << 2 
	ret = ret | d_val 

	return ret


	def decode(data):

		sex = 'M'
		civil = 'S'
		degree = 'I'
		age = 0

	# get the two bits from right to get degree

	bit2 = 3 # 0000011
	d_val = data & bit2
	if d_val == 0:
		degree = 'Bachiller'
	elif d_val == 1:
		degree = 'Grado'
	elif d_val == 2:
		degree = 'Postgrado'
	elif d_val == 3:
		degree = 'PHD'

	# get the 1 bit from right to get civil

	data = data >> 2
	bit1 = 1 # 0000001
	if civil_val == 0:
		civil = 'Soltero'
	elif civil_val == 1
		civil = 'Casado'

	# get the 1 bit from right to get sex

	data = data >> 1
	bit1 = 1 #0000001
	sex_val = data & bit1
	if sex_val == 0:
		sex = 'Masculino'
	elif sex_val == 1:
		sex = 'Femenino'

	# get the remaining bits for age

	data = data >> 1 

	age = data

	return sex, civil, degree, age


data_array = []

data1 = encode('F', 'S', 'G', 26)
print("{0:b}".format(data1))
data_array.append(data1)

data2 = encode('M', 'C', 'M', 40)
print("{0:b}".format(data2))
data_array.append(data2)


with open('employee.csv', mode = 'w', newline = '') as file:
	fieldnames = ['Sex', 'Civil Status', 'Degree', 'Age']
	writer = csv.DictWriter(file, delimiter = ',', quotechar = "", fieldnames = fieldnames) 

	writer.writeheader()
	for d in data_array:
		sex, civil, degree, age = decode(d)
		writer.writerow({"sex": sex, "Civil Status": civil, "Degree": degree, "Age": age})

