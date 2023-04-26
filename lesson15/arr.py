from array import array

byte_arr = array('b', [1, 2, 3, 4, 5])
byte_arr.append(-256)
print(byte_arr)
