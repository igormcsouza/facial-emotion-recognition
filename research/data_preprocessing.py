"""Data preprocessing

Keras has some very useful tools to work with images and generation  on their 
trainning steps. In order to make good use of this features we need to organize 
the data on this fashion:

```
class1/
    0001.jpg
    0002.jpg
    ...
class2/
    0001.jpg
...
```

This way, Keras may preprocess, augment, and generate images to be used  model's
train.
"""
import os 
import shutil

from tqdm import tqdm # feedback on progressions
from pandas import read_csv 


# if for any reason the repository wasn't clone, it will do for you
if not os.path.exists('facial_expressions'):
    os.system('git clone git@github.com:igormcsouza/facial_expressions.git')

data = read_csv('facial_expressions/data/legend.csv')

# get the unique classes, take the duplicated ones and lower them all
classes = set([class_name.lower() for class_name in data['emotion'].unique()])

if not os.path.exists('data'):
    os.mkdir('data')

# create one folder for each class
for class_name in classes:
    class_path = os.path.join('data', class_name)
    if not os.path.exists(class_path):
        os.mkdir(class_path)

# move the images from repository to the data folder
for image, emotion in tqdm(zip(data['image'], data['emotion'])):
    images_original_path = os.path.join('facial_expressions/images', image)
    images_new_path = os.path.join(os.path.join('data', emotion.lower()), image)

    if os.path.exists(images_original_path):
        shutil.move(images_original_path, images_new_path)

# at the end, erase the repository
os.system('rm -r facial_expressions')




