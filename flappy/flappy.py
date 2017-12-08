pontoMaximo = 0
vida = 3
melhor_pontuacao_atual = 0

def menu(pontoMaximo, vida, melhor_pontuacao_atual):
    import sys, pygame, os, random

    #Inicia o pygame
    pygame.init()

    #Define o tamanho da tela
    size = (288, 512)
    screen = pygame.display.set_mode(size)

    #Define o título da janela
    pygame.display.set_caption("Flappy Bird")

    folder = "imagens"

    branco = [255, 255, 255]

    fonte2 = pygame.font.SysFont("LITHOGRAPH", 40)
    fonteBotao = pygame.font.SysFont("LITHOGRAPH", 25)
    texto2 = fonte2.render(("Flappy Bird"), True, branco)
    play = fonteBotao.render("Jogar", True, branco)
    instrucao = fonteBotao.render("Instruções", True, branco)

    cenarios = ("background-day.png", "background-night.png")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

    som = {}
    som["despause"] = pygame.mixer.Sound('audio/swoosh.wav')

    while True:
        screen.blit(cenario, (0, 0))
        screen.blit(instrucao, [160, 380])
        screen.blit(play, [50, 380])

        screen.blit(texto2, [70, 75])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x > 150 and x < 550 and y > 380 and y < 400):
                    som["despause"].play()
                    como_jogar(pontoMaximo, vida, melhor_pontuacao_atual)
                if (x > 10 and x < 100 and y > 380 and y < 400):
                    som["despause"].play()
                    jogar(pontoMaximo, vida, melhor_pontuacao_atual)

        pygame.display.flip()


def jogar(pontoMaximo, vida, melhor_pontuacao_atual):
    import sys, pygame, os, random

    # Inicia o pygame
    pygame.init()

    # Define o tamanho da tela
    size = (288, 512)
    screen = pygame.display.set_mode(size)

    # Define o título da janela
    pygame.display.set_caption("Flappy Bird")

    # Define a pasta com todas as imagens
    folder = "imagens"

    # Inicializa o cenário
    cenarios = ("background-day.png", "background-night.png")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))
    x_cenario = 0

    # Define a cor dos canos
    cor = ("green", "red")
    cor_random = random.randint(0, len(cor) - 1)
    cor_cano = cor[cor_random]
    if (cor_cano == "green"):
        cano_up = pygame.image.load(os.path.join(folder, "pipe-green-up.png"))
        cano_down = pygame.image.load(os.path.join(folder, "pipe-green-down.png"))
    else:
        cano_up = pygame.image.load(os.path.join(folder, "pipe-red-up.png"))
        cano_down = pygame.image.load(os.path.join(folder, "pipe-red-down.png"))

    # Define a posição dos canos
    x_cano_up1 = 240
    y_cano_up1 = random.randint(150, 450)
    x_cano_down1 = 240
    y_cano_down1 = y_cano_up1 - 620
    x_cano_up2 = 480
    y_cano_up2 = random.randint(150, 450)
    x_cano_down2 = 480
    y_cano_down2 = y_cano_up2 - 620

    # Define a cor do passaro
    cor_passaro = random.randint(0, 2)
    if (cor_passaro == 0):
        passaro_descendo = pygame.image.load(os.path.join(folder, "bluebird-upflap.png"))
        passaro_subindo = pygame.image.load(os.path.join(folder, "bluebird-downflap.png"))
    else:
        passaro_descendo = pygame.image.load(os.path.join(folder, "redbird-upflap.png"))
        passaro_subindo = pygame.image.load(os.path.join(folder, "redbird-downflap.png"))

    passaro = pygame.image.load(os.path.join(folder, "redbird-midflap.png"))

    # Define a posição do passaro
    x_passaro = 100
    y_passaro = 250

    # Define a gravidade
    gravidade = 1.5
    gravidade_invertida = 2

    # Define o fps
    fps = 120

    clock = pygame.time.Clock()

    start_ticks = pygame.time.get_ticks()

    fonte = pygame.font.SysFont("LITHOGRAPH", 25)

    pontos = 0

    dificuldade = 1

    branco = [255, 255, 255]

    som = {}
    som["ponto"] = pygame.mixer.Sound('audio/point.wav')
    som["morte"] = pygame.mixer.Sound('audio/die.wav')
    som["despause"] = pygame.mixer.Sound('audio/swoosh.wav')

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    fps+=5
                if event.key == pygame.K_DOWN:
                    fps-=5
                    if (fps<120):
                        fps = 120

        segundos = str(int((pygame.time.get_ticks()-start_ticks)/1000))

        rel_x_cenario = x_cenario % cenario.get_rect().width
        screen.blit(cenario, (rel_x_cenario - cenario.get_rect().width, 0))
        if (rel_x_cenario < 288):
            screen.blit(cenario, (rel_x_cenario, 0))
        x_cenario -= dificuldade

        screen.blit(cano_up, (x_cano_up1, y_cano_up1))
        screen.blit(cano_down, (x_cano_down1, y_cano_down1))
        x_cano_up1 -= dificuldade
        x_cano_down1 -= dificuldade

        screen.blit(cano_up, (x_cano_up2, y_cano_up2))
        screen.blit(cano_down, (x_cano_down2, y_cano_down2))
        x_cano_up2 -= dificuldade
        x_cano_down2 -= dificuldade

        # SURGIMENTO DOS CANOS
        if (x_cano_up1 < -50):
            x_cano_up1 = 430
            y_cano_up1 = random.randint(150, 450)
            x_cano_down1 = 430
            y_cano_down1 = y_cano_up1 - 620

        if (x_cano_up2 < -50):
            x_cano_up2 = 430
            y_cano_up2 = random.randint(150, 450)
            x_cano_down2 = 430
            y_cano_down2 = y_cano_up2 - 620

        # PONTUAÇÃO
        pontoAtual = str(pontos)
        msg_ponto_atual = fonte.render(("Pontuação atual: " + str(pontoAtual)), True, branco)
        record = fonte.render(("Record: " + str(pontoMaximo)), True, branco)
        screen.blit(msg_ponto_atual, (20, 80))
        screen.blit(record, (20, 50))

        life = fonte.render(("Vida: " + str(vida)), True, branco)
        screen.blit(life, (20, 20))

        if (melhor_pontuacao_atual < pontos):
            melhor_pontuacao_atual = pontos

        msg_melhor_pontuacao_atual = fonte.render(("Melhor pontuação atual: " + str(melhor_pontuacao_atual)), True, branco)
        screen.blit(msg_melhor_pontuacao_atual, (20, 110))


        msg_segundos = fonte.render(("Tempo: " + segundos), True, branco)
        screen.blit(msg_segundos, (100, 20))

        if (x_cano_down1 == x_passaro):
            pontos += 1
            som["ponto"].play()
        if (x_cano_down2 == x_passaro):
            pontos += 1
            som["ponto"].play()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE]:
            screen.blit(passaro_subindo, (x_passaro, y_passaro))
            y_passaro -= gravidade_invertida
        else:
            y_passaro += gravidade
            screen.blit(passaro_descendo, (x_passaro, y_passaro))

        


        cano_up1_colisao = cano_up.get_rect()
        cano_up1_colisao.left, cano_up1_colisao.top = (x_cano_up1), (y_cano_up1)

        cano_up2_colisao = cano_up.get_rect()
        cano_up2_colisao.left, cano_up2_colisao.top = (x_cano_up2), (y_cano_up2)

        cano_down1_colisao = cano_down.get_rect()
        cano_down1_colisao.left, cano_down1_colisao.top = (x_cano_down1), (y_cano_down1)

        cano_down2_colisao = cano_down.get_rect()
        cano_down2_colisao.left, cano_down2_colisao.top = (x_cano_down2), (y_cano_down2)

        passaro_colisao = passaro.get_rect()
        passaro_colisao.left, passaro_colisao.top = (x_passaro), (y_passaro)

        if (passaro_colisao.colliderect(cano_up1_colisao)):
            som["morte"].play()
            vida -= 1
            if (vida == 0):
                if (melhor_pontuacao_atual > pontoMaximo):
                    pontoMaximo = melhor_pontuacao_atual
                fim_de_jogo(pontos, pontoMaximo, vida, melhor_pontuacao_atual)
            else:
                esperar(pontoMaximo, vida, melhor_pontuacao_atual)

        if (passaro_colisao.colliderect(cano_up2_colisao)):
            som["morte"].play()
            vida -= 1
            if (vida == 0):
                if (melhor_pontuacao_atual > pontoMaximo):
                    pontoMaximo = melhor_pontuacao_atual
                fim_de_jogo(pontos, pontoMaximo, vida, melhor_pontuacao_atual)
            else:
                esperar(pontoMaximo, vida, melhor_pontuacao_atual)

        if (passaro_colisao.colliderect(cano_down1_colisao)):
            som["morte"].play()
            vida -= 1
            if (vida == 0):
                if (melhor_pontuacao_atual > pontoMaximo):
                    pontoMaximo = melhor_pontuacao_atual
                fim_de_jogo(pontos, pontoMaximo, vida, melhor_pontuacao_atual)
            else:
                esperar(pontoMaximo, vida, melhor_pontuacao_atual)

        if (passaro_colisao.colliderect(cano_down2_colisao)):
            som["morte"].play()
            vida -= 1
            if (vida == 0):
                if (melhor_pontuacao_atual > pontoMaximo):
                    pontoMaximo = melhor_pontuacao_atual
                fim_de_jogo(pontos, pontoMaximo, vida, melhor_pontuacao_atual)
            else:
                esperar(pontoMaximo, vida, melhor_pontuacao_atual)

        pygame.display.update()
        clock.tick(fps)

def como_jogar(pontoMaximo, vida, melhor_pontuacao_atual):
    import sys, pygame, os, random

    # Inicia o pygame
    pygame.init()

    # Define o tamanho da tela
    size = (288, 512)
    screen = pygame.display.set_mode(size)

    # Define o título da janela
    pygame.display.set_caption("Flappy Bird")

    folder = "imagens"

    cenarios = ("background-day.png", "background-night.png")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

    branco = [255, 255, 255]

    fonte_menor = pygame.font.SysFont("LITHOGRAPH", 23)
    titulo = pygame.font.SysFont("LITHOGRAPH", 50)
    fonte_botao = pygame.font.SysFont("LITHOGRAPH", 25)

    msg_titulo = titulo.render(("Como jogar:"), True, branco)
    texto = fonte_menor.render(("Guie o pássaro sem tocar nos canos"), True, branco)
    texto2 = fonte_menor.render(("Utilize o espaço para faze-lo voar"), True, branco)

    play = fonte_botao.render("Jogar", True, branco)
    voltar = fonte_botao.render("Voltar", True, branco)

    msg_dificuldade1 = fonte_menor.render(("Utilize as setas para mudar a"), True, branco)
    msg_dificuldade2 = fonte_menor.render(("dificuldade. Cima = mais rápido,"), True, branco)
    msg_dificuldade3 = fonte_menor.render(("Baixo = mais lento"), True, branco)

    som = {}
    som["despause"] = pygame.mixer.Sound('audio/swoosh.wav')

    while True:

        screen.blit(cenario, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x > 10 and x < 100) and (y > 380 and y < 400):
                    som["despause"].play()
                    jogar(pontoMaximo, vida, melhor_pontuacao_atual)

                if (x > 150 and x < 210) and (y > 380 and y < 400):
                    som["despause"].play()
                    menu(pontoMaximo, vida, melhor_pontuacao_atual)



        screen.blit(msg_titulo, [3, 3])
        screen.blit(texto, [3, 50])
        screen.blit(texto2, [3, 85])
        screen.blit(play, [50, 380])
        screen.blit(voltar, [160, 380])
        screen.blit(msg_dificuldade1, [3, 120])
        screen.blit(msg_dificuldade2, [3, 135])
        screen.blit(msg_dificuldade3, [3, 150])


        pygame.display.flip()


def fim_de_jogo(pontos, pontoMaximo, vida, melhor_pontuacao_atual):
    import sys, pygame, os, random

    # Inicia o pygame
    pygame.init()

    # Define o tamanho da tela
    size = (288, 512)
    screen = pygame.display.set_mode(size)

    # Define o título da janela
    pygame.display.set_caption("Flappy Bird")

    folder = "imagens"

    cenarios = ("background-day.png", "background-night.png")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

    branco = [255, 255, 255]

    fonte = pygame.font.SysFont("LITHOGRAPH", 50)
    texto = fonte.render("GAME OVER", True, branco)
    fonte_menor = pygame.font.SysFont("LITHOGRAPH", 23)
    fonte_botao = pygame.font.SysFont("LITHOGRAPH", 25)

    play = fonte_botao.render("Jogar", True, branco)
    voltar = fonte_botao.render("Voltar", True, branco)

    texto2 = fonte_menor.render(("Você fez " + str(melhor_pontuacao_atual) + " pontos"), True, branco)
    texto3 = fonte_menor.render(("O record é " + str(pontoMaximo) + " pontos"), True, branco)

    vida = 3
    melhor_pontuacao_atual = 0

    som = {}
    som["despause"] = pygame.mixer.Sound('audio/swoosh.wav')

    while (True):
        screen.blit(cenario, (0, 0))
        screen.blit(play, [50, 380])
        screen.blit(voltar, [160, 380])
        screen.blit(texto2, [80, 210])
        screen.blit(texto3, [80, 260])
        screen.blit(texto, [40, 75])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x2 = pygame.mouse.get_pos()[0]
                y2 = pygame.mouse.get_pos()[1]
                if (x2 > 10 and x2 < 100 and y2 > 380 and y2 < 400):
                    som["despause"].play()
                    jogar(pontoMaximo, vida, melhor_pontuacao_atual)

                if (x2 > 150 and x2 < 210 and y2 > 380 and y2 < 400):
                    som["despause"].play()
                    menu(pontoMaximo, vida, melhor_pontuacao_atual)
        pygame.display.flip()

def esperar(pontoMaximo, vida, melhor_pontuacao_atual):
    import sys, pygame, os, random

    # Inicia o pygame
    pygame.init()

    # Define o tamanho da tela
    size = (288, 512)
    screen = pygame.display.set_mode(size)

    # Define o título da janela
    pygame.display.set_caption("Flappy Bird")

    folder = "imagens"

    cenarios = ("background-day.png", "background-night.png")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

    branco = [255, 255, 255]

    titulo = pygame.font.SysFont("LITHOGRAPH", 25)

    msg1 = titulo.render(("Você bateu!"), True, branco)
    msg2 = titulo.render(("Aperte enter para continuar"), True, branco)

    som = {}
    som["despause"] = pygame.mixer.Sound('audio/swoosh.wav')

    while (True):
        screen.blit(cenario, (0, 0))
        screen.blit(msg1, (20, 65))
        screen.blit(msg2, (20, 85))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    som["despause"].play()
                    jogar(pontoMaximo, vida, melhor_pontuacao_atual)

        pygame.display.flip()


menu(pontoMaximo, vida, melhor_pontuacao_atual)
