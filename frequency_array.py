from itertools import chain, product
dataset_file = open('dataset_2_7.txt', 'r')
dataset_read = dataset_file.read()
k = int(input('k-len? '))
a = 0
letters_list = ['A', 'C', 'G', 'T']
frequency_array_dict = {}
frequency_array_list = []

# from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

for i in list(bruteforce(letters_list, k)):
    if len(i) == k:
        frequency_array_dict[i] = frequency_array_dict.get(i, 0)
# print(frequency_array_dict)

for letter in dataset_read:
    kmer = dataset_read[a:a+k]
    a += 1
    if len(kmer) == k:
        frequency_array_list.append(kmer)
# print(frequency_array_list)

for kmer in frequency_array_list:
    frequency_array_dict[kmer] = frequency_array_dict.get(kmer, 0) + 1

integers_list = ''
for integer in list(frequency_array_dict.values()):
    integers_list = integers_list + str(integer) + ' '
print(integers_list)
