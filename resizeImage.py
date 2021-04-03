from PIL import Image
import os

size_96 = (96,96)


for f in os.listdir('.'):
    while os.stat(f).st_size > 100000:
        im = Image.open(f)
        fn, fext = os.path.splitext(f)
        im.thumbnail(size_96)

        im.save('96/{}_96{}'.format(fn,fext))

        if os.stat(f).st_size <= 100000:
            break

