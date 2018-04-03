import get_data
import ui


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))

side_margin = 5
w = w-side_margin
top_margin = 20

forecast_dict = get_data.forecast_me()

for n,day in enumerate(forecast_dict):
    view_x = side_margin+((w/3)*n)
    view_width = (w/3)-side_margin
    n = n+1
    label_name = "label"+str(n)
    view_name = "view_"+str(n)
    view_name = ui.ScrollView(frame=(view_x, top_margin, view_width, h-top_margin), background_color='lightyellow')
    view_name.border_color = 'black'
    view_name.border_width = 1

    label_width = view_width-(side_margin*4)
    label_x = side_margin*2
    label_y = top_margin
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (label_x, label_y, label_width, lblh))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 1 #1 is center
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 2
    label_name.text = forecast_dict[day]['time']['pretty']

    view_name.add_subview(label_name)
    view.add_subview(view_name)


# view.add_subview(view_2)
# view.add_subview(view_3)

view.present(style='sheet', hide_title_bar=True)
