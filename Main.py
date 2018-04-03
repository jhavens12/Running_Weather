import get_data
import ui


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))

side_margin = 5
w = w-side_margin
top_margin = 20
title_label_height = 64 #title labels
spacing_margin = 15

forecast_dict = get_data.forecast_me()

def create_button(n,label_x,label_y,label_width):
    label_width = view_width-(side_margin*4)
    label_x = side_margin*2
    label_y = top_margin

    label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (label_x, label_y, label_width, title_label_height))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 1 #1 is center
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 2

    return label_name

for n,day in enumerate(forecast_dict):
    entry_count = len(forecast_dict)
    view_x = side_margin+((w/entry_count)*n)
    view_width = (w/entry_count)-side_margin
    n = n+1

    view_name = "view_"+str(n)
    view_name = ui.ScrollView(frame=(view_x, top_margin, view_width, h-top_margin), background_color='lightyellow')
    view_name.border_color = 'black'
    view_name.border_width = 1

    #this creates the title labels
    label_width = view_width-(side_margin*4)
    label_x = side_margin*2
    label_y = top_margin
    label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (label_x, label_y, label_width, title_label_height))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 1 #1 is center
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 2
    label_name.text = forecast_dict[day]['time']['pretty']
    view_name.add_subview(label_name)

    frame_x = side_margin*2
    frame_y = top_margin + title_label_height + spacing_margin
    frame_width = view_width-(side_margin*4)
    frame_height = frame_width

    image_view_name = "ImageView"+str(n)
    image_view_name = ui.ImageView(name=image_view_name, bg_color='white', frame=(frame_x, frame_y, frame_width, frame_height))
    ImageView.load_from_url(forecast_dict[day]['weather']['icon_url'])
    view_name.add_subview(image_view_name)

    view.add_subview(view_name)

view.present(style='sheet', hide_title_bar=True)
