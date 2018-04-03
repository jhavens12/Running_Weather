import get_data
import ui
import build


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

vis = build.vis()
#create view dictionary
view_dict = {}
for n,day in enumerate(forecast_dict):
    view_dict[n+1] = build.subviews(n,vis) #build dictionary
    view.add_subview(view_dict[n+1]) #add subview to main view



view.present(style='sheet', hide_title_bar=True)
