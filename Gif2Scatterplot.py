from PIL import Image
import csv
import glob
from os.path import join
import os

output = [['x', 'y', 'colour', 'datapoint', 'picturename']]
datapoint = 1
colours = []
picture = 'hat'#.gif
filepath = 'C:\\GIF2Scatterplot\\'

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%s.png' % (outFolder, os.path.basename(inGif), nframes ) , 'PNG')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True
    
extractFrames(filepath + picture + '.gif', picture)

directory = filepath + picture

filelist = glob.glob(join(directory,'*.png'))

for item in filelist:
	im = Image.open(item) #Can be many different formats.
	rgb_im = im.convert('RGB')
	pix = im.load()
	print '%i pixels wide and %i pixels height' % (im.size[0],im.size[1])
	for x in range(0,im.size[0]):
		for y in range(0,im.size[1]):
				pixelcolor = rgb_im.getpixel((1, 1))
			output.append([x + 1, y + 1, pixelcolor, datapoint, item])
			colours.append(pixelcolor)
			datapoint += 1
	print item
with open(filepath + picture + ".csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(output)

colourset = set(colours)
colours = sorted(colourset)
colourpalette = '<color-palette name="' + picture + '" type="regular" >\n'
for colour in colours:
	if type(colour) == int:
		#print colour
		break
	elif len(colour) == 4:
		colour = colour[:-1]
	colour = '#%02x%02x%02x' % colour
	colourpalette += '<color>%s</color>\n' % colour
colourpalette += '</color-palette>'
with open("'filepath + picture + '.txt", "wb") as f:
	f.write(colourpalette)
print colourpalette
