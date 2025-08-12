import pygame

def main():
    pygame.init()
    pygame.mixer.init()

    # Tela e relógio
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption("Jogo Iniciante")
    relogio = pygame.time.Clock()

    # Cores
    cor_branca = (255, 255, 255)
    cor_vermelha = (227, 57, 9)
    cor_preta = (0, 0, 0)

    # Superfície de fundo
    sup = pygame.Surface((600, 450))
    sup.fill(cor_preta)

    # Retângulo do jogador
    ret = pygame.Rect(10, 10, 30, 30)

    # Obstáculos
    obstaculos = [
        pygame.Rect(10, 70, 555, 6),
        pygame.Rect(10, 120, 350, 6),
        pygame.Rect(405, 120, 195, 6),
        pygame.Rect(45, 170, 555, 6),
        pygame.Rect(10, 220, 400, 6),
        pygame.Rect(455, 220, 145, 6),
        pygame.Rect(45, 270, 555, 6),
        pygame.Rect(10, 320, 545, 6)
    ]

    # Fontes
    pygame.font.init()
    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    # Áudio
    audio_explosao = pygame.mixer.Sound('explodir.ogg')
    audio_explosao.set_volume(0.5)

    # Estado do jogo
    perdeu = False
    ganhou = False
    sair = False

    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            elif event.type == pygame.MOUSEBUTTONDOWN and ganhou:
                # Reinicia o jogo
                ret.left, ret.top = 10, 10
                perdeu = False
                ganhou = False
                obstaculos = [
                    pygame.Rect(10, 70, 555, 6),
                    pygame.Rect(10, 120, 350, 6),
                    pygame.Rect(405, 120, 195, 6),
                    pygame.Rect(45, 170, 555, 6),
                    pygame.Rect(10, 220, 400, 6),
                    pygame.Rect(455, 220, 145, 6),
                    pygame.Rect(45, 270, 555, 6),
                    pygame.Rect(10, 320, 545, 6)
                ]

        relogio.tick(30)
        tela.fill(cor_branca)
        tela.blit(sup, [0, 0])

        # Movimento do jogador
        xant, yant = ret.left, ret.top
        ret.left, ret.top = pygame.mouse.get_pos()
        ret.left -= ret.width // 2
        ret.top -= ret.height // 2

        # Verifica colisão
        if not perdeu and any(ret.colliderect(obst) for obst in obstaculos):
            perdeu = True
            audio_explosao.play()
            ret.left, ret.top = xant, yant

        # Verifica vitória
        if not perdeu and ret.top > 330:
            ganhou = True
            obstaculos = []  # Remove obstáculos

        # Desenha jogador
        pygame.draw.rect(tela, cor_vermelha, ret)

        # Desenha obstáculos
        for obst in obstaculos:
            pygame.draw.rect(tela, cor_branca, obst)

        # Mensagens
        if perdeu:
            texto = fonte_perdeu.render('VOCÊ PERDEU', True, cor_branca)
            tela.blit(texto, texto.get_rect(center=(300, 200)))
        elif ganhou:
            texto1 = fonte_perdeu.render('VOCÊ GANHOU', True, cor_branca)
            texto2 = fonte_ganhou.render('Clique para recomeçar', True, cor_vermelha)
            tela.blit(texto1, texto1.get_rect(center=(300, 200)))
            tela.blit(texto2, texto2.get_rect(center=(300, 250)))

        pygame.display.update()

    pygame.quit()

main()
