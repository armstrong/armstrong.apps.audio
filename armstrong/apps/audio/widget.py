#extends the widget thats part of 

def render(template='/arm_audio/jqplayer.html',):
    render_to_string(template,{"url":self.url, 'filetype':self.filetype})
