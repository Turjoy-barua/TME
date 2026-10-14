# Example file showing a circle moving on screen
import pygame
import demineur as d

size = 9


SCREEN_WIDTH = 920 # window width
SCREEN_HEIGHT = 920 # window height
MARGIN = 10 # margin around the board
BOARD = 900 
LIGHT_GRAY = (224,224,224)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
SIZE = 9
NB_MINES = 4
    

""" 
def drawCell(screen, value, status, x, y, tile_size):
    rect = pygame.Rect(x, y, tile_size - 2, tile_size - 2) 
    if status == d.Status.COVERED:
        pygame.draw.rect(screen, LIGHT_GRAY, rect)
    elif status == d.Status.UNCOVERED:
        pygame.draw.rect(screen, WHITE, rect)
        if value > 0 and value < 9:
            font = pygame.font.SysFont(None, 36)
            number = font.render(str(value), True, BLACK)
            screen.blit(number, (x + 40, y + 35))
    
    elif status == d.Status.MARK:
        pygame.draw.rect(screen, LIGHT_GRAY, rect)
        font = pygame.font.SysFont(None, 36)
        flag = font.render("F", True, (255, 0, 0))
        screen.blit(flag, (x + 40, y + 35))
    
def drawGrid(screen, game_board, status_board):
   tile_size = BOARD // len(game_board)
   
   for row in range(len(game_board)):
        for column in range(len(game_board)):
            x = MARGIN + column * tile_size
            y = MARGIN + row * tile_size
            drawCell(screen, game_board[row][column], status_board[row][column], x, y, tile_size)
"""
            
def dessiner_plateau(screen, board, statut):
    taille = len(board)
    tile_size = BOARD // taille

    font = pygame.font.SysFont(None, 36)

    for y in range(taille):
        for x in range(taille):
            px = MARGIN + x * tile_size
            py = MARGIN + y * tile_size

            etat = statut[y][x]
            valeur = board[y][x]

            if etat == d.Status.COVERED:
                pygame.draw.rect(screen, LIGHT_GRAY, [px, py, tile_size - 2, tile_size - 2])

            elif etat == d.Status.MARK:
                pygame.draw.rect(screen, (220, 50, 50), [px, py, tile_size - 2, tile_size - 2])
                texte = font.render("M", True, WHITE)
                screen.blit(texte, (px + 40, py + 35))

            elif etat == d.Status.UNCOVERED:
                pygame.draw.rect(
                    screen, WHITE,
                    [px, py, tile_size - 2, tile_size - 2])

                if valeur == 9:
                    texte = font.render("*", True, (220, 0, 0))
                    screen.blit(texte, (px + 40, py + 35))

                elif valeur > 0:
                    texte = font.render(
                        str(valeur), True, (0, 0, 200)
                    )
                screen.blit(texte, (px + 40, py + 35))


def win(board, statut):
    taille = len(board)

    for y in range(taille):
        for x in range(taille):
            if board[y][x] != 9:
                if statut[y][x] != d.Status.UNCOVERED:
                    return False

    return True


def afficher_message(screen, message, couleur):
    font = pygame.font.SysFont(None, 64)
    texte = font.render(message, True, couleur)

    fond = pygame.Surface((420, 100), pygame.SRCALPHA)
    fond.fill((255, 255, 255, 230))

    x = (SCREEN_WIDTH - fond.get_width()) // 2
    y = (SCREEN_HEIGHT - fond.get_height()) // 2

    screen.blit(fond, (x, y))
    screen.blit(texte,texte.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("DEMINEUR")
    clock = pygame.time.Clock()
    board = d.init_plateau_mine(SIZE, NB_MINES)
    statut = d.init_statut(SIZE)
    running = True
    perdu = False
    gagne = False

    tile_size = BOARD // SIZE

    while running:

        # 1. GESTION DES EVENEMENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and not perdu and not gagne :
                mouse_x, mouse_y = event.pos

                # Convertir les pixels en coordonnées
                # de case (x = colonne, y = ligne)
                x = (mouse_x - MARGIN) // tile_size
                y = (mouse_y - MARGIN) // tile_size

                # Vérifier que le clic est dans le plateau
                if MARGIN <= mouse_x < MARGIN + BOARD and MARGIN <= mouse_y < MARGIN + BOARD:
                    
                    # CLIC GAUCHE : DECOUVRIR
                    if event.button == 1:

                        if statut[y][x] != d.Status.MARK:
                            resultat = d.decouvrir_case( (x, y), board, statut )

                            if not resultat:
                                perdu = True

                                # Montrer tout le plateau
                                statut = d.init_statut( SIZE, d.Status.UNCOVERED )

                    # CLIC DROIT : MARQUER
                    elif event.button == 3:
                        if statut[y][x] != d.Status.UNCOVERED:
                            d.change_status( (x, y), statut )

                    # VERIFIER LA VICTOIRE
                    if not perdu and win(board, statut):
                        gagne = True


        # 2. EFFACER L'ECRAN
        screen.fill(BLACK)

        # 3. DESSINER LE PLATEAU
        dessiner_plateau(screen, board, statut)

        # 4. AFFICHER LE RESULTAT
        if perdu:
            afficher_message(
                screen, "GAME OVER", RED
            )

        elif gagne:
            afficher_message(
                screen, "YOU WIN!", GREEN
            )

        # 5. ACTUALISER L'ECRAN
        pygame.display.flip()

        # 6. LIMITER A 60 IMAGES PAR SECONDE
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
