names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)
print(names)
print(insurance_costs)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records")

first_medical_record = medical_records [0]
print(f"Here is the first medical record: {first_medical_record}")

medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}")

cheapest_tree = medical_records[:3]
print(f"Here are the three cheapest insurance costs in out medical records: {cheapest_tree}")

priciest_three = medical_records[-3:]
print(f"Here are the three priciest insurance costs in our medical records: {priciest_three}")

occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records")

medical_records = list(zip(names, insurance_costs))
print(medical_records)

medical_records.sort()
print(f"Here are the medical records sorted by name: {medical_records}")

middle_five_records = medical_records[3:7]
print(middle_five_records)

