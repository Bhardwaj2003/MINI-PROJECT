import matplotlib.pyplot as plt

x = ['Category A', 'Category B', 'Category C', 'Category D']
y = [80, 79, 95, 83, 75]

plt.bar(x, y)


plt.title('Categories')
plt.xlabel('Subjects')
plt.ylabel('Marks')

plt.show()
