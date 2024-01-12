data = 'The lazy red fox slept instead of jumping over a dog.'

# Write the data
with open('fox.doc', mode = 'w', encoding = 'utf-8') as f:
    f.write(data)


# Read the file
with open('fox.doc', mode = 'r', encoding = 'utf-8') as f:
    read_data = f.read()


# Display the results
print('Original  : ' + data)
print('From disk : ' + read_data)
