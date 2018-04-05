import get_data
import ui
import build
from pprint import pprint


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

def switch_pressed(self):
    print ("Pressed "+self.name)
    if "AM" in self.name: #passed name like button_AM1
        #print("Button pressed and AM displayed")
        view_name = self.name.replace("button_","")
        view_number = view_name.replace("AM","")
        new_view_name = "PM"+view_number
        view.remove_subview(view_dict[view_name]) #view_dict contains names as keys and view objects as values
        view.remove_subview(self) #remove button
        view.add_subview(view_dict[new_view_name])

        #add back button with PM name
        button = build.switch_buttons(int(view_number),new_view_name,vis,ui) #pass cycle number, view name(data), vis library and ui element
        button.action = switch_pressed
        view.add_subview(button)

    if "PM" in self.name:
        #print("Button pressed and PM displayed")
        view_name = self.name.replace("button_","")
        view_number = view_name.replace("PM","")
        new_view_name = "AM"+view_number
        view.remove_subview(view_dict[view_name]) #view_dict contains names as keys and view objects as values
        view.remove_subview(self) #remove button
        view.add_subview(view_dict[new_view_name])

        #add back button with PM name
        button = build.switch_buttons(int(view_number),new_view_name,vis,ui) #pass cycle number, view name(data), vis library and ui element
        button.action = switch_pressed
        view.add_subview(button)

def first_run(forecast_dict,view):
    am_count = len(forecast_dict['AM'])
    pm_count = len(forecast_dict['PM'])
    global vis
    if pm_count == am_count:
        vis = build.vis(w,h,am_count)
    if pm_count > am_count:
        #need to create additional AM entry to fill in missing entry
        #USE PM ENTRY TWICE
        vis = build.vis(w,h,pm_count)
    #create view dictionary
    global view_dict
    view_dict = {}

    for n,day in enumerate(forecast_dict['AM']):
        d = n+1
        q = 'AM'+str(d)
        view_dict[q] = build.subviews(n,vis,ui) #build dictionary
        #view.add_subview(view_dict[subview])view.add_subview(view_dict[q])
        # #add subview to main view

        header = build.headers(n,vis,ui,forecast_dict['AM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
        view_dict[q].add_subview(header)

        #the load from url option seems to be freezing every once in a while
        #imageview = build.imageview(n,vis,ui,forecast_dict[day],view_dict[q])
        #view_dict[q].add_subview(imageview)

        title_label_list,value_label_list = build.AM_titles_and_values(forecast_dict['AM'][day])

        build.title_labels(n,vis,ui,view_dict[q],title_label_list,'AM')
        build.value_labels(n,vis,ui,view_dict[q],value_label_list,'AM')

    for n,day in enumerate(forecast_dict['PM']):
        d = n+1
        q = 'PM'+str(d)
        view_dict[q] = build.subviews(n,vis,ui) #build dictionary
        view_dict[q].background_color = "#0952c6" #change for PM
        #view.add_subview(view_dict[q]) #add subview to main view

        header = build.headers(n,vis,ui,forecast_dict['PM'][day],view_dict[q]) #n, vis dict, ui object, day info, view_name
        view_dict[q].add_subview(header)

        title_label_list,value_label_list = build.PM_titles_and_values(forecast_dict['PM'][day])

        build.title_labels(n,vis,ui,view_dict[q],title_label_list,'PM')
        build.value_labels(n,vis,ui,view_dict[q],value_label_list,'PM')

    if am_count == pm_count:
        for c,subview in enumerate(view_dict):
            if "AM" in subview:
                view.add_subview(view_dict[subview])
                d = c+1 #start with button 1, not 0
                button = build.switch_buttons(d,subview,vis,ui) #pass cycle number, view name(data), vis library and ui element
                button.action = switch_pressed
                view.add_subview(button) #each view gets a button
    else:
        if pm_count > am_count: #on a run day, but after the morning has passed
            count = 0 #have to reset and not use enumerate because PM comes later in dict than AM
            #need to clone the PM1 to AM1, then push AM1 to AM2
            #Push AM1 to AM2, HOW?
            new_view_dict = {}
            for subview in view_dict: #modify view_dict to show two PM views for AM1 and PM1
                if "AM" in subview:
                    AM_number = int(subview.replace("AM",""))
                    AM_number_plus = AM_number + 1
                    new_view_dict["AM"+str(AM_number_plus)] = view_dict[subview]
                if subview == "PM1": #copy PM1 to AM1
                    new_view_dict['AM1'] == view_dict[subview]
                if "PM" in subview: #move from old to new dictionary
                    new_view_dict[subview] = view_dict[subview]

            for subview in new_view_dict: #now that view_dict should be the way we want it
                if "AM" in subview: #still show AM side first (most important)
                    view.add_subview(view_dict[subview])
                    d = c+1 #start with button 1, not 0
                    button = build.switch_buttons(d,subview,vis,ui) #pass cycle number, view name(data), vis library and ui element
                    button.action = switch_pressed
                    view.add_subview(button) #each view gets a button

                # if "PM" in subview:
                #     count = count + 1
                #     view.add_subview(view_dict[subview])
                #     print(view_dict[subview])
                #     print()
                #     button = build.switch_buttons(count,subview,vis,ui)
                #     button.action = switch_pressed
                #     view.add_subview(button)

first_run(forecast_dict,view)

view.present(style='sheet', hide_title_bar=True)
