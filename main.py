from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from colorthief import ColorThief

# Initializing tk for filegrabbing
root = Tk()
root.withdraw()
root.update()


# function to grab hexidecimal codes
def hexmaker(lis):
    hexlist = []
    for color in lis:
        hexcode = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        hexlist.append(hexcode)
    return hexlist

answer = input("Would you like to select an image for color extrapolation?\nType 'y' or 'n'. ").lower().strip()
if answer == 'y':
    print('Select now.')
    # grabbing filepath of user-selected image
    filepath = askopenfilename()
    # extracting its 10 most frequent RGB values & their hexcodes
    colorthief = ColorThief(filepath)
    colors = colorthief.get_palette(color_count=11)
    hexcodes = hexmaker(colors)
    # writing that data to a text file for record keeping
    with open('colors.txt', 'w') as file:
        file.write(str(colors))
        file.write("\n")
        file.write(str(hexcodes))
    print("The top 10 most common RGB values of your image and their hexidecimal codes "
          "have been written to a file in your local directory.\n"
          "Please look for a file named \"colors.txt\".")
    # asking if the user would like to see a visualization of their colors
    answer = input('Would you like to see an image of the extracted colors? Type \'y\' or \'n\'. ').lower().strip()
    if answer == 'y':
        plt.figure(figsize=(10,2))
        # looping through the extracted list of colors and displaying them
        plt.imshow([[colors[i] for i in range(10)]])
        # adding hexidecimal codes as tickmarks
        plt.xticks(range(10), hexcodes, rotation=30)
        plt.show()



