#Import the relevant modules
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# Create a window
window = tk.Tk()
#Creates a title at the top of the window
window.title('My Wardrobe')
#Sets the size of the window
window.geometry('366x527')
#Sets the background colour
window.configure(bg='#a795ad')

# Lists/path to find all of the folders and images for tops and bottoms
top_images = [
    "tops/shirt1.png",
    "tops/shirt2.png",
    "tops/shirt3.png",
    "tops/shirt4.png"
]

bottom_images = [
    "pants/pant1.png",
    "pants/pant2.png",
    "pants/pant3.png"
]

# Create frames to hold the top images
frame_top = tk.Frame(window, width=300, height=300, bg="#cac0ce")
#Sets the location of the frame the frame_top is above
frame_top.grid(row=0, column=1, padx=10, pady=10)

#Creates frame to hold the bottom images
frame_bottom = tk.Frame(window, width=300, height=300, bg="#cac0ce")
#Sets the location of the frame the frame_bottom is below
frame_bottom.grid(row=1, column=1, padx=10, pady=10)

#Global Variables to track the current index for both tops and bottoms
current_top_index = 0
current_bottom_index = 0

# Function to display the image in a frame
def display_image(frame, image_path):
    image = Image.open(image_path)
    #Rotate image based on EXIF data (if I took the photo portrait on my phone it will remember and remain in portrait)
    image = ImageOps.exif_transpose(image)
    #Resize the image so it stays in the frame
    image = image.resize((200, 200))
    #Makes it compatible with Tknter
    img_tk = ImageTk.PhotoImage(image)

    #All the widgets (images) in the frame become 'children' of the frame
    # Tom.Slick. (2013, April 3). Python tkinter clearing a frame [Online forum post]. Stack Overflow. https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    for widget in frame.winfo_children():
        #Clears the widgets (images) so the next image can be shown
        widget.destroy()

    #Creates a label "image_label" which will display the image in frame
    image_label = tk.Label(frame, image=img_tk)
    #Makes sure the image does not get lost or disappear because of 'garbage collection' (Keeps it in memory)
    image_label.image = img_tk
    #Adds the label to the window making it show up on screen
    image_label.pack()

# Initial display of the first images when you open the window
display_image(frame_top, top_images[current_top_index])
display_image(frame_bottom, bottom_images[current_bottom_index])

#Functions for navigation buttons (left to right buttons)
#MOO ICT. (n.d.). Make an image slide show app using Python and Tkinter. MOO ICT. https://www.mooict.com/make-a-image-slide-show-app-using-python-and-tkinter/
def next_top():
    #Tells Python we're using the global variable to remember the current index mentioned earlier
    global current_top_index
    #Move to the next image by adding 1
    current_top_index = current_top_index + 1
    # If we've reached the end of the list, start from the beginning
    if current_top_index >= len(top_images):
        current_top_index = 0
    # Display the new image
    display_image(frame_top, top_images[current_top_index])


def previous_top():
    #Tell Python we're using the global variable to remember the current index mentioned earlier
    global current_top_index
    #Move to the previous image by subtracting 1
    current_top_index = current_top_index - 1
    #If It goes before the first image, move to the last image
    if current_top_index < 0:
        current_top_index = len(top_images) - 1
    # Display the new image
    display_image(frame_top, top_images[current_top_index])


def next_bottom():
    #Tell Python we're using the global variable to remember the current index
    global current_bottom_index
    #Move to the next image by adding 1
    current_bottom_index = current_bottom_index + 1
    #If we've reached the end of the list, move to the first image
    if current_bottom_index >= len(bottom_images):
        current_bottom_index = 0
    # Display the new image
    display_image(frame_bottom, bottom_images[current_bottom_index])


def previous_bottom():
    # Tell Python we're using the global variable to remember the current index
    global current_bottom_index
    # Move to the previous image by subtracting 1
    current_bottom_index = current_bottom_index - 1
    # If we go before the first image, move to the last image
    if current_bottom_index < 0:
        current_bottom_index = len(bottom_images) - 1
    # Display the new image
    display_image(frame_bottom, bottom_images[current_bottom_index])

#Function to generate and display a random outfit
def random_outfit():
    global current_top_index, current_bottom_index
    #randint selects a random integer
    current_top_index = random.randint(0, len(top_images) - 1)
    current_bottom_index = random.randint(0, len(bottom_images) - 1)
    #Displays the image it randomly generates
    display_image(frame_top, top_images[current_top_index])
    display_image(frame_bottom, bottom_images[current_bottom_index])

# Buttons for navigating tops
button_top_left = tk.Button(window, text="<", command=previous_top)
button_top_left.grid(row=0, column=0, padx=10)

button_top_right = tk.Button(window, text=">", command=next_top)
button_top_right.grid(row=0, column=2, padx=10)

# Buttons for navigating bottoms
button_bottom_left = tk.Button(window, text="<", command=previous_bottom)
button_bottom_left.grid(row=1, column=0, padx=10)

button_bottom_right = tk.Button(window, text=">", command=next_bottom)
button_bottom_right.grid(row=1, column=2, padx=10)

# button to generate a random outfit
random_button = tk.Button(window, text="Generate Random Outfit", command=random_outfit)
random_button.grid(row=2, column=1, pady=20)

# Run the application
window.mainloop()






