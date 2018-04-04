import get_data
import ui
import build


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

vis = build.vis(w,h,len(forecast_dict['AM']))
#create view dictionary
view_dict = {}

for n,day in enumerate(forecast_dict['AM']):
    q = n+1
    view_dict[q] = build.subviews(n,vis,ui) #build dictionary
    view.add_subview(view_dict[q]) #add subview to main view

    header = build.headers(n,vis,ui,forecast_dict['AM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
    view_dict[q].add_subview(header)

    #the load from url option seems to be freezing every once in a while
    #imageview = build.imageview(n,vis,ui,forecast_dict[day],view_dict[q])
    #view_dict[q].add_subview(imageview)

    title_label_list,value_label_list = build.titles_and_values(forecast_dict['AM'][day])

    build.title_labels(n,vis,ui,view_dict[q],title_label_list)
    #value_labels
    build.value_labels(n,vis,ui,view_dict[q],value_label_list)


view.present(style='sheet', hide_title_bar=True)
