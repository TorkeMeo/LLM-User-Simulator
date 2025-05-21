from torch.utils.tensorboard import SummaryWriter
import numpy as np
from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)
        self.img_path = os.listdir(self.path)
    def __getitem__(self,index):
        img_name = self.img_path[index]
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img,label
    def __len__(self):
        return len(self.img_path)

writer = SummaryWriter("logs")
train_root_dir = "train"
ants_label_dir = "ants"
bees_label_dir = "bees"
dataset_ants=MyData(train_root_dir,ants_label_dir)
index = int(input("input index please:"))
image_PIL =dataset_ants[index][0]
image_array = np.array(image_PIL)
image_shape = image_array.shape
if image_shape[0]==3 or image_shape[0]==1 or image_shape[0]==2:
    image_format = "CHW"
elif image_shape[2]==3 or image_shape[2]==1 or image_shape[2]==2:
    image_format = "HWC"
else:
    image_format = "HW"
writer.add_image("test",image_array,1,dataformats=image_format)
for i in range(100):
    writer.add_scalar("y=x",i,i)
    writer.add_scalar("y=2*x",2*i,i)


writer.close()