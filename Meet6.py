# perbandingan 
# lebih besar >
# lebih kecil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# tidak sama "is not"

x = 4
y = 5

# lebih besar >
hasil = x > y 
print(x, '>',y, 'adalah', hasil)

# lebih kecil <
hasil = x < y 
print(x, '<',y, 'adalah', hasil)

# lebih besar sama dengan >=
hasil = x >= y 
print(x, '>=',y, 'adalah', hasil)

# lebih kecil sama dengan <=
hasil = x <= y 
print(x, '<=',y, 'adalah', hasil)

# sama dengan ==
hasil = x == y 
print(x, '==',y, 'adalah', hasil)

# tidak sama dengan !=
hasil = x != y 
print(x, '!=',y, 'adalah', hasil)

# sama "is"
hasil = x is y 
print(x, 'is',y, 'adalah', hasil)

# tidak sama "is not"
hasil = x is not y 
print(x, 'is not',y, 'adalah', hasil)

# > < >= <= == != ini adalah perbandingan literal
# x = 4, 4= literal (tidak memakan memory)
# x = objeck (memory)
#
# x = 4 (bisa)
# x is 4 (tidak bisa)
# x is y (bisa, kerana yd dibandingankan adalah onjeck)

# is dan is not
hasil = x is y
print(x, 'is', y, 'adalah', hasil)

hasil = x is not y
print(x, 'is not', y, 'adalah', hasil)
