"""
@author: Cuong Pham <giacuong171@gmail.com>
"""
import os
import cv2
from pygame.image import load
from pygame import RLEACCEL
from pygame import (
    Rect, 
    init, 
    time, 
    display,  
    mixer, 
    transform, 
    surface
    )

mixer.pre_init(44100, -16, 2, 2048)
# initialize all imported pygame modules
init()

#set screen size
scr_size = (width, height) = (600, 150)
FPS = 60
gravity = 0.6

black = (0, 0, 0)
white = (255, 255, 255)
background_col = (235, 235, 235)

high_score = 0

screen = display.set_mode(scr_size)
clock  = time.Clock()
display.set_caption("Dino Run")

def load_image(
        name,
        sizex=-1,#for transform image size
        sizey=-1,
        colorkey=None,
        ):
    sprites_path = os.path.join('assets/sprites',name)
    image = load(sprites_path)
    image = image.convert() #create a copy that will draw more quickly on the screen.
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
        #RLEACCEL: This flag will create the image with RLEACCEL set, 
        # which will make the image draw faster on the screen.
    if sizex != -1 or sizey != -1:
        image = transform.scale(image, (sizex, sizey))
    
    return (image, image.get_rect())

def load_sprite_sheet(
    sheetname,
    nx,
    ny,
    scalex = -1,
    scaley = -1,
    colorkey = None,):
    sheet_path = os.path.join('assets/sprites',sheetname)
    sheet = load(sheet_path)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()
    sprites = []

    sizey = sheet_rect.height/ny 
    if isinstance(nx, int):
        sizex = sheet_rect.width/nx 
        for i in range(0,ny):
            for j in range(0,nx):
                #Getting all sprites from the sprite sheet
                rect = Rect((sizex*j, sizey*i, sizex, sizey)) 
                image = surface.Surface(rect.size)
                image = image.convert()
                image.blit(sheet, (0, 0), rect) #draw many images onto another

                if colorkey is not None:
                    if colorkey is -1:
                        colorkey = image.get_at((0,0))
                    image.set_colorkey(colorkey, RLEACCEL)

                    if scalex != -1 or scaley != -1:
                        image = transform.scale(image, (scalex, scaley))

                    sprites.append(image)
    else:
        sizex_ls = [sheet_rect.width/ i_nx for i_nx in nx]
        for i in range(0,ny):
            for i_nx,size, i_scalex in zip(nx,sizex_ls,scalex):
                rect = Rect((sizex*j,sizey*i,sizex,sizey))
                image = surface.Surface(rect.size)
                image = image.convert()
                image.blit(sheet, (0,0), rect)

                if colorkey is not None:
                    if colorkey is -1:
                        colorkey = image.get_at((0,0))
                    image.set_colorkey(colorkey, RLEACCEL)

                    if scalex != -1 or scaley != -1:
                        image = transform.scale(image, (scalex, scaley))

                    sprites.append(image)
    
    sprite_rect = sprites[0].get_rect()
    return sprites, sprite_rect
                
if __name__ == "__main__":
    pass