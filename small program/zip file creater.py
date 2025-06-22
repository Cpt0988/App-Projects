#
import FreeSimpleGUI as gui
from zip_function import make_archive

# files to compress
label = gui.Text("Select files to compress:")
input1= gui.Input()
choose_button1 = gui.FileBrowse("Choose", key='files')

#folder to save file
label2 = gui.Text("Select folder save to:")
input2= gui.Input()
choose_button2 = gui.FolderBrowse("Choose", key='folder')

compress_button =gui.Button("Compress")
output_label = gui.Text(key="output")

window = gui.Window("File Compressor",layout=[[label, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button,output_label]])

while True:
    event,values = window.read()
    print(event,values)
    filepaths= values['files'].split(';')
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Completed")
    
    
window.read()
window.close()