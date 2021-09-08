# faire interaction avec le bouton engrenage

"""les import"""
import sys

sys.path.append(".\classes")

# les classes
from os import environ
from pygame_button import *
from return_text import *
from Player import *
from load_img import *
from open_doctxt import *
from play_son import *
# les constantes
from constants import *

import pygame
from pygame.locals import *
import random
import pickle

"""les def()"""


def draw_credits():
    global rectangle4, rectangle2, rectangle3, rectangle, rectangle5, rectangle6, rectangle8
    if nom_fen == "credits":
        ft = pygame.font.Font(police, 50)
        text = ft.render("les credits", True, blanc[0])
        fen.blit(text, (50, 50))
        les_credit = Text(credit, 20, 125, 960, 30, police, blanc[0], noir[0], "left")
        les_credit.show(fen)

        rectangle8 = Bouton(blanc[0], 375, 525, 250, 50, "retour", 20, police, noir[0])
        rectangle8.draw(fen, (0, 0, 0))


def draw_collection():
    global rectangle4, rectangle2, rectangle3, rectangle, rectangle5, rectangle6, rectangle8
    if nom_fen == "collection":
        ft = pygame.font.Font(police, 50)
        text = ft.render("Collection :", True, blanc[0])
        fen.blit(text, (50, 50))

        if lock[0] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre1
        collection1 = Bouton(blanc[0], 25, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (22, 147, 81, 81))
        collection1.draw(fen, noir[0])

        if lock[1] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre2
        collection2 = Bouton(blanc[0], 150, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (147, 147, 81, 81))
        collection2.draw(fen, noir[0])

        if lock[2] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre3
        collection3 = Bouton(blanc[0], 275, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (272, 147, 81, 81))
        collection3.draw(fen, noir[0])

        if lock[3] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre4
        collection4 = Bouton(blanc[0], 400, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (397, 147, 81, 81))
        collection4.draw(fen, noir[0])

        if lock[4] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre5
        collection5 = Bouton(blanc[0], 525, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (522, 147, 81, 81))
        collection5.draw(fen, noir[0])

        if lock[5] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre6
        collection6 = Bouton(blanc[0], 650, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (647, 147, 81, 81))
        collection6.draw(fen, noir[0])

        if lock[6] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre7
        collection7 = Bouton(blanc[0], 775, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (772, 147, 81, 81))
        collection7.draw(fen, noir[0])

        if lock[7] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre8
        collection8 = Bouton(blanc[0], 900, 150, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, vert[0], (897, 147, 81, 81))
        collection8.draw(fen, noir[0])

        if lock[8] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre9
        collection9 = Bouton(blanc[0], 25, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (22, 272, 81, 81))
        collection9.draw(fen, noir[0])

        if lock[9] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre10
        collection10 = Bouton(blanc[0], 150, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (147, 272, 81, 81))
        collection10.draw(fen, noir[0])

        if lock[10] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre11
        collection11 = Bouton(blanc[0], 275, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (272, 272, 81, 81))
        collection11.draw(fen, noir[0])

        if lock[11] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre12
        collection12 = Bouton(blanc[0], 400, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (397, 272, 81, 81))
        collection12.draw(fen, noir[0])

        if lock[12] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre13
        collection13 = Bouton(blanc[0], 525, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (522, 272, 81, 81))
        collection13.draw(fen, noir[0])

        if lock[13] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre14
        collection14 = Bouton(blanc[0], 650, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (647, 272, 81, 81))
        collection14.draw(fen, noir[0])

        if lock[14] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre15
        collection15 = Bouton(blanc[0], 775, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (772, 272, 81, 81))
        collection15.draw(fen, noir[0])

        if lock[15] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre16
        collection16 = Bouton(blanc[0], 900, 275, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, bleu[0], (897, 272, 81, 81))
        collection16.draw(fen, noir[0])

        if lock[16] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre17
        collection17 = Bouton(blanc[0], 25, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, violet[0], (22, 397, 81, 81))
        collection17.draw(fen, noir[0])

        if lock[17] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre18
        collection18 = Bouton(blanc[0], 150, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, violet[0], (147, 397, 81, 81))
        collection18.draw(fen, noir[0])

        if lock[18] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre19
        collection19 = Bouton(blanc[0], 275, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, violet[0], (272, 397, 81, 81))
        collection19.draw(fen, noir[0])

        if lock[19] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre20
        collection20 = Bouton(blanc[0], 400, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, violet[0], (397, 397, 81, 81))
        collection20.draw(fen, noir[0])

        if lock[20] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre21
        collection21 = Bouton(blanc[0], 525, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, violet[0], (522, 397, 81, 81))
        collection21.draw(fen, noir[0])

        if lock[21] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre22
        collection22 = Bouton(blanc[0], 650, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, jaune[0], (647, 397, 81, 81))
        collection22.draw(fen, noir[0])

        if lock[22] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre23
        collection23 = Bouton(blanc[0], 775, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, jaune[0], (772, 397, 81, 81))
        collection23.draw(fen, noir[0])

        if lock[23] == True:
            a = src_img_monstre_lock
        else:
            a = src_img_monstre24
        collection24 = Bouton(blanc[0], 900, 400, 75, 75, "", 20, police, noir[0], a)
        pygame.draw.rect(fen, jaune[0], (897, 397, 81, 81))
        collection24.draw(fen, noir[0])

        rectangle8 = Bouton(blanc[0], 375, 525, 250, 50, "retour", 20, police, noir[0])
        rectangle8.draw(fen, (0, 0, 0))


def draw_menu():
    global rectangle4, rectangle2, rectangle3, rectangle, rectangle5, rectangle6, rectangle8, x_menu, y_menu, alpha_titre, pause_intro

    if nom_fen == "menu":
        palier = 0
        for l in player.bots:
            palier += l.mult * l.val_argent
        if palier < 10:
            a = src_img_fond_menu1
        elif palier < 30:
            a = src_img_fond_menu2
        elif palier < 100:
            a = src_img_fond_menu3
        elif palier < 300:
            a = src_img_fond_menu4
        elif palier < 1000:
            a = src_img_fond_menu5
        load_img(a, (0, 0), fen)

        if pause_intro > 100:
            s_titre = pygame.Surface((700, 75))
            s_titre.fill((255, 0, 255))
            s_titre.set_colorkey((255, 0, 255))
            s_titre.set_alpha(alpha_titre)
            ft = pygame.font.Font(police, 70)
            text = ft.render('MONSTER CLICKER', 1, blanc[0])
            s_titre.blit(text, (0, 0))
            fen.blit(s_titre, (40, 40))

            rectangle3 = Bouton(blanc[0], 20 + x_menu, 150, 350, 100, "JOUER", 40, police, noir[0])
            rectangle3.draw(fen, (0, 0, 0))

            rectangle2 = Bouton(blanc[0], 20 + x_menu, 300, 350, 100, "SHOP", 40, police, noir[0])
            rectangle2.draw(fen, (0, 0, 0))

            rectangle = Bouton(blanc[0], 20 + x_menu, 450, 350, 100, "COLLECTION", 40, police, noir[0])
            rectangle.draw(fen, (0, 0, 0))

            rectangle4 = Bouton(blanc[0], 800, 10 + y_menu, 40, 40, "C", 20, police, noir[0])
            rectangle4.draw(fen, blanc[0])

            if son == "off":
                image = src_img_son_off
            else:
                image = src_img_son_on
            rectangle5 = Bouton(blanc[0], 860, 10 + y_menu, 50, 50, "", 20, police, noir[0], image)
            rectangle5.draw(fen, (0, 0, 0))

            if musique == "off":
                image = src_img_musique_off
            else:
                image = src_img_musique_on

            rectangle6 = Bouton(blanc[0], 920, 10 + y_menu, 50, 50, "", 20, police, noir[0], image)
            rectangle6.draw(fen, (0, 0, 0))

            if alpha_titre < 255:
                alpha_titre += 5
            else:
                if x_menu < 0:
                    x_menu += 7
                if y_menu < 0:
                    y_menu += 1
        else:
            pause_intro += 1


def save():
    src = open(src_save_init, "w")
    txt = son + "\n" + musique + "\n"
    src.write(txt)
    src.close()

    with open('resources/save/player', 'wb') as fichier:
        sauvegarde = {
            'argent': player.argent,
            'uranium': player.uranium,
            'bots': player.bots,
            'val_argent': player.val_argent,
            'val_uranium': player.val_uranium,
            'mult': player.mult
        }
        a = pickle.Pickler(fichier)
        a.dump(sauvegarde)

    contenus = ""
    with open('resources/save/lock.txt', 'w') as fichier:
        for ppp in lock:
            contenus += str(int(ppp)) + "\n"
        fichier.write(contenus)


def init_clique_menu():
    global y_barre, x_son, x_musique, y_bouton1_menu_barre, y_bouton2_menu_barre, y_bouton3_menu_barre
    y_barre = -40
    x_son = 0
    x_musique = 0
    y_bouton1_menu_barre = 0
    y_bouton2_menu_barre = 0
    y_bouton3_menu_barre = 0


def init_intro():
    global x_menu, y_menu, alpha_titre, alpha_intro, sens_intro, pause_intro
    x_menu = -450
    y_menu = -65
    alpha_titre = 0
    alpha_intro = 0
    pause_intro = 0
    sens_intro = "up"


def init_shop():
    global x_barre_shop, nom_rubrique_shop, alpha_fond_shop
    x_barre_shop = -200
    alpha_fond_shop = 0
    nom_rubrique_shop = "materiaux"


def init_barre():
    global option_barre, menu_barre, list_menu_barre
    option_barre = False
    menu_barre = False
    list_menu_barre = ["menu"]
    if nom_fen != "jouer":
        list_menu_barre += ["jouer"]
    if nom_fen != "shop":
        list_menu_barre += ["shop"]
    list_menu_barre += ["collection"]


def draw_intro():
    global alpha_intro, nom_fen, sens_intro, pause_intro
    img = pygame.image.load(src_img_logo).convert_alpha()
    if alpha_intro == 9 and sens_intro == "up" and son == "on":
        play_son(intro)
    s_logo = pygame.Surface((400, 400))
    s_logo.set_alpha(alpha_intro)
    s_logo.blit(img, (0, 0))
    fen.blit(s_logo, (300, 100))

    if sens_intro == "up":
        if alpha_intro < 255:
            alpha_intro += 3
        else:
            pause_intro += 1

    if pause_intro == 50:
        sens_intro = "down"

    if sens_intro == "down":
        if alpha_intro > 0:
            alpha_intro -= 3
        else:
            pause_intro += 1

    if pause_intro == 75:
        nom_fen = "menu"


def draw_barre():
    global pos_engrenage, pos_menu_barre, pos_son_j, pos_musique_j, bouton1_menu_barre, bouton2_menu_barre, bouton3_menu_barre, x_son, x_musique, y_bouton1_menu_barre, y_bouton2_menu_barre, y_barre, y_bouton3_menu_barre
    # barre
    barre = pygame.Surface((TAILLE_FEN[0], 40))
    barre.fill(blanc[0])

    # image menu
    pos_obj = TAILLE_FEN[0] - 60, 0
    load_img(src_img_triple_trait, pos_obj, barre)
    pos_menu_barre = pos_obj[0], pos_obj[1] + y_barre

    """ressource"""
    # argent
    pos_obj = pos_obj[0] - 35, (40 - 25) / 2
    load_img(src_img_piece, pos_obj, barre)

    ft = pygame.font.Font(police, 20)
    text = ft.render(str(player.argent), True, noir[0])
    pos_obj = pos_obj[0] - 10 - text.get_width(), (40 - text.get_height()) // 2 + 3
    barre.blit(text, pos_obj)

    # uranium
    pos_obj = pos_obj[0] - 45, (40 - 25) / 2
    load_img(src_img_uranium, pos_obj, barre)

    ft = pygame.font.Font(police, 20)
    text = ft.render(str(player.uranium), True, noir[0])
    pos_obj = pos_obj[0] - 10 - text.get_width(), (40 - text.get_height()) // 2 + 3
    barre.blit(text, pos_obj)

    # image engrenage
    pos_obj = (0, 0)

    if option_barre == True and x_musique < 40:
        if x_son == 40:
            x_musique += 10
        else:
            x_son += 10

    if option_barre == False and x_son > 0:
        if x_musique == 0:
            x_son -= 10
        else:
            x_musique -= 10

    if x_musique > 0:
        pos_obj = pos_obj[0] + x_son, pos_obj[1]
        pos_obj = pos_obj[0] + x_musique, pos_obj[1]
        pos_musique_j = pos_obj[0], pos_obj[1] + y_barre
        if musique == "on":
            a = src_img_musique_on_jeu
        else:
            a = src_img_musique_off_jeu
        load_img(a, pos_obj, barre)

    if x_son > 0:
        pos_obj = (0, 0)
        pos_obj = pos_obj[0] + x_son, pos_obj[1]
        pos_son_j = pos_obj[0], pos_obj[1] + y_barre
        if son == "on":
            a = src_img_son_on_jeu
        else:
            a = src_img_son_off_jeu
        load_img(a, pos_obj, barre)

    pos_obj = (0, 0)
    load_img(src_img_engrenage, pos_obj, barre)
    pos_engrenage = pos_obj[0], pos_obj[1] + y_barre

    pos_obj = 800
    if menu_barre == True and y_bouton3_menu_barre < 50:
        if y_bouton2_menu_barre == 50:
            y_bouton3_menu_barre += 10
        elif y_bouton1_menu_barre == 50:
            y_bouton2_menu_barre += 10
        else:
            y_bouton1_menu_barre += 10

    if menu_barre == False and y_bouton1_menu_barre > 0:
        if y_bouton2_menu_barre == 0:
            y_bouton1_menu_barre -= 10
        elif y_bouton3_menu_barre == 0:
            y_bouton2_menu_barre -= 10
        else:
            y_bouton3_menu_barre -= 10

    if y_bouton3_menu_barre > 0:
        bouton3_menu_barre = Bouton(blanc[0], 800,
                                    -10 + y_barre + y_bouton1_menu_barre + y_bouton2_menu_barre + y_bouton3_menu_barre,
                                    200, 50, list_menu_barre[2], 30, police, noir[0])
        bouton3_menu_barre.draw(fen, noir[0])

    if y_bouton2_menu_barre > 0:
        bouton2_menu_barre = Bouton(blanc[0], 800, -10 + y_barre + y_bouton1_menu_barre + y_bouton2_menu_barre, 200, 50,
                                    list_menu_barre[1], 30, police, noir[0])
        bouton2_menu_barre.draw(fen, noir[0])

    if y_bouton1_menu_barre > 0:
        bouton1_menu_barre = Bouton(blanc[0], 800, -10 + y_barre + y_bouton1_menu_barre, 200, 50, list_menu_barre[0],
                                    30, police, noir[0])
        bouton1_menu_barre.draw(fen, noir[0])

    fen.blit(barre, (0, y_barre))

    if y_barre < 0:
        y_barre += 2


def draw_fond_jeu():
    a = src_img_fond_jeu
    load_img(a, (0, 0), fen)
    palier = 0
    for l in player.bots:
        palier += l.mult * l.val_argent
    if palier <= 10:
        a = 0
    elif palier > 10 and palier < 30:
        a = src_img_decor_bidon
        load_img(a, (500, 350), fen)

    elif palier < 100:
        a = src_img_decor_bidon
        load_img(a, (460, 335), fen)
        load_img(a, (540, 340), fen)

    elif palier < 300:
        a = src_img_decor_bidon
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
    elif palier < 1000:
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        a = src_img_decor_bidon
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
    elif palier < 5000:
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        a = src_img_decor_bidon
        load_img(a, (500, 350), fen)
    elif palier < 10000:
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
    elif palier < 15000:
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
        a = src_img_decor_egoux_rempli
        load_img(a, (123, 468), fen)
    elif palier < 20000:
        a = src_img_decor_cuve_vide
        load_img(a, (470, 150), fen)
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
        a = src_img_decor_egoux_rempli
        load_img(a, (123, 468), fen)
    elif palier < 25000:
        a = src_img_decor_cuve_rempli1
        load_img(a, (470, 150), fen)
        a = src_img_decor_cuve_vide
        load_img(a, (470, 150), fen)
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
        a = src_img_decor_egoux_rempli
        load_img(a, (123, 468), fen)
    elif palier < 30000:
        a = src_img_decor_cuve_rempli2
        load_img(a, (470, 150), fen)
        a = src_img_decor_cuve_vide
        load_img(a, (470, 150), fen)
        a = src_img_decor_bidon_ouvert
        load_img(a, (535, 327), fen)
        load_img(a, (465, 332), fen)
        load_img(a, (500, 350), fen)
        a = src_img_decor_egoux_rempli
        load_img(a, (123, 468), fen)


def draw_fen_shop():
    global alpha_fond_shop, bouton1_menu_barre_shop, bouton2_menu_barre_shop, bouton3_menu_barre_shop, bouton4_menu_barre_shop, x_barre_shop, bouton1_rubrique_materiaux, bouton2_rubrique_materiaux, bouton3_rubrique_materiaux, bouton4_rubrique_materiaux, bouton1_rubrique_tirage, bouton2_rubrique_tirage, bouton3_rubrique_tirage
    barre_shop = pygame.Surface((200, TAILLE_FEN[1]))
    barre_shop.fill(blanc[0])

    fond_shop = pygame.Surface(TAILLE_FEN)
    fond_shop.set_alpha(alpha_fond_shop)

    pygame.draw.rect(barre_shop, noir[0], (0, 0, 200, 40))

    bouton1_menu_barre_shop = Bouton(blanc[0], 0, 40, 200, 50, "materiaux", 30, police, noir[0])
    bouton1_menu_barre_shop.draw(barre_shop, noir[0])

    bouton2_menu_barre_shop = Bouton(blanc[0], 0, 90, 200, 50, "outil", 30, police, noir[0])
    bouton2_menu_barre_shop.draw(barre_shop, noir[0])

    bouton3_menu_barre_shop = Bouton(blanc[0], 0, 140, 200, 50, "ouvrier", 30, police, noir[0])
    bouton3_menu_barre_shop.draw(barre_shop, noir[0])

    bouton4_menu_barre_shop = Bouton(blanc[0], 0, 190, 200, 50, "tirage", 30, police, noir[0])
    bouton4_menu_barre_shop.draw(barre_shop, noir[0])

    if nom_rubrique_shop == "materiaux":
        ft = pygame.font.Font(police, 20)

        bouton1_rubrique_materiaux = Bouton(blanc[0], 266, 76, 301, 140, "", 30, police, noir[0],
                                            image=src_img_piece_to_uranium)
        bouton1_rubrique_materiaux.draw(fond_shop, noir[0])
        text = ft.render('10000', 1, noir[0])
        fond_shop.blit(text, (295, 182))
        text = ft.render('1000', 1, noir[0])
        fond_shop.blit(text, (485, 182))

        bouton2_rubrique_materiaux = Bouton(blanc[0], 633, 76, 301, 140, "", 30, police, noir[0],
                                            image=src_img_uranium_to_piece)
        bouton2_rubrique_materiaux.draw(fond_shop, noir[0])
        text = ft.render('1000', 1, noir[0])
        fond_shop.blit(text, (661, 182))
        text = ft.render('5000', 1, noir[0])
        fond_shop.blit(text, (842, 182))

        bouton3_rubrique_materiaux = Bouton(blanc[0], 266, 251, 301, 140, "", 30, police, noir[0],
                                            image=src_img_piece_to_uranium)
        bouton3_rubrique_materiaux.draw(fond_shop, noir[0])
        text = ft.render('10000k', 1, noir[0])
        fond_shop.blit(text, (295, 357))
        text = ft.render('1000k', 1, noir[0])
        fond_shop.blit(text, (485, 357))

        bouton4_rubrique_materiaux = Bouton(blanc[0], 633, 251, 301, 140, "", 30, police, noir[0],
                                            image=src_img_uranium_to_piece)
        bouton4_rubrique_materiaux.draw(fond_shop, noir[0])
        text = ft.render('1000k', 1, noir[0])
        fond_shop.blit(text, (661, 357))
        text = ft.render('5000k', 1, noir[0])
        fond_shop.blit(text, (842, 357))

    elif nom_rubrique_shop == "tirage":
        bouton1_rubrique_tirage = Bouton(blanc[0], 266, 76, 668, 140, "", 30, police, noir[0])
        bouton1_rubrique_tirage.draw(fond_shop, blanc[0])

        pygame.draw.rect(fond_shop, bleu[0], (294, 94, 79, 79))
        load_img(src_img_monstre13, (296, 96), fond_shop)

        ft = pygame.font.Font(police, 20)
        text = ft.render('Mamoutagion', 1, noir[0])
        fond_shop.blit(text, (275, 182))

        ft = pygame.font.Font(police, 50)
        text = ft.render('Tirage de Hiroshima', 1, noir[0])
        fond_shop.blit(text, (391, 86))

        ft = pygame.font.Font(police, 15)
        text = ft.render('Achetez ce pack de monstres basique pour seulement 50 000 uranium.', 1, noir[0])
        fond_shop.blit(text, (411, 136))
        text = ft.render('Plongez un animal dans des cuves duranium pour le faire muter ', 1, noir[0])
        fond_shop.blit(text, (411, 156))
        text = ft.render('et esperez obtenir un monstre surpuissant !', 1, noir[0])
        fond_shop.blit(text, (411, 176))

        bouton2_rubrique_tirage = Bouton(blanc[0], 266, 251, 668, 140, "", 30, police, noir[0])
        bouton2_rubrique_tirage.draw(fond_shop, blanc[0])

        pygame.draw.rect(fond_shop, violet[0], (294, 269, 79, 79))
        load_img(src_img_monstre17, (296, 271), fond_shop)

        ft = pygame.font.Font(police, 20)
        text = ft.render('Fantocyclus', 1, noir[0])
        fond_shop.blit(text, (275, 357))

        ft = pygame.font.Font(police, 50)
        text = ft.render('Tirage de Fukushima', 1, noir[0])
        fond_shop.blit(text, (391, 261))

        ft = pygame.font.Font(police, 15)
        text = ft.render('Achetez ce pack de monstres expert pour seulement 500 000 uranium.', 1, noir[0])
        fond_shop.blit(text, (411, 311))
        text = ft.render('Plongez 5 animaux dans des cuves duranium pour les faire muter ', 1, noir[0])
        fond_shop.blit(text, (411, 331))
        text = ft.render('et esperez obtenir des monstres surpuissants !', 1, noir[0])
        fond_shop.blit(text, (411, 351))

        bouton3_rubrique_tirage = Bouton(blanc[0], 266, 426, 668, 140, "", 30, police, noir[0])
        bouton3_rubrique_tirage.draw(fond_shop, blanc[0])

        pygame.draw.rect(fond_shop, jaune[0], (294, 444, 79, 79))
        load_img(src_img_monstre23, (296, 446), fond_shop)

        ft = pygame.font.Font(police, 20)
        text = ft.render('quarancuve', 1, noir[0])
        fond_shop.blit(text, (275, 532))

        ft = pygame.font.Font(police, 50)
        text = ft.render('Tirage de Tchernobyl', 1, noir[0])
        fond_shop.blit(text, (391, 436))

        ft = pygame.font.Font(police, 15)
        text = ft.render('Achetez ce pack de monstres legendaire pour seulement 50 000 000', 1, noir[0])
        fond_shop.blit(text, (411, 486))
        text = ft.render('uraniums. Plongez 10 animaux dans des cuves duranium pour les faire', 1, noir[0])
        fond_shop.blit(text, (411, 506))
        text = ft.render('muter et esperez obtenir des monstres surpuissants !', 1, noir[0])
        fond_shop.blit(text, (411, 526))

    elif nom_rubrique_shop == "ouvrier":
        pygame.draw.rect(fond_shop, (255, 255, 255), (266, 76, 301, 140))
        pygame.draw.rect(fond_shop, (255, 255, 255), (633, 76, 301, 140))
        pygame.draw.rect(fond_shop, (255, 255, 255), (266, 251, 301, 140))
        pygame.draw.rect(fond_shop, (255, 255, 255), (633, 251, 301, 140))

        font = pygame.font.Font(police, 20)
        for index, bouton in enumerate(boutons_rubrique_ouvier):
            bouton.draw(fond_shop, noir[0])
            text = font.render(str(player.bots[index // 2].prices[index % 2]), 1, noir[0])
            pos = bouton.x + (bouton.width - text.get_width()) // 2 + 3, bouton.y + bouton.height // 2 + (
                        35 - text.get_height()) // 2
            piece = pygame.image.load(src_img_piece)
            fond_shop.blit(piece, (pos[0] + text.get_width(), pos[1] - 5))
            fond_shop.blit(text, pos)
            if not index % 2:
                text = font.render(name_bots[index // 2] + ' x' + str(player.bots[index // 2].mult), 1, noir[0])
                pos = bouton.x + bouton.width - text.get_width() // 2, bouton.y - bouton.height // 2 - (
                            35 - text.get_height()) // 2
                fond_shop.blit(text, pos)
            txt = 'Plus de bots' if not index % 2 else 'Moins de temps'
            text = font.render(txt, 1, noir[0])
            pos = bouton.x + (bouton.width - text.get_width()) // 2 + 3, bouton.y + (35 - text.get_height()) // 2
            fond_shop.blit(text, pos)

    elif nom_rubrique_shop == 'outil':
        font = pygame.font.Font(police, 20)
        prices = str(3 ** (player.val_argent + 1)), str(10 * 3 ** (player.val_argent + 1))
        for index, bouton in enumerate(boutons_rubrique_outil):
            bouton.draw(fond_shop, noir[0])
            text = font.render(prices[index], 1, noir[0])
            pos = bouton.x + (bouton.width - text.get_width()) // 2, bouton.y + bouton.height // 2 + 20
            fond_shop.blit(text, pos)
            piece = pygame.image.load(src_img_piece)
            fond_shop.blit(piece, (pos[0] + text.get_width(), pos[1] - 5))

    fen.blit(fond_shop, (0, 0))
    fen.blit(barre_shop, (x_barre_shop, 0))

    if alpha_fond_shop < 255:
        alpha_fond_shop += 10

    if x_barre_shop < 0:
        x_barre_shop += 10


def draw_fen():
    global musique_load, musique_act
    if nom_fen == "intro":
        draw_intro()
    else:
        if nom_fen != "tirage":
            if musique_act != musique1:
                musique_act = musique1
                pygame.mixer.music.fadeout(1000)
                musique_load = False
        else:
            if musique_act != musique2:
                musique_act = musique2
                pygame.mixer.music.fadeout(1000)
                musique_load = False
        if musique == "on" and musique_load == False:
            pygame.mixer.music.load(musique_act)
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(loops=-1)
            musique_load = True
        elif musique == "off":
            pygame.mixer.music.fadeout(1000)
            musique_load = False
    if nom_fen == "menu":
        draw_menu()
    if nom_fen == "jouer":
        draw_fond_jeu()
        player.show(fen)
    if nom_fen == "shop":
        draw_fen_shop()
        player.show(fen, plus=False)
    if nom_fen == "jouer" or nom_fen == "shop":
        draw_barre()
    if nom_fen == "credits":
        draw_credits()
    if nom_fen == "collection":
        draw_collection()


def tirage():
    global tirage_img, tirages_restants, tirage_rarete
    tirages_restants -= 1
    rdm = random.random()
    if rdm <= 0.01 and tirage_type == 3:
        rarete = [i for i in range(21, 24)]
    elif 0.01 < rdm <= 0.11 and tirage_type >= 2:
        rarete = [i for i in range(16, 21)]
    elif 0.11 < rdm <= 0.41 and tirage_type >= 1:
        rarete = [i for i in range(8, 16)]
    else:
        rarete = [i for i in range(8)]
    choix = random.choice(rarete)
    if rarete[0] == 0:
        tirage_rarete = vert[0]
    elif rarete[0] == 8:
        tirage_rarete = bleu[0]
    elif rarete[0] == 16:
        tirage_rarete = violet[0]
    else:
        tirage_rarete = jaune[0]

    if rarete[0] == 0:
        if lock[choix]:
            player.uranium += 10000000
        else:
            player.mult += 100
    elif rarete[0] == 8:
        if lock[choix]:
            player.uranium += 50000
        else:
            player.mult += 50
    elif rarete[0] == 16:
        if lock[choix]:
            player.argent += 25000
        else:
            player.mult += 20
    else:
        if lock[choix]:
            player.uranium += 10000
        else:
            player.mult += 5
    lock[choix] = False
    img = f"resources/picture/monstre/monstre{choix + 1}.png"
    tirage_img = pygame.image.load(img).convert()


"""initialisatation"""
nom_fen = "intro"
with open('resources/save/player', 'rb') as fichier:
    a = pickle.Unpickler(fichier)
    sauvegarde = a.load()

musique_load = False
musique_act = musique1

player = Player()
player.argent = sauvegarde['argent']
player.uranium = sauvegarde['uranium']
player.bots = sauvegarde['bots']
player.val_argent = sauvegarde['val_argent']
player.val_uranium = sauvegarde['val_uranium']
player.mult = sauvegarde['mult']

boutons_rubrique_ouvier = [
    Bouton(blanc[0], 266, 146, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 416, 146, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 633, 146, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 783, 146, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 266, 321, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 416, 321, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 633, 321, 150, 70, "", 20, police, noir[0]),
    Bouton(blanc[0], 783, 321, 150, 70, "", 20, police, noir[0])
]

boutons_rubrique_outil = [
    Bouton(blanc[0], 266, 76, 301, 140, "Plus d'argent", 30, police, noir[0]),
    Bouton(blanc[0], 633, 76, 301, 140, "Plus d'uranium", 30, police, noir[0])
]

with open('resources/save/lock.txt', 'r') as fichier:
    contenu = fichier.readlines()

lock = []
num_lock = 0
for mmm in contenu:
    lock += [bool(int((contenu[num_lock])[:-1]))]
    num_lock += 1

tirage_reveal = False
tirages_restants = 0
tirage_img = None
tirage_rarete = None
tirage_alpha = 0
tirage_taille = 0
tirage_angle = 0
tirage_type = 0

src = open_txt(src_save_init)
son = (src[0])[:-1]
musique = (src[1])[:-1]

init_intro()

pygame.init()
pygame.display.set_caption("Monster Clicker")
icon_insertion = pygame.image.load(icon)
pygame.display.set_icon(icon_insertion)
environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)

fen = pygame.display.set_mode(TAILLE_FEN)
clock = pygame.time.Clock()

pygame.key.set_repeat(400, 30)

lock_render = pygame.image.load(src_img_monstre_lock).convert()
lock_render = pygame.transform.scale(lock_render, (400, 400))

continuer = True

"""la boucle principale"""
while continuer:

    clock.tick(fps)

    for event in pygame.event.get():

        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            continuer = False
            break

        if son == "on" and event.type == MOUSEBUTTONUP and nom_fen != "intro":
            if nom_fen == "tirage":
                play_son(swoosh)
            else:
                play_son(click)

        if nom_fen == 'tirage':
            if event.type == MOUSEBUTTONUP:
                if tirages_restants == 0 and tirage_reveal:
                    nom_fen = 'shop'
                    continue
                tirage_reveal = not tirage_reveal
                tirage_alpha, tirage_taille, tirage_angle = 1, 1, 1
                if not tirage_reveal: tirage()

        if nom_fen == "shop":
            if event.type == MOUSEBUTTONUP:
                if nom_rubrique_shop == "materiaux":
                    if player.argent > 9999:
                        if bouton1_rubrique_materiaux.isOver(event.pos):
                            player.argent -= 10000
                            player.uranium += 1000

                    if player.uranium > 999:
                        if bouton2_rubrique_materiaux.isOver(event.pos):
                            player.uranium -= 1000
                            player.argent += 5000

                    if player.argent > 9999999:
                        if bouton3_rubrique_materiaux.isOver(event.pos):
                            player.argent -= 10000000
                            player.uranium += 1000000

                    if player.uranium > 999999:
                        if bouton4_rubrique_materiaux.isOver(event.pos):
                            player.uranium -= 1000000
                            player.argent += 5000000

                elif nom_rubrique_shop == "ouvrier":
                    for index, bouton in enumerate(boutons_rubrique_ouvier):
                        if bouton.isOver(event.pos):
                            price = player.bots[index // 2].prices[index % 2]
                            if player.argent >= price:
                                player.argent -= price
                                player.changeBot(index // 2, index % 2)

                elif nom_rubrique_shop == 'outil':
                    for index, bouton in enumerate(boutons_rubrique_outil):
                        if bouton.isOver(event.pos):
                            if index == 0:
                                if player.argent >= 3 ** (player.val_argent + 1):
                                    player.argent -= 3 ** (player.val_argent + 1)
                                    player.val_argent += 1
                            elif index == 1:
                                if player.argent >= 10 * 3 ** (player.val_argent + 1):
                                    player.argent -= 10 * 3 ** (player.val_argent + 1)
                                    player.val_uranium += 1

                elif nom_rubrique_shop == 'tirage' and y_bouton1_menu_barre == 0:
                    if bouton1_rubrique_tirage.isOver(event.pos) and player.uranium >= 10000:
                        player.uranium -= 10000
                        nom_fen = 'tirage'
                        tirage_reveal = False
                        tirages_restants = 1
                        tirage_type = 1
                        tirage()
                        continue
                    elif bouton2_rubrique_tirage.isOver(event.pos) and player.uranium >= 250000:
                        player.uranium -= 250000
                        nom_fen = 'tirage'
                        tirages_restants = 5
                        tirage_reveal = False
                        tirage_type = 2
                        tirage()
                        continue
                    elif bouton3_rubrique_tirage.isOver(event.pos) and player.uranium >= 1000000:
                        player.uranium -= 1000000
                        nom_fen = 'tirage'
                        tirage_reveal = False
                        tirages_restants = 10
                        tirage_type = 3
                        tirage()
                        continue

        if nom_fen == "menu" and pause_intro >= 100:
            if event.type == MOUSEBUTTONUP:

                if rectangle3.isOver(event.pos):
                    nom_fen = "jouer"
                    init_barre()
                    init_clique_menu()
                    draw_barre()

                if rectangle.isOver(event.pos):
                    nom_fen = "collection"
                    draw_collection()

                if rectangle2.isOver(event.pos):
                    nom_fen = "shop"
                    init_shop()
                    init_barre()
                    init_clique_menu()
                    draw_barre()

                if rectangle5.isOver(event.pos):
                    if son == "on":
                        son = "off"
                    else:
                        son = "on"

                if rectangle6.isOver(event.pos):
                    if musique == "on":
                        musique = "off"
                    else:
                        musique = "on"

                if rectangle4.isOver(event.pos):
                    nom_fen = "credits"
                    draw_credits()


        elif nom_fen == "jouer":
            if event.type == MOUSEBUTTONUP and y_bouton1_menu_barre == 0 and event.button != 4 and event.button != 5:
                player.click(fen, event.pos, y_barre)

        elif nom_fen == "shop":
            if event.type == MOUSEBUTTONUP:
                if bouton1_menu_barre_shop.isOver(event.pos):
                    nom_rubrique_shop = "materiaux"
                elif bouton2_menu_barre_shop.isOver(event.pos):
                    nom_rubrique_shop = "outil"
                elif bouton3_menu_barre_shop.isOver(event.pos):
                    nom_rubrique_shop = "ouvrier"
                elif bouton4_menu_barre_shop.isOver(event.pos):
                    nom_rubrique_shop = "tirage"

        if nom_fen == "jouer" or nom_fen == "shop":
            if menu_barre == True and event.type == MOUSEBUTTONUP and event.pos[1] > 40:
                if event.pos[1] <= 190 and event.pos[0] < 800:
                    menu_barre = False
                if event.pos[1] > 190:
                    menu_barre = False
            if x_son == 40:
                if event.type == MOUSEBUTTONUP and event.pos[0] >= pos_son_j[0] and event.pos[0] <= pos_son_j[
                    0] + 40 and event.pos[1] >= pos_son_j[1] and event.pos[1] <= pos_son_j[1] + 40:
                    if son == "on":
                        son = "off"
                    else:
                        son = "on"
            if x_musique == 40:
                if event.type == MOUSEBUTTONUP and event.pos[0] >= pos_musique_j[0] and event.pos[0] <= pos_musique_j[
                    0] + 60 and event.pos[1] >= pos_musique_j[1] and event.pos[1] <= pos_musique_j[1] + 40:
                    if musique == "on":
                        musique = "off"
                    else:
                        musique = "on"
            if y_bouton1_menu_barre == 50:
                if event.type == MOUSEBUTTONUP:
                    if bouton1_menu_barre.isOver(event.pos):
                        nom_fen = "menu"
                        x_menu = 0
                        y_menu = 0
            if y_bouton2_menu_barre == 50:
                if event.type == MOUSEBUTTONUP:
                    if bouton2_menu_barre.isOver(event.pos):
                        if list_menu_barre[1] == "jouer":
                            nom_fen = "jouer"
                        if list_menu_barre[1] == "shop":
                            nom_fen = "shop"
                            init_shop()
                        init_barre()
            if y_bouton3_menu_barre == 50:
                if event.type == MOUSEBUTTONUP:
                    if bouton3_menu_barre.isOver(event.pos):
                        nom_fen = "collection"

            if event.type == MOUSEBUTTONUP and event.pos[0] >= pos_engrenage[0] and event.pos[0] <= pos_engrenage[
                0] + 40 and event.pos[1] >= pos_engrenage[1] and event.pos[1] <= pos_engrenage[1] + 40:
                if option_barre == True:
                    option_barre = False
                else:
                    option_barre = True

            if event.type == MOUSEBUTTONUP and event.pos[0] >= pos_menu_barre[0] and event.pos[0] <= pos_menu_barre[
                0] + 60 and event.pos[1] >= pos_menu_barre[1] and event.pos[1] <= pos_menu_barre[1] + 40:
                if menu_barre == True:
                    menu_barre = False
                else:
                    menu_barre = True

        elif nom_fen == "credits":
            if event.type == MOUSEBUTTONUP:

                if rectangle8.isOver(event.pos):
                    x_menu = 0
                    y_menu = 0
                    nom_fen = "menu"

        elif nom_fen == "collection":
            if event.type == MOUSEBUTTONUP:
                if rectangle8.isOver(event.pos):
                    nom_fen = "menu"
                    x_menu = 0
                    y_menu = 0
    fen.fill(noir[0])
    draw_fen()
    if nom_fen == 'tirage':
        tirage_alpha += 5
        tirage_taille += 10
        tirage_angle += 10
        tirage_alpha = min(tirage_alpha, 255)
        tirage_taille = min(tirage_taille, 400)
        tirage_angle = min(tirage_angle, 360)
        if tirage_reveal:
            if tirage_taille < 400:
                img = pygame.transform.rotozoom(tirage_img, tirage_angle, tirage_taille / 75)
            else:
                img = pygame.transform.scale(tirage_img, (tirage_taille, tirage_taille))
            img.set_alpha(tirage_alpha)
            fen.blit(img, (500 - img.get_width() // 2, 300 - img.get_width() // 2))
        else:
            lock_render.set_alpha(tirage_alpha)
            fen.blit(lock_render, (300, 100))
            pygame.draw.rect(fen, tirage_rarete, (300, 100, lock_render.get_width(), lock_render.get_height()), 5)

    pygame.display.update()

pygame.quit()
save()
