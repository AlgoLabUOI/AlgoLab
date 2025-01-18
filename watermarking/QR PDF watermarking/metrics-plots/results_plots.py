import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Data from the table
arnold_transformations = [0, 1, 2, 4, 8, 16, 32]

# Embedding Phase
embedding_time_p1 = [19.55, 20.97, 20.98, 21.04, 21.12, 21.15, 22.19]
embedding_time_p4 = [73.82, 79.77, 80.80, 81.30, 81.35, 82.37, 83.39]
embedding_time_p16 = [313.71, 316.50, 320.97, 321.82, 323.64, 324.30, 325.45]

embedding_cpu_p1 = [29, 29, 29, 29, 29, 29, 29]
embedding_cpu_p4 = [30, 31, 31, 34, 34, 35, 35]
embedding_cpu_p16 = [40, 40, 40, 40, 41, 41, 41]

embedding_ram_p1 = [31.37, 45.31, 45.47, 45.55, 46.18, 46.23, 46.36]
embedding_ram_p4 = [56.95, 70.43, 70.99, 71.35, 71.61, 73.00, 74.40]
embedding_ram_p16 = [150.19, 164.89, 168.80, 168.89, 169.39, 169.90, 171.54]

# Extraction Phase
extraction_time_p1 = [0.58, 0.60, 0.61, 0.62, 0.65, 0.66, 0.66]
extraction_time_p4 = [0.95, 0.98, 0.99, 1.01, 1.05, 1.17, 1.20]
extraction_time_p16 = [2.52, 2.60, 2.70, 2.78, 2.91, 3.30, 3.58]

extraction_cpu_p1 = [21, 21, 25, 25, 25, 25, 25]
extraction_cpu_p4 = [24, 25, 26, 29, 29, 30, 30]
extraction_cpu_p16 = [35, 36, 38, 43, 44, 45, 49]

extraction_ram_p1 = [41.19, 42.02, 42.18, 42.21, 42.39, 42.41, 42.89]
extraction_ram_p4 = [77.16, 77.92, 78.21, 78.65, 79.05, 79.10, 79.63]
extraction_ram_p16 = [140.73, 141.20, 142.82, 150.76, 151.88, 153.03, 153.24]

# Plotting
plt.figure(figsize=(16, 16))

# Embedding Phase Time
plt.subplot(3, 2, 1)
plt.plot(arnold_transformations, embedding_time_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, embedding_time_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, embedding_time_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('Time (s)')
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='center right')
plt.grid(True)

# Extraction Phase Time
plt.subplot(3, 2, 2)
plt.plot(arnold_transformations, extraction_time_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, extraction_time_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, extraction_time_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('Time (s)')
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='center right')
plt.grid(True)

# Embedding Phase CPU
plt.subplot(3, 2, 3)
plt.plot(arnold_transformations, embedding_cpu_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, embedding_cpu_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, embedding_cpu_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('CPU Usage (%)')
plt.ylim(10, 50)  # Set y-axis range
plt.yticks(np.arange(10, 51, 10))  # Set y-axis ticks from 10 to 50 with step 10
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='lower right')
plt.grid(True)

# Extraction Phase CPU
plt.subplot(3, 2, 4)
plt.plot(arnold_transformations, extraction_cpu_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, extraction_cpu_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, extraction_cpu_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('CPU Usage (%)')
plt.ylim(10, 50)  # Set y-axis range
plt.yticks(np.arange(10, 51, 10))  # Set y-axis ticks from 10 to 50 with step 10
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='lower right')
plt.grid(True)

# Embedding Phase RAM
plt.subplot(3, 2, 5)
plt.plot(arnold_transformations, embedding_ram_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, embedding_ram_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, embedding_ram_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('RAM Usage (MB)')
plt.ylim(30, 180)  # Set y-axis range
plt.yticks(np.arange(30, 181, 20))  # Set y-axis ticks from 10 to 50 with step 10
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='center right')
plt.grid(True)

# Extraction Phase RAM
plt.subplot(3, 2, 6)
plt.plot(arnold_transformations, extraction_ram_p1, marker='o', color='green', label='p=1')
plt.plot(arnold_transformations, extraction_ram_p4, marker='D', color='blue', label='p=4')
plt.plot(arnold_transformations, extraction_ram_p16, marker='s', color='red', label='p=16')
plt.xlabel('Number of Arnold\'s Transformations')
plt.ylabel('RAM Usage (MB)')
plt.ylim(30, 180)  # Set y-axis range
plt.yticks(np.arange(30, 181, 20))  # Set y-axis ticks from 10 to 50 with step 10
plt.xticks(arnold_transformations)  # Set x-axis labels
plt.legend(ncol=3, loc='center right')
plt.grid(True)

plt.tight_layout()
plt.show()
