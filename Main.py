import get_data
import ui


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))

bh = 32
bw = w/2
sp = 5
smg = 5
tmg = 20
lblh = 64
lblw = (w/3)-20

forecast_dict = get_data.forecast_me()

#view_1 = ui.ScrollView(frame=(0, tmg, w/3, h-tmg), background_color='orange')
#view_2 = ui.ScrollView(frame=(0+w/3, tmg, w/3, h-tmg), background_color='purple')
#view_3 = ui.ScrollView(frame=(0+((w/3)*2), tmg, w/3, h-tmg), background_color='green')


for n,day in enumerate(forecast_dict):
    frame_x = 0+((w/3)*n)
    n = n+1
    label_name = "label"+str(n)
    view_name = "view_"+str(n)
    view_name = ui.ScrollView(frame=(frame_x, tmg, w/3, h-tmg), background_color='orange')
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (0, tmg, lblw, lblh))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 2
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 2
    label_name.text = forecast_dict[day]['time']['pretty']

    view_name.add_subview(label_name)
    view.add_subview(view_name)


# view.add_subview(view_2)
# view.add_subview(view_3)

view.present(style='sheet', hide_title_bar=True)
