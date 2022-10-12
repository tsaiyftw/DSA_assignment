from myarray import MultiArray

# read sale data files
data0 = open("data/d0.txt", "r")
data1 = open("data/d1.txt", "r")
data2 = open("data/d2.txt", "r")
data3 = open("data/d3.txt", "r")
data4 = open("data/d4.txt", "r")
data5 = open("data/d5.txt", "r")
data6 = open("data/d6.txt", "r")
data7 = open("data/d7.txt", "r")
data8 = open("data/d8.txt", "r")
data9 = open("data/d9.txt", "r")
data_lst = []
data_lst.extend((data0, data1, data2, data3, data4, data5, data6, data7, data8, data9))

# store sale data into the 3D array
salesData = MultiArray(100, 100, 100)
for i in range(len(data_lst)):
    j = 0
    for product in data_lst[i]:
        product_name = product.split()
        for k in range(1, 13):
            salesData[i, j, k] = int(product_name[k])
            # print("y,i,j: ", y, i, j, "#: ", salesData[y, i, j])
        j += 1

# calculate sale number of all products in 10 years
total_sale = 0
for i in range(10):
    for j in range(1, 27):
        for k in range(1, 13):
            total_sale += salesData[i, j, k]
            # print("i,j,k", i, j, k, "#", salesData[i, j, k], total_sale)
print("10年內賣出所有的物品的總數: ", total_sale)

# calculate sale number of each month in 10 years
total_M = [0] * 13
for y in range(10):
    for p in range(1, 27):
        for m in range(1, 13):
            total_M[m] += salesData[y, p, m]
for i in range(1, 13):
    print(f"10年內{i}月份賣出的總數:{total_M[i]}")

# calcuate sale number of the same product in 10 years
total_P = [0] * 27
for y in range(10):
    for p in range(1, 27):
        for m in range(1, 13):
            total_P[p] += salesData[y, p, m]
for i in range(1, 27):
    print(f"10年內{chr(64+i)}產品賣出的總數:{total_P[i]}")
