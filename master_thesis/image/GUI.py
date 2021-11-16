# import glob
# import PySimpleGUI as sg
# from PIL import Image, ImageTk

# def parse_folder(path):
#     images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')
#     return images
# def load_image(path, window):
#     try:
#         image = Image.open(path)
#         image.thumbnail((400, 400))
#         photo_img = ImageTk.PhotoImage(image)
#         window["image"].update(data=photo_img)
#     except:
#         print(f"Unable to open {path}!")
        
# def main():
#     elements = [
#         [sg.Image(key="image")],
#         [
#             sg.Text("Image File"),
#             sg.Input(size=(25, 1), enable_events=True, key="file"),
#             sg.FolderBrowse(),
#         ],
#         [
#             sg.Button("Prev"),
#             sg.Button("Next")
#         ]
#     ]
#     window = sg.Window("Image Viewer", elements, size=(475, 475))
#     images = []
#     location = 0
#     while True:
#         event, values = window.read()
#         if event == "Exit" or event == sg.WIN_CLOSED:
#             break
#         if event == "file":
#             images = parse_folder(values["file"])
#             if images:
#                 load_image(images[0], window)
#         if event == "Next" and images:
#             if location == len(images) - 1:
#                 location = 0
#             else:
#                 location += 1
#             load_image(images[location], window)
#         if event == "Prev" and images:
#             if location == 0:
#                 location = len(images) - 1
#             else:
#                 location -= 1
#             load_image(images[location], window)
#     window.close()
# if __name__ == "__main__":
#     main()

import io
import os
from typing import Sized
import PySimpleGUI as sg
from PIL import Image

file_types = [("PNG (*.png)", "*.png"),
              ("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
def main():
    col1_layout = [
        [sg.Text("First Image")],
        [
            sg.Input(size=(30, 1), key="-FILE_1-"),
            sg.FileBrowse(file_types=file_types, key="-BROWSE_1-"),
            sg.Button("Load Image", key="-Button_1-")
        ],
        [sg.Frame("", [[sg.Image(key="-IMAGE_1-")]])]
    ]
    col1 = sg.Column(col1_layout, element_justification="center")

    col2_layout = [
        [sg.Text("Second Image")],
        [
            sg.Input(size=(30, 1), key="-FILE_2-"),
            sg.FileBrowse(file_types=file_types, key="-BROWSE_2-"),
            sg.Button("Load Image",  key="-Button_2-")
        ],
        [sg.Frame("", [[sg.Image(key="-IMAGE_2-")]])]
    ]
    col2 = sg.Column(col2_layout, element_justification="center")

    main_layout = [[col1, col2]]


    window = sg.Window("Image Viewer", main_layout, size=(1000, 1000))
    while True:
        event, values = window.read()
        print(event, values)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-Button_1-":
                filename = values["-FILE_1-"]
                if os.path.exists(filename):
                    image = Image.open(filename)
                    image.thumbnail((200, 200))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    window["-IMAGE_1-"].update(data=bio.getvalue())
        if event == "-Button_2-":
                filename = values["-FILE_2-"]
                if os.path.exists(filename):
                    image = Image.open(filename)
                    image.thumbnail((200, 200))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    window["-IMAGE_2-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()

