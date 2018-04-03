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
    vis['subview_height'] = h-(vis['top_margin']*4)
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
    vis['title_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['title_label_height'] = vis['other_label_height']
    vis['title_label_margins'] = 1
    #Value Labels
    vis['value_label_width'] = vis['subview_width']-(vis['side_margin']*4)
    vis['value_label_height'] = vis['other_label_height']
    vis['value_label_margins'] = vis['title_label_margins']

    return vis

def subviews(n,vis,ui):
    subview_x = vis['side_margin'] + ( ( vis['w_adjusted'] / vis['entry_count'] ) *n) #this is dynamic
    n = n+1
    view_name = "view_"+str(n)
    subview = ui.ScrollView(frame=(subview_x, vis['subview_y'], vis['subview_width'], vis['subview_height']), background_color="#01B2FC")
    subview.border_color = 'black'
    subview.border_width = 0

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
