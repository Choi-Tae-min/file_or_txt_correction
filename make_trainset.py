import random
import os

# Define the path to your data directory
data_dir = 'C:/Users/user/datapath'
#image data file name
file = "image_{:04d}.png" 


train_paths = []
count = 0
# Iterate directory
for path in os.listdir(data_dir):
    
        count += 1
print('File count:', count)
counta=[]
sum=0
i=1
k=0
for i in range(count): 
    for filename in os.listdir(os.path.join(data_dir,f"ep{i}/color")):
        
        sum += 1
        print(i," ",sum)
            
    counta.append(sum)
    sum=0           
for j in range(len(counta)):
     print(counta[j])   

for episode_num in range(count):
    for frame_num in range(counta[episode_num]):
        file_name = f"ep{episode_num}/color {frame_num}"
        file_path = os.path.join(file_name)
        if frame_num%2==0:
            train_paths.append(file_path)
        elif frame_num%2==1:
            train1_paths.append(file_path)
             
       

# Write to the training files.txt
with open('data_path/train_files.txt', 'w') as f:
    for path in train_paths:
        f.write(str(path) + ' l\n')
        

