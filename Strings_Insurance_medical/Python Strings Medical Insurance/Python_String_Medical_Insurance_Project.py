# 1 - Print medical_data to see the output below the code block.

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

print(medical_data)

# 2 - We want the insurance costs to be represented in US dollars. Replace all instances of # in medical_data with $.
# Store the result in a variable called updated_medical_data. Print updated_medical_data.

updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)

# 3 -We want to calculate the number of medical records in our data. Create a variable called num_records and initialize
# it at 0.

num_records = 0

# 4 - Next, write a for loop to iterate through the updated_medical_data string. Inside of the loop, add 1 to num_records
# when the current character is equal to $.

for i in updated_medical_data:
    if i == '$':
        num_records += 1

# 5 - Outside of the loop, print num_records with the following message:  There are {num_records} medical records in the
# data.

print(f'There are {num_records} medical records in the data.')

# 6 - The medical data in its current form is difficult to analyze. An essential job for a data scientist is to clean
# up data so that it's easy to work with. Let's start off by splitting the updated_medical_data string into a list
# of each record. Remember that each medical record is separated by a ; in the string. Store the result in a variable
# called medical_data_split and print this variable.

medical_data_split = updated_medical_data.split(';')
print(medical_data_split)

# 7 - Our data is now stored in a list, but it is still hard to read. Let's split each medical record into its own list.
# First, define an empty list called medical_records.

medical_records = []

# 8 - Next, iterate through medical_data_split and for each record, split the string after each comma (,) and append
# the split string to medical_records. Print medical_records after the loop.

for nb in medical_data_split:
    parts = nb.split(',')
    medical_records.append(parts)
print(medical_records)

# 9 - Our data is now slightly more readable. However, it is not properly formatted - it contains unnecessary
# whitespace. To fix this, let's start by creating an empty list called medical_records_clean.
# 10 - Next, use a for loop to iterate through medical_records. Inside of the loop, create an empty list called
# record_clean. We'll use this list to store a formatted version of each medical record.
# 11 -After the record_clean variable, create a nested for loop that goes through each record: for item in record
# Inside of this loop, append item.strip() to record_clean to remove any whitespace from the string.
# 12 - Finally, we need to add each cleaned up record to medical_records_clean. Outside of the nested for loop,
# append record_clean to medical_records_clean.
# 13 - Print medical_records_clean outside of the for loops to see the output. You should see output that is formatted
# and much easier to read.

medical_records_clean = [] # 9
for na in medical_records: # 10
    record_clean = []
    for item in na: # 11
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean) # 12
print(medical_records_clean) # 13

# 14 - Our data is now clean and ready for analysis. For example, to print out the names of each of the ten individuals,
# we can use the following loop: for record in medical_records_clean: print(record[0])
# Add this loop to the code block below and run it.

for record in medical_records_clean:
    print(record[0])

# 15 - You want all of the names in the medical records to be uppercase characters. In the for loop, update records[0]
# before the print statement so that all of the characters are uppercase. Run the code to see the result.

for record in medical_records_clean:
    cima = record[0]
    print(cima.upper())

# 16 - Let's store each name, age, BMI, and insurance cost in separate lists. To start, create four empty lists:
# names
# ages
# bmis
# insurance_costs

names = []
ages = []
bmis = []
insurance_costs = []

# 17 - Next, iterate through medical_records_clean and for each record:
# Append the name to names.
# Append the age to ages.
# Append the BMI to bmis.
# Append the insurance cost to insurance_costs.

for name in medical_records_clean:
    name = name[0]
    names.append(name)
for age in medical_records_clean:
    age = age[1]
    ages.append(age)
for BMI in medical_records_clean:
    BMI = BMI[2]
    bmis.append(BMI)
for insurance in medical_records_clean:
    insurance = insurance[3]
    insurance_costs.append(insurance)

# 18 - Print names, ages, bmis, and insurance_costs outside of the loop. Make sure the output is what you expect.
print(names)
print(ages)
print(bmis)
print(insurance_costs)

# 19 -Now that all of our data is in separate lists, we can easily perform analysis on that data. Let's calculate the
# average BMI in our dataset. First, create a variable called total_bmi and set it equal to 0.

total_ibm = 0

# 20- Next, use a for loop to iterate through bmis and add each bmi to total_bmi. Remember to convert bmi to a float.

for peso in bmis:
    total_ibm += float(peso)
# 21 - After the for loop, create a variable called average_bmi that stores the total_bmi divided by the length of the
# bmis list. Print out average_bmi with the following message:
# Average BMI: {average_bmi}

average_bmi = total_ibm/len(bmis)
print(f'Average BMI: {average_bmi:.2f}')

# 22 - a) Calculate the average insurance cost in insurance_costs. You will have the remove the $ in order to calculate this.
total_insurance = 0
for y in insurance_costs:
    custo = y.replace('$', '')
    total_insurance += float(custo)

average_insurance = total_insurance/len(insurance_costs)
print(f'Average insurance cost is ${average_insurance:.2f}')


# Write a for loop that outputs a string for each individual in the following format:

for all in medical_records_clean:
    print(f'{all[0]} is {all[1]} years old with a BMI of {all[2]}'
          f' and an insurance cost of {all[3]}.')

