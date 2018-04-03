import get_data
import ui

def create_title_label(label_name,label_x,label_y,label_width,label_height):

    #label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='transparent', frame = (label_x, label_y, label_width, label_height))
    label_name.border_color = 'black'
    label_name.text_color = 'black'
    label_name.border_width = 0
    label_name.alignment = 0 #1 is center, #0 is left justified
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 1
    return label_name

def create_value_label(label_name,label_x,label_y,label_width,label_height):
    label_name = ui.Label(name = label_name, bg_color ='transparent', frame = (label_x, label_y, label_width, label_height))
    label_name.border_color = 'black'
    label_name.text_color = 'white'
    label_name.border_width = 0
    label_name.alignment = 3 #1 is center, #0 is left justified
    label_name.font = ('<system>',14)
    label_name.number_of_lines = 1
    return label_name

def build_outputs(forecast_dict):
    #put toogether dictionary of data we want to display based on forecast dict
    title_label_list = ['Condition:','Actual Temp:','Feels Like:','Windchill:','% Precipitation:','Humidity:','Astro Twilight:',\
                        'Nautical Twilight:','Civil Twilight:','Sunrise:','Windspeed:']

    value_label_list = []
    value_label_list.append(forecast_dict[day]['weather']['condition'])
    value_label_list.append(forecast_dict[day]['weather']['temp']['english'])
    value_label_list.append(forecast_dict[day]['weather']['feelslike']['english'])
    value_label_list.append(forecast_dict[day]['weather']['windchill']['english'])
    value_label_list.append(forecast_dict[day]['weather']['pop'])
    value_label_list.append(forecast_dict[day]['weather']['humidity'])
    value_label_list.append(forecast_dict[day]['twilight']['astronomical_twilight_begin_time'])
    value_label_list.append(forecast_dict[day]['twilight']['nautical_twilight_begin_time'])
    value_label_list.append(forecast_dict[day]['twilight']['civil_twilight_begin_time'])
    value_label_list.append(forecast_dict[day]['twilight']['sunrise_time'])
    value_label_list.append(forecast_dict[day]['weather']['wspd']['english'])

    return dict(zip(title_label_list,value_label_list))

def build_vis(w,h,entry_count):

    vis = {}
    vis['side_margin'] = 5
    vis['w_adjusted'] = w-vis['side_margin']
    vis['top_margin'] = 20
    vis['other_label_height'] = 32
    vis['spacing_margin'] = 10
    vis['entry_count'] = entry_count
    #for the subviews
    #vis['subview_x'] = vis['side_margin']+((w/vis['entry_count'])*n)
    #vis['subview_y'] = vis['top_margin']
    vis['subview_width'] = (w/vis['entry_count'])-vis['side_margin']
    vis['subview_height'] = h-(vis['top_margin']*4)
    #for the header titles
    vis['header_x'] = vis['side_margin'] * 2
    vis['header_y'] = vis['top_margin'] / 2
    vis['header_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['header_height'] = 64
    #for the image_view_name
    vis['imageview_x'] = vis['side_margin'] * 4
    vis['imageview_y'] = vis['header_y'] + vis['header_height'] + vis['spacing_margin']
    vis['imageview_width'] = vis['subview_width'] - (vis['side_margin'] *8)
    vis['imageview_height'] = vis['imageview_width']
    #for title labels
    #vis['title_label_x'] = vis['side_margin']
    #vis['title_label_y'] =  frame_y+frame_height +( x*(other_label_height+label_margins) )
    vis['title_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['title_label_height'] = vis['other_label_height']
    vis['title_label_margins'] = 1
    #for value labels
    #vis['value_label_x'] = vis['side_margin']*2
    #vis['value_label_y'] =  frame_y+frame_height+(other_label_height/2) +( x*(other_label_height+label_margins) )
    vis['value_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['value_label_height'] = vis['other_label_height']
    vis['value_label_margins'] = vis['title_label_margins']

    return vis

def build_subviews(n,vis):
    #sub-views
    #dd contains data about this subview
    #use it to change background?
    subview_x = vis['side_margin'] + ( ( vis['w_adjusted'] / vis['entry_count'] ) *n)
    n = n+1
    view_name = "view_"+str(n)
    view_number = str(n)
    view_name = ui.ScrollView(frame=(subview_x, vis['top_margin'], vis['subview_width'], vis['subview_height']), background_color="#01B2FC")
    view_name.border_color = 'black'
    view_name.border_width = 0

    return view_name

def build_headers(n,day,vis,view_name):
    #Headers
    label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (vis['header_x'], vis['header_y'], vis['header_width'], vis['header_height']))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 1 #1 is center, 0 is left justified
    label_name.font = ('<system>',17)
    label_name.number_of_lines = 3
    label_name.text = day['time']['mon_abbrev']+" "+day['time']['mday']+" "+day['time']['weekday_name']+" "+day['time']['civil']
    view_name.add_subview(label_name)

def build_imageview(n,day,vis,view_name):
    #Image View
    image_view_name = "ImageView"+str(n)
    image_view_name = ui.ImageView(name=image_view_name, bg_color='white', frame=(vis['imageview_x'], vis['imageview_y'], vis['imageview_width'], vis['imageview_height']))
    image_view_name.load_from_url(day['weather']['icon_url'])
    image_view_name.border_width = 1
    image_view_name.border_color = "grey"
    view_name.add_subview(image_view_name)

def build_title_labels(n,forecast_dict):

    title_label_x = side_margin
    title_label_y = frame_y+frame_height
    title_label_width = view_width-(side_margin*4)
    title_label_height = other_label_height
    label_margins = 1
    for x,text in enumerate(title_label_list):
        adjusted_label_y = title_label_y +( x*(other_label_height+label_margins) )
        x = x+1
        label_name = "tlabel"+view_number+str(x)
        label_name = create_title_label(label_name, title_label_x, adjusted_label_y, title_label_width, title_label_height)
        label_name.text = text
        view_name.add_subview(label_name)

def build_view_labels(n,forecast_dict):
    #Value Labels
    # value_label_list = []
    # value_label_list.append(forecast_dict[day]['weather']['condition'])
    # value_label_list.append(forecast_dict[day]['weather']['temp']['english'])
    # value_label_list.append(forecast_dict[day]['weather']['feelslike']['english'])
    # value_label_list.append(forecast_dict[day]['weather']['windchill']['english'])
    # value_label_list.append(forecast_dict[day]['weather']['pop'])
    # value_label_list.append(forecast_dict[day]['weather']['humidity'])
    # value_label_list.append(forecast_dict[day]['twilight']['astronomical_twilight_begin_time'])
    # value_label_list.append(forecast_dict[day]['twilight']['nautical_twilight_begin_time'])
    # value_label_list.append(forecast_dict[day]['twilight']['civil_twilight_begin_time'])
    # value_label_list.append(forecast_dict[day]['twilight']['sunrise_time'])
    # value_label_list.append(forecast_dict[day]['weather']['wspd']['english'])

    value_label_x = side_margin*2
    value_label_y = frame_y+frame_height+(other_label_height/2)
    value_label_width = view_width-(side_margin*4)
    value_label_height = other_label_height
    for x,text in enumerate(value_label_list):
        adjusted_label_y = value_label_y +( x*(other_label_height+label_margins) )
        x = x+1
        label_name = "vlabel"+view_number+str(x)
        label_name = create_value_label(label_name, value_label_x, adjusted_label_y, value_label_width, value_label_height)
        label_name.text = str(text)
        view_name.add_subview(label_name)

    view.add_subview(view_name)

w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

forecast_dict = get_data.forecast_me() #get actual data

 #create dictionary of labels and values for display from dictionary
vis = build_vis(w,h,len(forecast_dict)) #build measurement dictionary to use

for n,day in enumerate(forecast_dict): #enumerate over data dictionary, each day is a cycle
    view_dictionary = {}
    dd = build_outputs(forecast_dict) #do i need to add more outputs or use forecast_dict?
    viewname = build_subviews(n,vis)
    view_dictionary[n+1] = viewname #create dictionary for addressing views later

    build_headers(n,forecast_dict[day],vis,viewname) #pass the day information
    build_imageview(n,forecast_dict[day],vis,viewname)

    #build_title_labels(n,forecast_dict[day],vis,dd)
    #build_view_labels(n,forecast_dict[day],vis,dd)

view.present(style='sheet', hide_title_bar=True)
