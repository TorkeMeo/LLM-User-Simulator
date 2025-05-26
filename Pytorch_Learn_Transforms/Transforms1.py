from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img=Image.open("pic1.jpg")
print(img)

trans_totensor=transforms.ToTensor()
img_tensor=trans_totensor(img)
writer.add_image("ToTensor",img_tensor)

print(img_tensor[0][0][0])
trans_norm=transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm=trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image("Normalize",img_norm)

print(img.size)
trans_resize=transforms.Resize((512,512))
img_resize = trans_resize(img)
print(img_resize)
img_resize_tensor=trans_totensor(img_resize)
writer.add_image("Resize",img_resize_tensor)

trans_resize2=transforms.Resize(256)
trans_compose=transforms.Compose([trans_resize2,trans_totensor])
img_resize_tensor2=trans_compose(img)
writer.add_image("Compose",img_resize_tensor2)

trans_random = transforms.RandomCrop(100)
trans_compose2=transforms.Compose([trans_random,trans_totensor])
img_random_tensor = trans_compose2(img)
writer.add_image("Random",img_random_tensor)

writer.close()
