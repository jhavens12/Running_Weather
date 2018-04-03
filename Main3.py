import get_data
import ui
import build


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

vis = build.vis(w,h,len(forecast_dict))
#create view dictionary
view_dict = {}

for n,day in enumerate(forecast_dict):
    q = n+1
    view_dict[q] = build.subviews(n,vis,ui) #build dictionary
    view.add_subview(view_dict[q]) #add subview to main view

    header = build.headers(n,vis,ui,forecast_dict[day],view_dict[q]) #n, vis dict, ui object, day info, view_name
    view_dict[q].add_subview(header)


view.present(style='sheet', hide_title_bar=True)