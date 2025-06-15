import FreeSimpleGUI as gui

label = gui.Text("Inches:")
input1 = gui.Input

label2 = gui.Text("Feet:")
input2 = gui.Input

convert_button = gui.Button("Convert")

window = gui.Window("Unit Converter", [[label, input1],[label2,input2]],[convert_button])

window.read()
window.close()