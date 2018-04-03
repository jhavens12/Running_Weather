import get_data
import ui


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))

bh = 32
bw = w/2
sp = 5
smg = 5
tmg = 20
lblh = 32
lblw = 40

forecast_dict = get_data.forecast_me()

view_1 = ui.ScrollView(frame=(0, tmg, w/3, h-tmg), background_color='orange')
view_2 = ui.ScrollView(frame=(0+w/3, tmg, w/3, h-tmg), background_color='purple')
view_3 = ui.ScrollView(frame=(0+((w/3)*2), tmg, w/3, h-tmg), background_color='green')

view_dict = {}
view_dict[1] = view_1
view_dict[2] = view_2
view_dict[3] = view_3

for n,day,sub_view in enumerate(zip(forecast_dict,view_dict)):
    n = n+1
    label_name = "label"+str(n)
    #view_name = "view"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (0, tmg, lblw, lblh))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment=1
    label_name.title = forecast_dict[day]['time']['pretty']

    sub_view.add_subview(label_name)

view.add_subview(view_1)
view.add_subview(view_2)
view.add_subview(view_3)

view.present(style='sheet', hide_title_bar=True)
