string1 = input()
string2 = input()
array1 = string1.split()
array2 = string2.split()
diff_arrays = sorted(set(array1) - set(array2), reverse=True)

print(' '.join(diff_arrays))