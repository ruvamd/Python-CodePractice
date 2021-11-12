# def make_album(name,title,n_songs=None):
#     album_info={'alb_name':name,
#                 'titl_name':title,}
#     if n_songs:
#         album_info['n_songs']=n_songs
#     return album_info

# albums=make_album('a','b',n_songs=4)
# print(albums)

#user albums
def make_album(name,title,n_songs=None):
    album_info=f'the album name is {name} and the title {title}'
    if n_songs:
        album_info['n_songs']=n_songs
    return album_info

while True:
    print('enter q if finished')
    a_name=input('enter album name:')
    if a_name=='q':
        break
    a_title=input('enter album title:')
    if a_title=='q':
        break
    f_a=make_album(a_name,a_title)
    print(f_a)