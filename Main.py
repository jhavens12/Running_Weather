import get_data
import ui
import build


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

def switch_pressed(self):
    print ("Pressed "+self.name)
    #get titles and labels based on PM
    #figure out which subview has been pressed
    #rebuild header, imagview, title labels and value labels


def first_run(forecast_dict,view):
    vis = build.vis(w,h,len(forecast_dict['AM']))
    #create view dictionary
    view_dict = {}

    for n,day in enumerate(forecast_dict['AM']):
        d = n+1
        q = 'AM_'+str(d)
        view_dict[q] = build.subviews(n,vis,ui) #build dictionary
        view.add_subview(view_dict[q]) #add subview to main view

        header = build.headers(n,vis,ui,forecast_dict['AM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
        view_dict[q].add_subview(header)

        #the load from url option seems to be freezing every once in a while
        #imageview = build.imageview(n,vis,ui,forecast_dict[day],view_dict[q])
        #view_dict[q].add_subview(imageview)

        title_label_list,value_label_list = build.AM_titles_and_values(forecast_dict['AM'][day])

        build.title_labels(n,vis,ui,view_dict[q],title_label_list)
        #value_labels
        build.value_labels(n,vis,ui,view_dict[q],value_label_list)

    for n,day in enumerate(forecast_dict['PM']):
        d = n+1
        q = 'PM_'+str(d)
        view_dict[q] = build.subviews(n,vis,ui) #build dictionary
        #view.add_subview(view_dict[q]) #add subview to main view

        header = build.headers(n,vis,ui,forecast_dict['PM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
        view_dict[q].add_subview(header)

        #the load from url option seems to be freezing every once in a while
        #imageview = build.imageview(n,vis,ui,forecast_dict[day],view_dict[q])
        #view_dict[q].add_subview(imageview)

        title_label_list,value_label_list = build.PM_titles_and_values(forecast_dict['PM'][day])

        build.title_labels(n,vis,ui,view_dict[q],title_label_list)
        #value_labels
        build.value_labels(n,vis,ui,view_dict[q],value_label_list)

    pprint(view_dict)

    # for c,data in enumerate(view_dict): #for each view, create button and add to main view
    #     button = build.switch_buttons(c,data,vis,ui) #pass cycle number, view name(data), vis library and ui element
    #     button.action = switch_pressed
    #     view.add_subview(button) #each view gets a button




first_run(forecast_dict,view)

view.present(style='sheet', hide_title_bar=True)
