
from pathlib import Path
from modules import scripts, script_callbacks, shared, sd_hijack




import modules.scripts as scripts
import gradio as gr
import os
import  shutil



from modules import script_callbacks
def when_clicked(ch):
    if ch:
        # we move the current config.json to this folder /extensions/reset_default_settings/scripts
        #incase the user decides he wants it back

        # Get the current working directory
        current_directory = os.getcwd()
        file_path = current_directory + "/config.json"  #to be moved
        destination_relative_path = '/extensions/reset_default_settings/scripts'

        destination_directory = current_directory + destination_relative_path
        # Move the file to the destination directory
        shutil.move(file_path, destination_directory)



        return "Settings are resetted,\n RESTART REQUIRED"

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            btn= gr.Button(
                value="Reset settings"


            )
            txt= gr.Textbox(label="",interactive=True,lines=5)
            btn.click(fn=when_clicked,inputs=[btn],outputs=[txt])



        return [(ui_component, "Default Settings", "Defualt Settings")]

script_callbacks.on_ui_tabs(on_ui_tabs)