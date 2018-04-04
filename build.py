def vis(w,h,entry_count):

    #Static Entries
    vis = {}
    vis['side_margin'] = 5
    vis['w_adjusted'] = w-vis['side_margin']
    vis['top_margin'] = 20
    vis['other_label_height'] = 32
    vis['spacing_margin'] = 10
    vis['entry_count'] = entry_count
    #Subview
    vis['subview_width'] = (w/vis['entry_count'])-vis['side_margin']
    vis['subview_height'] = h-(vis['top_margin']*6)
    vis['subview_y'] = vis['top_margin']
    vis['subview_x'] = vis['side_margin']
    #Header
    vis['header_x'] = vis['side_margin'] * 2
    vis['header_y'] = vis['top_margin'] / 2
    vis['header_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['header_height'] = 64
    #Image View
    vis['imageview_x'] = vis['side_margin'] * 4
    vis['imageview_y'] = vis['header_y'] + vis['header_height'] + vis['spacing_margin']
    vis['imageview_width'] = vis['subview_width'] - (vis['side_margin'] *8)
    vis['imageview_height'] = vis['imageview_width']
    #Title Labels
    vis['title_label_x'] = vis['side_margin']
    vis['title_label_y'] = vis['imageview_y']+vis['imageview_height']
    vis['title_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['title_label_height'] = vis['other_label_height']
    vis['title_label_margins'] = 1
    #Value Labels
    vis['value_label_x'] = vis['side_margin'] * 2
    vis['value_label_y'] = vis['imageview_y'] + vis['imageview_height'] + (vis['other_label_height']/2)
    vis['value_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['value_label_height'] = vis['other_label_height']
    vis['value_label_margins'] = vis['title_label_margins']
    #Buttons
    #vis['button_x'] = vis['header_x'] + vis['subview_x']#subviewx + header_x
    vis['button_height'] = 32 #above button_y
    vis['button_y'] = h - vis['button_height'] - 5 #view height minus button height plus some
    vis['button_width'] = vis['header_width']


    return vis

def AM_titles_and_values(day):
    #put toogether dictionary of data we want to display based on forecast dict
    title_label_list = ['Condition:','Actual Temp:','Feels Like:','Windchill:','% Precipitation:','Humidity:','Astro Twilight:',\
                        'Nautical Twilight:','Civil Twilight:','Sunrise:','Windspeed:']

    value_label_list = []
    value_label_list.append(day['weather']['condition'])
    value_label_list.append(day['weather']['temp']['english'])
    value_label_list.append(day['weather']['feelslike']['english'])
    value_label_list.append(day['weather']['windchill']['english'])
    value_label_list.append(day['weather']['pop'])
    value_label_list.append(day['weather']['humidity'])
    value_label_list.append(day['twilight']['astronomical_twilight_begin_time'])
    value_label_list.append(day['twilight']['nautical_twilight_begin_time'])
    value_label_list.append(day['twilight']['civil_twilight_begin_time'])
    value_label_list.append(day['twilight']['sunrise_time'])
    value_label_list.append(day['weather']['wspd']['english'])

    return title_label_list,value_label_list

def PM_titles_and_values(day):
    #put toogether dictionary of data we want to display based on forecast dict
    title_label_list = ['Condition:','Actual Temp:','Feels Like:','Windchill:','% Precipitation:','Humidity:','Sunset:',\
                        'Civil Twilight:','Nautical Twilight:','Astro Twilight:','Windspeed:']

    value_label_list = []
    value_label_list.append(day['weather']['condition'])
    value_label_list.append(day['weather']['temp']['english'])
    value_label_list.append(day['weather']['feelslike']['english'])
    value_label_list.append(day['weather']['windchill']['english'])
    value_label_list.append(day['weather']['pop'])
    value_label_list.append(day['weather']['humidity'])
    value_label_list.append(day['twilight']['sunset_time'])
    value_label_list.append(day['twilight']['civil_twilight_end_time'])
    value_label_list.append(day['twilight']['nautical_twilight_end_time'])
    value_label_list.append(day['twilight']['astronomical_twilight_end_time'])
    value_label_list.append(day['weather']['wspd']['english'])

    return title_label_list,value_label_list

def subviews(n,vis,ui):
    subview_x = vis['side_margin'] + ( ( vis['w_adjusted'] / vis['entry_count'] ) *n) #this is dynamic
    n = n+1
    view_name = "view_"+str(n)
    subview = ui.ScrollView(frame=(subview_x, vis['subview_y'], vis['subview_width'], vis['subview_height']), background_color="#01B2FC")
    subview.border_color = 'black'
    subview.border_width = 0
    subview.title = view_name

    return subview #return object

def headers(n,vis,ui,day,view_name):
    #Headers
    label_name = "label"+str(n)
    header = ui.Label(name = label_name, bg_color ='white', frame = (vis['header_x'], vis['header_y'], vis['header_width'], vis['header_height']))
    header.border_color = 'black'
    header.tint_color = 'black'
    header.border_width = 1
    header.alignment = 1 #1 is center, 0 is left justified
    header.font = ('<system>',17)
    header.number_of_lines = 3
    header.text = day['time']['mon_abbrev']+" "+day['time']['mday']+" "+day['time']['weekday_name']+" "+day['time']['civil']

    return header

def imageview(n,vis,ui,day,view_name):
    #Image View
    image_view_name = "imageview"+str(n)
    imageview = ui.ImageView(name=image_view_name, bg_color='white', frame=(vis['imageview_x'], vis['imageview_y'], vis['imageview_width'], vis['imageview_height']))
    imageview.load_from_url(day['weather']['icon_url'])
    imageview.border_width = 1
    imageview.border_color = "grey"

    return imageview

def title_labels(n,vis,ui,view_name,title_label_list,timeset):

    for x,text in enumerate(title_label_list):
        adjusted_label_y = vis['title_label_y'] +( x*( vis['other_label_height'] + vis['title_label_margins'] ) )
        x = x+1
        label_name = "tlabel"+str(view_name)+str(x)
        label = ui.Label(name = label_name, bg_color ='transparent', frame = (vis['title_label_x'], adjusted_label_y, vis['title_label_width'], vis['title_label_height']))
        label.border_color = 'black'
        if timeset == 'AM':
            label.text_color = 'black'
        if timest == 'PM':
            label.text_color = 'white'
        label.border_width = 0
        label.alignment = 0 #1 is center, #0 is left justified
        label.font = ('<system>',12)
        label.number_of_lines = 1
        label.text = text
        view_name.add_subview(label)

def value_labels(n,vis,ui,view_name,value_label_list,timeset):
    for x,text in enumerate(value_label_list):
        adjusted_label_y = vis['value_label_y'] +( x*(vis['value_label_height']+vis['title_label_margins']) )
        x = x+1
        label_name = "vlabel"+str(view_name)+str(x)
        label = ui.Label(name = label_name, bg_color ='transparent', frame = (vis['value_label_x'], adjusted_label_y, vis['value_label_width'], vis['value_label_height']))
        label.border_color = 'black'
        if timeset == 'AM':
            label.text_color = 'black'
        if timest == 'PM':
            label.text_color = 'white'
        label.border_width = 0
        label.alignment = 3 #1 is center, #0 is left justified
        label.font = ('<system>',14)
        label.number_of_lines = 1
        label.text = str(text)
        view_name.add_subview(label)

def switch_buttons(n,view_name,vis,ui):
    #Buttons
    button_x = vis['header_x'] + vis['side_margin'] + ( ( vis['w_adjusted'] / vis['entry_count'] ) * (n-1)) #has to be dynamic
    button_name = "button_"+str(view_name)
    button = ui.Button(name = button_name, bg_color ='white', frame = (button_x, vis['button_y'], vis['button_width'], vis['button_height']))
    button.border_color = 'black'
    button.tint_color = 'blue'
    button.border_width = 1
    button.alignment = 1 #1 is center, 0 is left justified
    button.font = ('<system>',12)
    button.number_of_lines = 1
    button.title = "AM/PM"

    return button
