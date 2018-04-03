import get_data
import ui


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))

side_margin = 5
w = w-side_margin
top_margin = 20
other_label_height = 32
spacing_margin = 15

forecast_dict = get_data.forecast_me()

def create_title_label(label_name,label_x,label_y,label_width,label_height):

    #label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='transparent', frame = (label_x, label_y, label_width, label_height))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 0
    label_name.alignment = 0 #1 is center, #0 is left justified
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 1
    return label_name

def create_value_label(label_name,label_x,label_y,label_width,label_height):
    label_name = ui.Label(name = label_name, bg_color ='transparent', frame = (label_x, label_y, label_width, label_height))
    label_name.border_color = 'black'
    label_name.tint_color = 'green'
    label_name.border_width = 0
    label_name.alignment = 3 #1 is center, #0 is left justified
    label_name.font = ('<system>',14)
    label_name.number_of_lines = 1
    return label_name

for n,day in enumerate(forecast_dict):
    entry_count = len(forecast_dict)
    view_x = side_margin+((w/entry_count)*n)
    view_width = (w/entry_count)-side_margin
    n = n+1

    view_name = "view_"+str(n)
    view_number = str(n)
    view_name = ui.ScrollView(frame=(view_x, top_margin, view_width, h-top_margin), background_color='lightyellow')
    view_name.border_color = 'black'
    view_name.border_width = 1

    #this creates the title labels at the top of the page
    header_label_width = view_width-(side_margin*4)
    header_label_height = 64 #title labels
    label_x = side_margin*2
    label_y = top_margin
    label_name = "label"+str(n)
    label_name = ui.Label(name = label_name, bg_color ='white', frame = (label_x, label_y, header_label_width, header_label_height))
    label_name.border_color = 'black'
    label_name.tint_color = 'black'
    label_name.border_width = 1
    label_name.alignment = 1 #1 is center, 0 is left justified
    label_name.font = ('<system>',12)
    label_name.number_of_lines = 2
    label_name.text = forecast_dict[day]['time']['pretty']
    view_name.add_subview(label_name)

    #image view from url
    frame_x = side_margin*2
    frame_y = top_margin + header_label_height + spacing_margin
    frame_width = view_width-(side_margin*4)
    frame_height = frame_width
    image_view_name = "ImageView"+str(n)
    image_view_name = ui.ImageView(name=image_view_name, bg_color='white', frame=(frame_x, frame_y, frame_width, frame_height))
    image_view_name.load_from_url(forecast_dict[day]['weather']['icon_url'])
    view_name.add_subview(image_view_name)

    #working on title labels for data
    #label101 - 1 is view and 01 is label number
    title_label_list = ['Condition','Feels Like','% Percip','Actual Temp','Astro Twilight','Civil Twilight','Sunrise']
    title_label_x = side_margin
    title_label_y = frame_y+frame_height
    title_label_width = view_width-(side_margin*4)
    title_label_height = other_label_height
    label_margins = 1
    for x,text in enumerate(title_label_list):
        x = x+1
        adjusted_label_y = title_label_y +( x*(other_label_height+label_margins) )
        label_name = "tlabel"+view_number+str(x)
        label_name = create_title_label(label_name, title_label_x, adjusted_label_y, title_label_width, title_label_height)
        label_name.text = text
        view_name.add_subview(label_name)

    #working on value labels
    value_label_list = []
    value_label_list.append(forecast_dict[day]['weather']['condition'])
    value_label_list.append(forecast_dict[day]['weather']['feelslike']['english'])
    value_label_list.append(forecast_dict[day]['weather']['pop'])
    value_label_list.append(forecast_dict[day]['weather']['temp']['english'])
    value_label_list.append(forecast_dict[day]['twilight']['astronomical_twilight_begin_time'])
    value_label_list.append(forecast_dict[day]['twilight']['civil_twilight_begin_time'])
    value_label_list.append(forecast_dict[day]['twilight']['sunrise_time'])

    value_label_x = side_margin*2
    value_label_y = frame_y+frame_height+spacing_margin
    value_label_width = view_width-(side_margin*4)
    value_label_height = other_label_height
    for x,text in enumerate(value_label_list):
        x = x+1
        adjusted_label_y = value_label_y +( x*(other_label_height+label_margins) )
        label_name = "vlabel"+view_number+str(x)
        label_name = create_value_label(label_name, value_label_x, adjusted_label_y, value_label_width, value_label_height)
        label_name.text = str(text)
        view_name.add_subview(label_name)

    view.add_subview(view_name)


view.present(style='sheet', hide_title_bar=True)
