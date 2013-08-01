#!/usr/bin/env python

"""
Finds duplicate images in the specified directories

"""
from sys import argv, exit
from PIL import Image
from os import listdir 
from os.path import join

def print_duplicates(im_dict):

    print "\n\nDuplicate files:\n----------------\n\n"

    for x in im_dict.values():
        if len(x) > 1:
            print "These files are duplicate:"

            for w in range(len(x)):

                print "    - %s" % x[w]

            print "\n" 

def get_exif(dirs):

    exifpath_dict = {}

    for dir_content, x in [(listdir(x), x) for x in set(dirs)]:
        
        for image_path in dir_content:

            exif_string = ""

            if image_path.endswith(".jpg") or image_path.endswith(".jpeg") \
                or image_path.endswith(".JPG") or image_path.endswith(".JPEG"):
                
                try:
                    exif_info = Image.open(join(x, image_path))._getexif()

                except IOError, e:
                    print "**ERROR** Error opening %s: %s" % (image_path, e)

                else:
                    try:
                        for z in exif_info.keys():
                            exif_string += str(exif_info[z])
                    
                    except AttributeError:
                        print "**WARNING** %s doesn't have exif content, skipping it" % image_path
                    
                    else:
                        exifpath_dict.setdefault(exif_string, []).append(join (x, image_path))

    return exifpath_dict
       

# for dir_content in [listdir(x) for x in dirs] for image_path in dir_content if image_path.endswith(".jpg") or image_path.endswith(".jpeg")

if __name__ == "__main__":

    if len(argv) == 1:
        exit ("Too few arguments. Usage: dup_images <dir1> <dir2> ...")

    print_duplicates(get_exif(argv[1:]))

