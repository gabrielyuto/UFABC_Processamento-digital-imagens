from skimage import io

url = input()

img = io.imread(url)
width,height = img.size 

print(width)
print(height)
