
import pygame
import numpy as np

# usefull?
#https://stackoverflow.com/questions/11846032/detect-mouseover-an-image-in-pygame

pygame.init()
display = pygame.display.set_mode((760, 760))
width, height = pygame.display.get_surface().get_size()


def make_hlayer(es,he):
    print(es.shape, he.shape)
    return np.concatenate([es,he,es,he,es,he,es], axis=0)

def pixels_to_surface(base, randoms, ve, hlayer):
    top = np.concatenate([ve, randoms[0], ve, randoms[1], ve, randoms[2], ve], axis=0)
    mid = np.concatenate([ve, randoms[3], ve, base, ve, randoms[4], ve], axis=0)
    bot = np.concatenate([ve, randoms[5], ve, randoms[6], ve, randoms[7], ve], axis=0)
    print(top.shape, mid.shape, bot.shape, hlayer.shape)
    return np.concatenate([hlayer,top,hlayer,mid,hlayer,bot,hlayer], axis=1)

def gen_rand():

    A = np.random.randint(300, size=(10,10))
    C = np.random.randint(300, size=(10,10))
    B = np.random.randint(300, size=(10,10))
    Z = np.stack([A,B,C], axis=2)
    Z = 255 * Z / Z.max()
    return Z.astype(int)

def gen_mut(base):

    An = np.random.randint(-50, 50, size=(10,10))
    Cn = np.random.randint(-50, 50, size=(10,10))
    Bn = np.random.randint(-50, 50, size=(10,10))
    Zn = np.stack([An,Bn,Cn], axis=2)
    new = Zn + base
    new[np.where(new > 255)] = 255
    new[np.where(new < 0)] = 0
    return new


def gen_N_muts(base, N):
    return [gen_mut(base) for _ in range(N)]



def coord_to_choice(x,y,b,s, scaling):
    b *= scaling
    s *= scaling
    if x > s and x < (s + b):
        if y > s and y < (s + b):
            return 1
        elif y > (2 * s + b) and y < (2 * s + 2 * b):
            return 4
        elif y > (3 * s + 2*b) and y < (3 * s + 3 * b):
            return 6
    elif x > (2*s + b) and x < (2 * s + 2 * b):
        if y > s and y < (s + b):
            return 2
        elif y > (3 * s + 2*b) and y < (3 * s + 3 * b):
            return 7
    else:
        if y > s and y < (s + b):
            return 3
        elif y > (2 * s + b) and y < (2 * s + 2 * b):
            return 5
        elif y > (3 * s + 2*b) and y < (3 * s + 3 * b):
            return 8


base = gen_rand()
randoms = gen_N_muts(base, 8)

big = 10
small = 2
scaling = 20

empty = np.zeros((small,small,3))
vert_empty = np.zeros((small,big, 3))
hor_empty = np.zeros((big,small, 3))


hlayer = make_hlayer(empty, hor_empty)
Z = pixels_to_surface(base, randoms, vert_empty, hlayer)


res = np.repeat(Z, scaling, axis=0)
res = np.repeat(res, scaling, axis=1)

surf = pygame.surfarray.make_surface(res)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            chosen = coord_to_choice(x, y, big, small, scaling)
            if chosen:
                newbase = randoms[chosen-1]
                randoms = gen_N_muts(randoms[chosen-1], 8)
                Z = pixels_to_surface(newbase, randoms, vert_empty, hlayer)
                res = np.repeat(Z, scaling, axis=0)
                res = np.repeat(res, scaling, axis=1)

                surf = pygame.surfarray.make_surface(res)

    display.blit(surf, (0, 0))
    pygame.display.update()
pygame.quit()