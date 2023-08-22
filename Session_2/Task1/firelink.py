#Make your module that contain favourite websites and have function called Firefox take url and open website 

import webbrowser

fav = {
    'facebook':'https://www.facebook.com/',
    'twitter' : 'https://twitter.com/home',
    'whatsapp web' : 'https://web.whatsapp.com/',
    'linkedin' : 'https://www.linkedin.com/feed/'
}

def firefox(fav_website):
    webbrowser.open(fav[fav_website.lower()])

