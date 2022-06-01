from PIL import Image


def open_image(file):
    im = Image.open(file)
    return im


def save(file, name=f'PSDIY File (', file_type='jpg'):
    try:
        file.save(f'{name}1)' + '.' + file_type)
    except SyntaxError:
        raise SyntaxError('Wrong file, type or name.')
    except FileExistsError:
        count = 1
        while FileExistsError:
            count += 1
            try:
                file.save(f'{name + str(count)})' + '.' + file_type)
            except FileExistsError:
                continue


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
            raise TypeError('Wrong type of either pixel_1, pixel_2 or mix percentage.')
    else:
        raise ValueError('Mix percentage value must be between 0 and 1.')


def resize_image(file, x_axis, y_axis):
    try:
        return file.resize(x_axis, y_axis)
    except TypeError:
        try:
            return file.resize(int(x_axis), int(y_axis))
        except SyntaxError:
            raise TypeError('Types of X and Y sizes must be integers, not float values or text.')


def crop_image(file, x_pos1, y_pos1, x_pos2, y_pos2):
    return file.crop((x_pos1, y_pos1, x_pos2, y_pos2))


class ApplyFilters:
    def __init__(self, file):
        self.file = file
        self.pixels = self.file.load()
        self.x, self.y = self.file.size

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
                r, g, b = self.pixels
                brightness = r + g + b if r + g + b > 0 else 1
                if brightness < ratio:
                    k = ratio / brightness
                    self.pixels[i, j] = min(255, int(r * k ** 2)), min(255, int(g * k ** 2)), min(255, int(b * k ** 2))
                else:
                    self.pixels[i, j] = r, g, b
