arrA = []
arrB = []

print("FIFO stack")
print(arrA)
arrA.append("A")
print(arrA)
arrA.append("B") 
print(arrA)
arrA.append("C")
print(arrA)
arrA.append("D")
print(arrA)
arrA.append("E")
print(arrA)
arrA.append("F")
print(arrA)

print("\nReverse FIFO")
arrB.append(arrA.pop(0))
print(arrB)
arrB.append(arrA.pop(0))
print(arrB)
arrB.append(arrA.pop(0))
print(arrB)
arrB.append(arrA.pop(0))
print(arrB)
arrB.append(arrA.pop(0))
print(arrB)
arrB.append(arrA.pop(0))
print(arrB)

print("\nReverse FILO")
arrA.append(arrB.pop())
print(arrA)
arrA.append(arrB.pop())
print(arrA)
arrA.append(arrB.pop())
print(arrA)
arrA.append(arrB.pop())
print(arrA)
arrA.append(arrB.pop())
print(arrA)
arrA.append(arrB.pop())
print(arrA)