import classes
from sys import exit
from random import randint
from loads import *

class RPG:
    def __init__(self, nome: str, x, y):
        pg.init()
        pg.display.init()
        self.nome = nome
        self.x, self.y = x, y

        pg.font.init()
        fonte = pg.font.get_default_font()
        self.fontePequena = pg.font.SysFont(fonte, 35)

        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(-1)

        self.vida_personagem = 10
        self.vida_inimigo = 10

        self.contadorEscolhaCassio, self.contadorEscolhaPietra = 0, 0
        self.contadorCassioParado, self.contadorPietraParada = 0, 0

        self.dano = 0
        self.dado = 0

    # ------------------------------------ Tela créditos ------------------------------------------------------------
    def tela_creditos(self):
        creditoLoop = True
        while creditoLoop:
            self.clock.tick(10)
            self.tela.fill((67, 54, 55))

            colisaoBtnVoltar = areaBtnVoltar.collidepoint(pg.mouse.get_pos())
            self.tela.blit(btnVoltar, (areaBtnVoltar.x, areaBtnVoltar.y))
            self.tela.blit(txtCreditos, (areaTxtCreditos.x, areaTxtCreditos.y))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                elif event.type == pg.MOUSEBUTTONDOWN and colisaoBtnVoltar:
                    creditoLoop = False

                elif pg.key.get_pressed()[pg.K_ESCAPE]:
                    creditoLoop = False

            pg.display.update()
            pg.display.flip()

    def tela_escolha_portas(self):
        self.tela.fill((0, 0, 0))

        grupo_sprites = pg.sprite.Group()
        porta1 = classes.Porta(150, 300)
        porta2 = classes.Porta(450, 300)
        grupo_sprites.add(porta1)
        grupo_sprites.add(porta2)

        self.escolha_portas = True
        while self.escolha_portas:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            grupo_sprites.draw(self.tela)
            porta1.carregar()
            porta2.carregar()

            if pg.mouse.get_pressed()[0]:
                if porta1.rect.collidepoint(pg.mouse.get_pos()):
                    porta1.abrir()
                    return True

                if porta2.rect.collidepoint(pg.mouse.get_pos()):
                    porta2.abrir()
                    return False
            self.tela.blit(escolhaPortas, (150, 20))

            pg.display.update()
            pg.display.flip()
# --------------------------------- Função Recursiva ---------------------------------------------------------------
    def verificador(self, dano: int):
        if self.vida_inimigo >= dano:
            self.vida_inimigo -= dano
        else:
            if dano >= 1:
                self.verificador(dano - 1)
# ------------------------------------ Batalha -------------------------------------------------------------------
    def tela_batalha(self, personagem, inimigo, dano: int, vida: int):
        if inimigo == 'minotaur' or inimigo == 'evil cleric':
            pg.mixer.music.pause()
            som_batalha.stop()
            som_batalha_final.set_volume(0.4)
            som_batalha_final.play(-1)
        else:
            pg.mixer.music.pause()
            som_batalha.set_volume(0.4)
            som_batalha.play(-1)

        if personagem == 'cassio':
            personagem = classes.Cassio(200, 250)
        elif personagem == 'pietra':
            personagem = classes.Pietra(200, 250)
        if inimigo == 'imp':
            inimigo = classes.Imp(450, 250)
        elif inimigo == 'psionic':
            inimigo = classes.PsionicGoblin(450, 250)
        elif inimigo == 'death':
            inimigo = classes.Death(450, 250)
        elif inimigo == 'red orc':
            inimigo = classes.RedOrc(450, 250)
        elif inimigo == 'hunter orc':
            inimigo = classes.HunterOrc(450, 250)
        elif inimigo == 'ghost':
            inimigo = classes.Ghost(450, 250)
        elif inimigo == 'yellow ghost':
            inimigo = classes.YellowGhost(450, 250)
        elif inimigo == 'minotaur':
            self.imagem = txt_ultima_vitoria
            inimigo = classes.GreyMinotaur(400, 200)
        elif inimigo == 'evil cleric':
            self.imagem = txt_ultima_vitoria
            inimigo = classes.EvilCleric(450, 250)

        grupo_sprites = pg.sprite.Group()
        grupo_sprites.add(personagem)
        grupo_sprites.add(inimigo)

        barra_vida = pontos_vida

        self.vida_inimigo = vida
        self.imagem = txt_vitoria

        ataque = False
        esquiva = False
        especial = False
        errou_ataque = False
        acertou_ataque = False
        errou_esquiva = False
        acertou_esquiva = False
        errou_especial = False
        acertou_especial = False

        self.batalha = True
        while self.batalha:
            self.clock.tick(10)
            self.tela.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        esquiva = False
                        ataque = True
                        self.dado = randint(1, 6)
                        if self.dado >= 4:
                            acertou_ataque = True
                            errou_ataque = False
                            self.dano = 3
                            self.verificador(self.dano)
                            personagem.atack()
                        else:
                            errou_ataque = True
                            acertou_ataque = False

                        if dano > self.vida_personagem:
                            self.vida_personagem = 0
                        else:
                            self.vida_personagem -= dano
                        inimigo.atack()

                    if event.key == pg.K_z:
                        ataque = False
                        esquiva = True
                        inimigo.atack()
                        self.dado = randint(1,6)
                        if self.dado >= 4:
                            acertou_esquiva = True
                            errou_esquiva = False
                            self.dano = 1
                            self.verificador(self.dano)
                            personagem.atack()
                        else:
                            errou_esquiva = True
                            acertou_esquiva = False
                            self.vida_personagem -= dano
                    
                    if event.key == pg.K_s:
                        ataque = False
                        esquiva = False
                        especial = True
                        self.dado = randint(1,6)
                        if self.dado == 6:
                            acertou_especial = True
                            errou_especial = False
                            self.dano = 10
                            self.verificador(self.dano)
                            personagem.atack()
                        else:
                            errou_especial = True
                            acertou_especial = False
                            self.vida_personagem -= dano

                indice = self.dado - 1

            self.tela.blit(imgBatalha, (areaImgBatalha.x, areaImgBatalha.y))
            grupo_sprites.draw(self.tela)
            personagem.carregar()
            inimigo.carregar()

            self.tela.blit(txt_informacao_batalha, (270, 500))
            self.tela.blit(barra_vida[self.vida_personagem - 1], (0, 0))
            self.tela.blit(barra_vida[self.vida_inimigo - 1], (467, 0))

            if errou_ataque:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_errou_ataque, (0,0))
            elif acertou_ataque:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_acertou_ataque, (0,0))
            if errou_esquiva:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_errou_esquiva, (0,0))
            elif acertou_esquiva:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_acertou_esquiva, (0,0))
            if errou_especial:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_errou_especial, (0,0))
            elif acertou_especial:
                self.tela.fill((0,0,0))
                self.tela.blit(txt_acertou_especial, (0,0))
            if ataque or esquiva:
                self.tela.blit(lista_dados[indice], (0,0))

            self.tela.blit(imgBatalha, (areaImgBatalha.x, areaImgBatalha.y))
            grupo_sprites.draw(self.tela)
            personagem.carregar()
            inimigo.carregar()

            self.tela.blit(txt_informacao_batalha, (270, 500))
            self.tela.blit(barra_vida[self.vida_personagem - 1], (0, 0))
            self.tela.blit(barra_vida[self.vida_inimigo - 1], (467, 0))

            if self.vida_personagem == 0:
                self.tela.blit(txt_derrota, (150, 200))
                if pg.key.get_pressed()[pg.K_r]:
                    self.vida_inimigo = 10
                    self.vida_personagem = 10
                    self.tela_escolha()

            if self.vida_inimigo == 0:
                self.tela.blit(self.imagem, (150, 200))
                if pg.key.get_pressed()[pg.K_c]:
                    self.vida_inimigo = 10
                    self.vida_personagem = 10
                    return 'ganhou'

            pg.display.update()
            pg.display.flip()

    def tela_vitoria_cassio(self):
        self.vitoria_Cassio = True
        while self.vitoria_Cassio:
            self.clock.tick(10)
            self.tela.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.tela.blit(imgBatalha, (areaImgBatalha.x, areaImgBatalha.y))
            self.tela.blit(imagem_cassio, (200, 220))
            self.tela.blit(imagem_pietra, (280, 300))
            self.tela.blit(imagem_pontos_fala, (340, 270))
            self.tela.blit(imagem_pontos_fala, (270, 180))
            self.tela.blit(agradecimentoPietra, (320, 205))
            self.tela.blit(respostaCassio, (290, 100))

            pg.display.update()
            pg.display.flip()

    def tela_vitoria_pietra(self):
        self.vitoria_pietra = True
        while self.vitoria_pietra:
            self.clock.tick(10)
            self.tela.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.tela.blit(imgBatalha, (areaImgBatalha.x, areaImgBatalha.y))
            self.tela.blit(imagem_cassio, (280, 300))
            self.tela.blit(imagem_pietra, (200, 220))
            self.tela.blit(imagem_pontos_fala, (340, 270))
            self.tela.blit(imagem_pontos_fala, (270, 180))
            self.tela.blit(agradecimentoCassio, (320, 205))
            self.tela.blit(respostaPietra, (290, 100))

            pg.display.update()
            pg.display.flip()

# ----------------------------------------------------------------------------------------------------------------
    def tela_texto_inicial(self):
        loop = True
        while loop:
            self.tela.fill((67, 54, 55))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            if pg.key.get_pressed()[pg.K_SPACE]:
                self.tela_escolha()
            self.tela.blit(txt_inicial, (0, 0))

            pg.display.update()
            pg.display.flip()

# --------------------------------------------------- Tela de escolha -----------------------------------------------
    def tela_escolha(self):
        jogoLoop = True
        while jogoLoop:

            self.clock.tick(10)
            self.tela.fill((67, 54, 55))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif pg.key.get_pressed()[pg.K_p]:
                    self.tela_pause()
                elif event.type == pg.MOUSEBUTTONDOWN and self.colisaoEscolhaCassio:
                    pg.time.delay(100)

                    escolha1 = self.tela_escolha_portas()
                    if escolha1:
                        vencedor1 = self.tela_batalha(personagem='cassio', inimigo='imp', dano=1, vida=10)
                        if vencedor1 == 'ganhou':
                            escolha2 = self.tela_escolha_portas()
                            if escolha2:
                                vencedor2 = self.tela_batalha(personagem='cassio', inimigo='death', dano=1, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='red orc', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='evil cleric',dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='hunter orc', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                            else:
                                vencedor2 = self.tela_batalha(personagem='cassio', inimigo='psionic', dano=1, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='ghost', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='yellow ghost',dano=2, vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()

                    else:
                        vencedor1 = self.tela_batalha(personagem='cassio', inimigo='psionic', dano=1, vida=10)
                        if vencedor1 == 'ganhou':
                            escolha2 = self.tela_escolha_portas()
                            if escolha2:
                                vencedor2 = self.tela_batalha(personagem='cassio', inimigo='death', dano=1, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='red orc', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='hunter orc', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                            else:
                                vencedor2 = self.tela_batalha(personagem='cassio', inimigo='imp', dano=1,vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='ghost',dano=2, vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='cassio', inimigo='yellow ghost',dano=2, vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='cassio', inimigo='minotaur',dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='cassio',inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_cassio()

            self.contadorEscolhaCassio += 1
            if self.contadorEscolhaCassio == len(escolhaCassio):
                self.contadorEscolhaCassio = 0
            self.colisaoEscolhaCassio = areaEscolhaCassio.collidepoint(pg.mouse.get_pos())
            if self.colisaoEscolhaCassio:
                self.tela.blit(escolhaCassioEscala[self.contadorEscolhaCassio], (250 - escolhaCassioEscala[0].get_width()/2,self.telaY/2 - escolhaCassioEscala[0].get_height()/2))
            else:
                self.tela.blit(escolhaCassio[self.contadorEscolhaCassio], (250 - escolhaCassio[0].get_width()/2, self.telaY/2 - escolhaCassio[0].get_height()/2))

            self.contadorEscolhaPietra += 1
            if self.contadorEscolhaPietra == len(escolhaPietra):
                self.contadorEscolhaPietra = 0
            colisaoEscolhaPietra = areaEscolhaPietra.collidepoint(pg.mouse.get_pos())
            if colisaoEscolhaPietra:
                self.tela.blit(escolhaPietraEscala[self.contadorEscolhaPietra], (550 - escolhaPietraEscala[0].get_width()/2, self.telaY/2 - escolhaPietraEscala[0].get_height()/2))
                if pg.mouse.get_pressed()[0] == 1:
                    pg.time.delay(150)

                    escolha1 = self.tela_escolha_portas()
                    if escolha1:
                        vencedor1 = self.tela_batalha(personagem='pietra', inimigo='imp', dano=1, vida=10)
                        if vencedor1 == 'ganhou':
                            escolha2 = self.tela_escolha_portas()
                            if escolha2:
                                vencedor2 = self.tela_batalha(personagem='pietra', inimigo='death', dano=2, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='red orc', dano=2,vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='hunter orc', dano=2,
                                                                      vida=10)
                                        escolha4 = self.tela_escolha_portas()
                                        if escolha4:
                                            vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                          dano=2, vida=10)
                                            if vencedor4 == 'ganhou':
                                                self.tela_vitoria_pietra()
                                        else:
                                            vencedor4 = self.tela_batalha(personagem='pietra', inimigo='evil cleric',
                                                                          dano=2, vida=10)
                                            if vencedor4 == 'ganhou':
                                                self.tela_vitoria_pietra()
                            else:
                                vencedor2 = self.tela_batalha(personagem='pietra', inimigo='psionic', dano=2, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='ghost', dano=2,
                                                                      vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=15)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='yellow ghost',
                                                                      dano=2, vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()

                    else:
                        vencedor1 = self.tela_batalha(personagem='pietra', inimigo='psionic', dano=1, vida=10)
                        if vencedor1 == 'ganhou':
                            escolha2 = self.tela_escolha_portas()
                            if escolha2:
                                vencedor2 = self.tela_batalha(personagem='pietra', inimigo='death', dano=2, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='red orc', dano=2,
                                                                      vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='hunter orc', dano=2,
                                                                      vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                            else:
                                vencedor2 = self.tela_batalha(personagem='pietra', inimigo='imp', dano=2, vida=10)
                                if vencedor2 == 'ganhou':
                                    escolha3 = self.tela_escolha_portas()
                                    if escolha3:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='ghost', dano=2,
                                                                      vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                    else:
                                        vencedor3 = self.tela_batalha(personagem='pietra', inimigo='yellow ghost',
                                                                      dano=2, vida=10)
                                        if vencedor3 == 'ganhou':
                                            escolha4 = self.tela_escolha_portas()
                                            if escolha4:
                                                vencedor4 = self.tela_batalha(personagem='pietra', inimigo='minotaur',
                                                                              dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
                                            else:
                                                vencedor4 = self.tela_batalha(personagem='pietra',
                                                                              inimigo='evil cleric', dano=2, vida=10)
                                                if vencedor4 == 'ganhou':
                                                    self.tela_vitoria_pietra()
            else:
                self.tela.blit(escolhaPietra[self.contadorEscolhaPietra], (550 - escolhaPietra[0].get_width()/2, self.telaY/2 - escolhaPietra[0].get_height()/2))

            self.tela.blit(selecaoPersonagens, (0, 0))

            pg.display.flip()
            pg.display.update()

# ---------------------------------- Tela de Pause ----------------------------------------------------------------

    def tela_pause(self):
        pauseLoop = True
        while pauseLoop:
            self.tela.fill((67, 54, 55))
            self.clock.tick(10)

            colisaoBtnContinuar = areaBtnContinuar.collidepoint(pg.mouse.get_pos())
            colisaoBtnSair = areaBtnSair.collidepoint(pg.mouse.get_pos())

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            if colisaoBtnContinuar:
                self.tela.blit(btnContinuarEscala, (areaBtnContinuar.x * 0.975, areaBtnContinuar.y * 0.975))
                if pg.mouse.get_pressed()[0] == 1:
                    self.tela.fill((67, 54, 55))
                    pauseLoop = False
            else:
                self.tela.blit(btnContinuar, (areaBtnContinuar.x, areaBtnContinuar.y))

            if colisaoBtnSair:
                self.tela.blit(btnSairEscala, (areaBtnSair.x * 0.975, areaBtnSair.y * 0.975))

                if pg.mouse.get_pressed()[0] == 1:
                    pg.quit()
                    exit()
            else:
                self.tela.blit(btnSair, (250, 400))

            self.tela.blit(txtPause, (areaTxtPause.x, areaTxtPause.y))

            pg.display.update()
            pg.display.flip()

# --------------------------------- Main Loop ------------------------------------------------------------------

    def loop_game(self):

        pg.display.set_caption(self.nome)
        self.clock = pg.time.Clock()
        self.telaX, self.telaY = self.x, self.y
        self.tela = pg.display.set_mode((self.telaX, self.telaY))

        menuLoop = True
        while menuLoop:
            self.tela.fill((67, 54, 55))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            colisaoBtnJogar = areaBtnJogar.collidepoint(pg.mouse.get_pos())
            if colisaoBtnJogar:
                self.tela.blit(btnJogarEscala, (areaBtnJogar.x*0.975, areaBtnJogar.y*0.975))
                if pg.mouse.get_pressed()[0] == 1:
                    self.tela_texto_inicial()
            else:
                self.tela.blit(btnJogar, (areaBtnJogar.x, areaBtnJogar.y))

            colisaoBtnCreditos = areaBtnCreditos.collidepoint(pg.mouse.get_pos())
            if colisaoBtnCreditos:
                self.tela.blit(btnCreditosEscala, (self.telaX / 2 - btnCreditosEscala.get_width() / 2, self.telaY / 2 - btnCreditosEscala.get_height() / 2))
                if pg.mouse.get_pressed()[0] == 1:
                    self.tela_creditos()
            else:
                self.tela.blit(btnCreditos, (areaBtnCreditos.x, areaBtnCreditos.y))

            colisaoBtnSair = areaBtnSair.collidepoint(pg.mouse.get_pos())
            if colisaoBtnSair:
                self.tela.blit(btnSairEscala,
                               (self.telaX / 2 - btnSairEscala.get_width() / 2,
                                self.telaY - btnSairEscala.get_height() - 100))
                if pg.mouse.get_pressed()[0] == 1:
                    pg.quit()
                    exit()
            else:
                self.tela.blit(btnSair, (areaBtnSair.x, areaBtnSair.y))
            pg.display.update()
            pg.display.flip()

jogo = RPG("game", 800, 600)
jogo.loop_game()
