import os
counter = 1
path = "./Data/dataset_train_model/"
dir_list = os.listdir(path)
for i in dir_list:
    if(i[0] != '.'):
        print(i)
        img_files = os.listdir(path+i)
        for j in img_files:
            if(j[0] != '.'):
                imgs = os.listdir(path+i+"/"+j)
                print(imgs)
                for k in imgs:
                    if(k[0] != '.'):
                        os.rename(path+i+"/"+j+"/"+k,"./TrainingDataSet/"+i+"-"+str(counter)+".png")
                        counter += 1

from PIL import Image
# grayscale
path = "./TrainingDataSet/"
dir_list = os.listdir(path)
for i in dir_list:
    if(i[0] != '.'):
        img_files = os.listdir(path+i)
        for j in img_files:
            if(j[0] != '.'):
                image = Image.open(path+i+"/"+j).convert('L')
                new_image = image.resize((100, 100))
                new_image.save(path+i+"/"+j)