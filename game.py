import pygame
import random

class Recs(object):
    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2, 560)
            toprandom = random.randrange(-580, -10)
            width = random.randrange(10, 30)
            height = random.randrange(15, 30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height))

            

    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0, 2)
                            

    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165,214,254),retangulo)

    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481:
                score = score + 1
                leftrandom = random.randrange(2, 560)
                toprandom = random.randrange(-580, -10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))
        
            

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100, 200)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)


def colisao(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False



def main():
    import pygame
    #Declaração das váriaveis (objetos)
    pygame.init()
    tela = pygame.display.set_mode((480, 300))
    sair = False
    relogio = pygame.time.Clock()

    img_nave = pygame.image.load("imagens/nave.png").convert_alpha()
    jogador = Player(img_nave)

    imagem_fundo = pygame.image.load("imagens/fundo.png").convert_alpha()
    imagem_explosao = pygame.image.load("imagens/explosao.png").convert_alpha()

    pygame.mixer.music.load("audios/musica.mp3")
    pygame.mixer.music.play(3)

    som_explosao = pygame.mixer.Sound("audios/explosao2.wav")
    som_mov = pygame.mixer.Sound("audios/som2.wav")

    vx, vy = 0,0
    velocidade = 10
    leftpress, rightpress, uppress, downpress = False, False, False, False

    texto = pygame.font.SysFont("Arial", 15, True, False)
    
    

    score = 0

    ret = Recs(30)
    colidiu = False

       

    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if colidiu == False:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftpress = True
                        vx = - velocidade

                    if event.key == pygame.K_RIGHT:
                        rightpress = True
                        vx = velocidade

                    if event.key == pygame.K_UP:
                        uppress = True
                        vy = - velocidade
                        som_mov.play()

                    if event.key == pygame.K_DOWN:
                        downpress = True
                        vy = velocidade

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftpress = False
                        if rightpress:vx = velocidade
                        else:vx = 0

                    if event.key == pygame.K_RIGHT:
                        rightpress = False
                        if leftpress:vx = -velocidade
                        else:vx = 0

                    if event.key == pygame.K_UP:
                        uppress = False
                        if downpress:vx = velocidade
                        vy = 0

                    if event.key == pygame.K_DOWN:
                        downpress = False
                        if uppress:vx = -velocidade
                        vy = 0


        if colisao(jogador, ret):
            
            colidiu = True
            jogador.imagem = imagem_explosao
            pygame.mixer.music.stop()
            som_explosao.play()
            
         

        if colidiu == False:
            ret.mover()
            jogador.mover(vx, vy)

            tela.blit(imagem_fundo,(0,0))
            segundos = pygame.time.get_ticks()/1000
            segundos = str(segundos)
            contador = texto.render("Pontuação:{}".format(segundos), 0, (255,255,255))
            tela.blit(contador, (320, 10))
                    

        relogio.tick(20)
        #tela.blit(imagem_fundo,(0,0))
        
        #ret.mover()
        ret.cor(tela)
        ret.recriar()
        jogador.update(tela)
        #jogador.mover(vx, vy)
        
        
        

        pygame.display.update()

    pygame.quit()

main()


                
                                    
