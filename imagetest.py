import ui
import io
import Image

def pil2ui(imgIn):
    with io.BytesIO() as bIO:
        imgIn.save(bIO, 'PNG')
        imgOut = ui.Image.from_data(bIO.getvalue())
        del bIO
    return imgOut

w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

imageview = ui.ImageView(name='imgv1', bg_color='white', frame=(0, 0, w/2, h/2))

my_image_path = './resources/'+ str(1) + ".gif"
my_image = Image.open(my_image_path)

imageview.image = pil2ui(my_image)

view.add_subview(imageview)

view.present()
