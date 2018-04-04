import get_data
import ui
import build
from pprint import pprint


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

def switch_pressed(self):
    print ("Pressed "+self.name)
    if "AM" in self.name:
        print("Button pressed and AM displayed")
        view_name = self.name.replace("button_","")
        view_number = view_name.replace("AM","")
        new_view_name = "PM"+view_number
        view.remove_subview(view_dict[view_name]) #view_dict contains names as keys and view objects as values
        view.remove_subview(self) #remove button
        view.add_subview(view_dict[new_view_name])

        #add back button with PM name
        button = build.switch_buttons(int(view_number-1),new_view_name,vis,ui) #pass cycle number, view name(data), vis library and ui element
        button.action = switch_pressed
        view.add_subview(button)

    if "PM" in self.name:
        print("Button pressed and PM displayed")
        view_name = self.name.replace("button_","")
        view_number = view_name.replace("PM","")
        new_view_name = "AM"+view_number
        view.remove_subview(view_dict[view_name]) #view_dict contains names as keys and view objects as values
        view.remove_subview(self) #remove button
        view.add_subview(view_dict[new_view_name])

        #add back button with PM name
        button = build.switch_buttons(int(view_number-1),new_view_name,vis,ui) #pass cycle number, view name(data), vis library and ui element
        button.action = switch_pressed
        view.add_subview(button)



def first_run(forecast_dict,view):
    global vis
    vis = build.vis(w,h,len(forecast_dict['AM']))
    #create view dictionary
    global view_dict
    view_dict = {}

    for n,day in enumerate(forecast_dict['AM']):
        d = n+1
        q = 'AM'+str(d)
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
        q = 'PM'+str(d)
        view_dict[q] = build.subviews(n,vis,ui) #build dictionary
        view_dict[q].background_color = "darkblue" #change for PM
        #view.add_subview(view_dict[q]) #add subview to main view

        header = build.headers(n,vis,ui,forecast_dict['PM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
        view_dict[q].add_subview(header)

        title_label_list,value_label_list = build.PM_titles_and_values(forecast_dict['PM'][day])

        build.title_labels(n,vis,ui,view_dict[q],title_label_list)
        build.value_labels(n,vis,ui,view_dict[q],value_label_list)

    for c,subview in enumerate(view_dict): #for each view, create button and add to main view
        if "AM" in subview:
            button = build.switch_buttons(c,subview,vis,ui) #pass cycle number, view name(data), vis library and ui element
            button.action = switch_pressed
            view.add_subview(button) #each view gets a button

first_run(forecast_dict,view)

view.present(style='sheet', hide_title_bar=True)
