"""
File: stanCodoshop.py
Name: Weili Chen
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2) ** 0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for i in range(len(pixels)):
        sum_red += pixels[i].red
        sum_green += pixels[i].green
        sum_blue += pixels[i].blue
    avg_red = sum_red // len(pixels)
    avg_green = sum_green // len(pixels)
    avg_blue = sum_blue // len(pixels)
    avg_list = [avg_red, avg_green, avg_blue]
    return avg_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_rgb = get_average(pixels)
    best_pixel = pixels[0]
    for i in range(len(pixels)):
        if get_pixel_dist(pixels[i], avg_rgb[0], avg_rgb[1], avg_rgb[2]) < get_pixel_dist(best_pixel, avg_rgb[0],
                                                                                          avg_rgb[1], avg_rgb[2]):
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            img_pixels = []
            pixel = result.get_pixel(x, y)
            for i in range(len(images)):
                img_pixels += [images[i].get_pixel(x, y)]
            pixel.red = get_best_pixel(img_pixels).red
            pixel.green = get_best_pixel(img_pixels).green
            pixel.blue = get_best_pixel(img_pixels).blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
