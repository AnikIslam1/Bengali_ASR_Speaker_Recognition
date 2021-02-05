import matplotlib.pyplot as plt
import math

X, Y, Z = [], [],[]
fig = plt.figure()

palette = plt.get_cmap('Set1')


for line in open(r'C:\Users\anika\Desktop\CSE465\demo.tsv'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  #Y.append(values[1]*10)
  Z.append(values[2]*10)


plt.style.use('seaborn-darkgrid')
fig.suptitle('Bengali_ASR', fontsize=20)
plt.xlabel('Epoch(50)', fontsize=18)
plt.ylabel('Classification error %', fontsize=16)


#plt.plot(Y,'r-',label='Average training loss/Frame')
plt.plot(Z,'g-',label='Classification error at frame level')

plt.legend()
plt.show()