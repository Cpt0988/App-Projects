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
#zip file name
label3 = gui.Text("Name of zip file")
input3= gui.Input(key='nam')
#nam=f"{input3}.zip"


compress_button =gui.Button("Compress")
output_label = gui.Text(key="output")

window = gui.Window("File Compressor",layout=[[label, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [label3,input3],
                                              [compress_button,output_label]])

while True:
    event,values = window.read()
    #print(event,values)
    filepaths= values['files'].split(';')
    folder = values["folder"]
    nam1 = values['nam']+".zip"
    make_archive(filepaths, folder,nam1)
    window["output"].update(value="Completed")
    gui.WIN_CLOSED
    
    
window.read()
window.close()