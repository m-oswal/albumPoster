from niceposter import Create as cr

import requests,os,PIL
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csvsongs
from PIL import Image
from son import songs,release,cover,runtime

prompts = csvsongs.prompt()
mulw = int(2481/595)
mulh = int(3507/842)
def main(album,artist):
    client_id = "your_client_id"
    client_secret = "secret_id"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q='album:"' + album + '" artist:"' + artist + '"', type='album')
    bg_image =  cr.Poster(base_size=(595*mulw,842*mulh),bg_color=('RGB',(255,255,250)),img_name=f'{album} by {artist}.png')

    slist = songs(album,artist,sp,results)
    n=len(slist)
    #text
    if n>14:
        temp=14
    else:
        temp=n
    for i in range(0,temp):
        bg_image.text(f"{i+1}. {slist[i]}", position=(74*mulw,(510+((i+1)*14))*mulh), color='black', align='center',font_style="fonts/ptext.ttf",text_size=18*mulw,textbox_width=500*mulw)
    if n>14:
        for i in range(0,n-14):
            bg_image.text(f"{i+15}. {slist[i+14]}", position=(225*mulw,(510+((i+1)*14))*mulh), color='black', align='center',font_style="fonts/ptext.ttf",text_size=18*mulh,textbox_width=500*mulw)

    #relase date
    date = release(album,artist,sp,results)
    run=runtime(album,artist,sp,results)
    bg_image.text(f"{run}/{date.upper()}" ,position=(74*mulw,(842-56-25)*mulh), color='black', align='center',font_style="fonts/releasedate.ttf",text_size=20*mulw,textbox_width=500*mulw)
    
    #released by
    rby = cover(album,artist,sp,results)
    
    bg_image.text(f"{rby.upper()}" ,position=(74*mulw,(842-65)*mulh), color='black', align='center',font_style="fonts/releasedate.ttf",text_size=20*mulw,textbox_width=500*mulw)
    #album Name on poster
    x=20
    album_font = PIL.ImageFont.truetype("fonts/album.otf", 30*mulw)
    width = album_font.getsize(album.upper())[0]
    h = album_font.getsize(album.upper())[1]
    bg_image.text(f" {album.upper()}" ,position=((521*mulw)-width,(842-55)*mulh-h), color='black', align='center',font_style="fonts/album.otf",text_size=30*mulw,textbox_width=500*mulw)

    #artist Name on poster
    
    artist_font = PIL.ImageFont.truetype("fonts/artist.otf", 20*mulw)
    a_width = artist_font.getsize(artist.upper())[0]
    bg_image.text(f" {artist.upper()}" ,position=((521*mulw)-a_width,((842-50-x)*mulh)-h), color='black', align='center',font_style="fonts/artist.otf",text_size=20*mulw,textbox_width=500*mulw)
    
    #image
    
    img = "album_art.jpg"
    bg_image.add_image(img,position=(74*mulw,56*mulh),resize=(447*mulw,447*mulw))
   
for i in prompts:
    album,artist = i
    main(album,artist)
print("done")
