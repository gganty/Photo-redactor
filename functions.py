from PIL import Image


def open_image(file):
    im = Picture(Image.open(file))
    return im


def mix(file_1, file_2, percentage_1st_photo):
    if 1 >= percentage_1st_photo >= 0:
        try:
            r, g, b = file_1
            r2, g2, b2 = file_2
            r = r * percentage_1st_photo + r2 * (1 - percentage_1st_photo)
            g = g * percentage_1st_photo + g2 * (1 - percentage_1st_photo)
            b = b * percentage_1st_photo + b2 * (1 - percentage_1st_photo)
            return round(r), round(g), round(b)
        except TypeError:
            print('Wrong type of either pixel_1, pixel_2 or mix percentage.')
    else:
        print('Mix percentage value must be between 0 and 1, both sides included.')


class Picture:
    def __init__(self, file):
        self.file = file
        self.pixels = self.file.load()
        self.x, self.y = self.file.size

    def resize_image(self, x_axis, y_axis):
        try:
            return self.file.resize(x_axis, y_axis)
        except TypeError:
            try:
                return self.file.resize(int(x_axis), int(y_axis))
            except SyntaxError:
                print('Types of X and Y sizes must be integers, not float values or text.')

    def crop_image(self, x_pos1, y_pos1, x_pos2, y_pos2):
        return self.file.crop((x_pos1, y_pos1, x_pos2, y_pos2))

    def bw(self):
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                a = (r + g + b) // 3
                self.pixels[i, j] = a, a, a

    def invert(self):
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b

    def curve(self, ratio):
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                brightness = r + g + b if r + g + b > 0 else 1
                if brightness < ratio:
                    k = ratio / brightness
                    self.pixels[i, j] = min(255, int(r * k ** 2)), min(255, int(g * k ** 2)), min(255, int(b * k ** 2))
                else:
                    self.pixels[i, j] = r, g, b

    def save(self, name=f'PSDIY File (', file_type='jpg'):
        try:
            self.file.save(f'{name}1)' + '.' + file_type)
        except SyntaxError:
            raise SyntaxError('Wrong file, type or name.')
        except FileExistsError:
            count = 1
            while FileExistsError:
                count += 1
                try:
                    self.file.save(f'{name + str(count)})' + '.' + file_type)
                except FileExistsError:
                    continue
