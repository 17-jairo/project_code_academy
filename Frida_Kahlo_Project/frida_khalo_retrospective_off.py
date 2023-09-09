# Task 1
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Task 2
dates = [1939, 1933, 1946, 1940]

# Task 3
paintings = list(zip(paintings, dates))
print(paintings)

# Task 4
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

# Task 5
lengh = len(paintings)
print(lengh)

# Task 6
audio_tour_number = list(range(1, lengh + 1))
print(audio_tour_number)

#Task 7
master_list = list(zip(paintings, audio_tour_number))

# Task 8
print(master_list)