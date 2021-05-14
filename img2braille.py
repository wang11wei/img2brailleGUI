import argparse
import sys
import cv2
import numpy as np


class CannotReadImage(Exception):
    pass


def open_image_in_grayscale(filename):
    # 加载一张彩色图片，忽视它的透明度
    # img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), 1)    # 通过decode的方式，避免中文路径下报错
    img_gray = img.max(axis=2)      # 计算每个点位RGB中最大的一个返回，相当于3维压缩到1维=>得到灰度图像
    if img is None:
        raise CannotReadImage(filename)
    return img_gray


def size_max(w, h):
    return 1


def size_from_width_ratio(new_width):
    def get_size(w, h):
        return (new_width * 2) / w

    return get_size


def size_from_height_ratio(new_height):
    def get_size(w, h):
        return (new_height * 3) / h

    return get_size


def resize(img, ratio):
    h, w = img.shape[0], img.shape[1]
    new_size = (
        int(w * ratio),
        int(h * ratio),
    )
    return cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)


def smooth(img):
    return cv2.bilateralFilter(img, 9, sigmaSpace=10, sigmaColor=10)


def threshold(img, bsize):
    """
    :param img:
    :return: 自适应阈值分割，将灰度图像二值化，直接用来确定盲文类型，不需要设置阈值
    """
    return cv2.adaptiveThreshold(img, 1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, bsize, 2)


def convert_to_braille(img, invert=False):
    """
    :param img:
    :param invert: 是否反色（填充浅色）。默认为 false，填充黑色
    :return:
    """
    # Image already resized appropriately
    height, width = img.shape
    # 切分成3×2的patch
    for y in range((height // 4) - 1):
        for x in range((width // 2) - 1):
            box = img[y * 4:(y + 1) * 4, x * 2:(x + 1) * 2]
            # 盲文点字的编码规则
            num = box[0, 0] + 2 * box[1, 0] + 4 * box[2, 0] + 8 * box[0, 1] + 16 * box[1, 1] + 32 * box[2, 1] + 64 * \
                  box[3, 0] + 128 * box[3, 1]
            if invert:
                num = 255 - num

            yield int_to_braille(num)
        yield "\n"



def int_to_braille(i: int) -> str:
    # https://en.wikipedia.org/wiki/Braille_Patterns
    return chr(0x2800 + i)


def img2braille(filename, bsize=11, resize_size=size_max, smoothing=True, invert=False):
    img = open_image_in_grayscale(filename)

    # Resizing
    h, w = img.shape
    img = resize(img, resize_size(w, h))

    # Perform smoothing
    if smoothing:
        img = smooth(img)

    img = threshold(img, bsize)
    return convert_to_braille(img, invert=invert)


def main():
    parser = argparse.ArgumentParser(description='Converts image to braille.')
    parser.add_argument('--file', type=str, default="imgs/1.png")
    parser.add_argument('--disable-smoothing', dest='disable_smoothing', action='store_true', default=False,
                        help='Use bilateral filter for image smoothing')
    parser.add_argument('--no-resize', dest='no_resize', action='store_true', default=False,
                        help='Prevent resizing')
    parser.add_argument('--width', dest='width', type=int, default=None,
                        help='Width of result')
    parser.add_argument('--height', dest='height', type=int, default=None,
                        help='Height of result')
    parser.add_argument('--invert', dest='invert', default=False,
                        help='Invert image')
    args = parser.parse_args()

    if args.no_resize:
        resize_size = size_max
    elif args.width and not args.height:
        resize_size = size_from_width_ratio(args.width)
    elif args.height and not args.width:
        resize_size = size_from_height_ratio(args.height)
    else:
        resize_size = size_from_width_ratio(30)     # ！！！设置宽度，

    result = img2braille(
        filename=args.file,
        resize_size=resize_size,
        smoothing=not args.disable_smoothing,
        invert=args.invert
    )
    try:
        for c in result:
            sys.stdout.write(c)
    except BrokenPipeError:
        pass


if __name__ == '__main__':
    main()
