import os
from PIL import Image
import PIL
import random


# Path to the layers folder
cwd = os.getcwd()
layers = os.path.join(cwd, 'layers')

# Load the layers
images = []
names = []


backgrounds = []
bottom_lids = []
eye_colors = []
eye_balls = []
goos = []
top_lids = []


for background in os.listdir('layers/Background'):
    backgrounds.append(Image.open(os.path.join(layers,'Background', background)))
for bottom_lid in os.listdir('layers/Bottom lid'):
    bottom_lids.append(Image.open(os.path.join(layers, 'Bottom lid', bottom_lid)))
for eye_color in os.listdir('layers/Eye color'):
    eye_colors.append(Image.open(os.path.join(layers, 'Eye color', eye_color)))
for eye_ball in os.listdir('layers/Eyeball'):
    eye_balls.append(Image.open(os.path.join(layers, 'Eyeball', eye_ball)))
for goo in os.listdir('layers/Goo'):
    goos.append(Image.open(os.path.join(layers, 'Goo', goo)))
goos.append(Image.new('RGBA', (512, 512), (0, 0, 0, 0)))
for top_lid in os.listdir('layers/Top lid'):
    top_lids.append(Image.open(os.path.join(layers, 'Top lid', top_lid)))

def pick_random_picture(layer):
    return layer[random.randint(0, len(layer) - 1)]

def generate_image(id_):
    background = pick_random_picture(backgrounds)
    bottom_lid = pick_random_picture(bottom_lids)
    eye_color = pick_random_picture(eye_colors)
    eye_ball = pick_random_picture(eye_balls)
    goo = pick_random_picture(goos)
    top_lid = pick_random_picture(top_lids)

    # Create a new image
    pfp = Image.new('RGBA', background.size)

    # Paste the layers:
    pfp.paste(background, (0, 0))
    pfp.paste(bottom_lid, (0, 0), bottom_lid)
    pfp.paste(eye_color, (0, 0), eye_color)
    pfp.paste(eye_ball, (0, 0), eye_ball)
    pfp.paste(goo, (0, 0), goo)
    pfp.paste(top_lid, (0, 0), top_lid)

    # Save the image
    pfp.save(os.path.join(cwd, f'outputs/pfp_{id_}.png'))
    
    print(f'pfp_{id_}.png created!')

    return pfp

total_possible = len(backgrounds) * len(bottom_lids) * len(eye_colors) * len(eye_balls) * len(goos) * len(top_lids)

for index in range(total_possible):
    generate_image(index)

