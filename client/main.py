from nicegui_components.local_file_picker import local_file_picker
from nicegui import ui

async def pick_file() -> None:
    result = await local_file_picker('~', multiple=True)
    ui.notify(f'You chose {result}')



# ui.label("Image Watermark - Signaturo").style.width = "100%".style.textAlign = "center".style.size = "20px"


ui.label("Image Watermark - Signaturo").style("width: 100%; text-align: center; font-size: 30px;")
ui.label("Select a folder to watermark").style("width: 100%; text-align: center; font-size: 20px;")

ui.label("").style("width: 100%; text-align: center; font-size: 10px;")



chosen = ui.button("Pick a file", on_click=pick_file,icon="folder")

ui.run()