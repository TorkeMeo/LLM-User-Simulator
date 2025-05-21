
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

def imgshow(img,label):
    img.show()
    print(label)
def output(data1,data2):
    choice = input("Enter 1 to view ants' picture. Enter 2 to view bees' picture:")
    if int(choice) == 1:
        idx = int(input("Please enter the index of the picture:"))
        if idx>= 0 and idx <= len(data1):
            img,label = data1[idx]
            imgshow(img,label)
        else:
            print("Out of range!")
    elif int(choice) == 2:
        idx = int(input("Please enter the index of the picture:"))
        if idx >= 0 and idx <= len(data2):
            img, label = data2[idx]
            imgshow(img, label)
        else:
            print("Out of range!")
    else:
        print("Please enter 1 or 2.")

train_root_dir = "train"
ants_label_dir = "ants"
bees_label_dir = "bees"
ants_dataset = MyData(train_root_dir,ants_label_dir)
bees_dataset = MyData(train_root_dir,bees_label_dir)
output(ants_dataset,bees_dataset)