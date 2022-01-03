import io
import os

import PySimpleGUI as sg
from PIL import Image, ImageTk


FILE_TYPES = [("PNG (*.png)", "*.png"),
              ("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]


def load_image(path, window_image, windows_frame):
    if os.path.exists(path):
        try:
            image = Image.open(path)
            title = path.split('/')[-1]
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window_image.update(data=bio.getvalue())
            windows_frame.TKFrame.config(text=title)
        except:
            print(f"Unable to open {path}!")


def main():
    sg.theme('DarkBrown')
    col1_layout = [
        [sg.Text("First Image", font=("Arial", 20))],
        [
            sg.Input(size=(30, 1), key="-FILE_1-"),
            sg.FileBrowse(file_types=FILE_TYPES, key="-BROWSE_1-"),
            sg.Button("Load Image", key="-Button_1-")
        ],
        [sg.Frame("", [[sg.Image(key="-IMAGE_1-")]], key="-FRAME_1-")]
    ]
    col1 = sg.Column(col1_layout, element_justification="center")

    col2_layout = [
        [sg.Text("Second Image", font=("Arial", 20))],
        [
            sg.Input(size=(30, 1), key="-FILE_2-"),
            sg.FileBrowse(file_types=FILE_TYPES, key="-BROWSE_2-"),
            sg.Button("Load Image",  key="-Button_2-")
        ],
        [sg.Frame("", [[sg.Image(key="-IMAGE_2-")]], key="-FRAME_2-")]
    ]
    col2 = sg.Column(col2_layout, element_justification="center")

    main_layout = [[col1, col2]]


    window = sg.Window("Image Viewer", main_layout, size=(1000, 800),
                       element_justification="center")
    while True: 
        event, values = window.read()
        print(event, values)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-Button_1-":
            path = values["-FILE_1-"]
            load_image(path, window["-IMAGE_1-"], window["-FRAME_1-"])
        if event == "-Button_2-":
            path = values["-FILE_2-"]
            load_image(path, window["-IMAGE_2-"], window["-FRAME_2-"])

    window.close()


if __name__ == "__main__":
    main()

