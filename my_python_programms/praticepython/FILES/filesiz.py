import os
totalSize = 0
for filename in os.listdir('/home/userland/my_python_programms/praticepython'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/userland/my_python_programms/praticepython', filename))
print(totalSize, 'kb')
