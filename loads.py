import pygame as pg

pg.mixer.init()

def spriteLista(lista, finalRange, local):
    for i in range(1, finalRange-1):
        lista.append(pg.image.load('%s%s.png' % (local, i)))

def spriteListaEscala(lista, img, finalRange):
    for i in range(finalRange-2):
        lista.append(pg.transform.scale(img[i], (img[0].get_width()*1.05, img[0].get_height()*1.05)))

# música/sons
musica_jogo = pg.mixer.music.load('musicasDoProjeto/som_de_fundo.mpga')
som_batalha = pg.mixer.Sound('musicasDoProjeto/FIGHT.mp3')
som_batalha_final = pg.mixer.Sound('musicasDoProjeto/FINAL_FIGHT.mp3')

# texto
txt_inicial = pg.image.load('IMAGENS/INFOS/txtInicio.png')
txt_vitoria = pg.image.load('IMAGENS/INFOS/txtVitoria2.png')
txt_opc_habilidade = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/opcaoHabilidade.png')
txt_derrota = pg.image.load('IMAGENS/INFOS/txtDerrota.png')
txt_ultima_vitoria = pg.image.load('IMAGENS/INFOS/txtUltimaVitoria.png')
txt_informacao_batalha_pietra = pg.image.load('IMAGENS/INFOS/informacao_de_batalha.png')
txt_informacao_batalha_cassio = pg.image.load('IMAGENS/INFOS/informacao_de_batalha_cassio.png')
txt_errou_ataque = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/errou_ataque.png')
txt_acertou_ataque = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/acertou_ataque.png')
txt_errou_esquiva = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/errou_esquiva.png')
txt_acertou_esquiva = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/acertou_esquiva.png')
txt_errou_especial = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/errou_especial.png')
txt_acertou_especial = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/acertou_especial.png')
txt_errou_cura = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/errou_cura.png')
txt_acertou_cura = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/acertou_cura.png')
txtPause = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/pause.png')
areaTxtPause = txtPause.get_rect(x=250, y=10)
escala_txt_inicial = pg.transform.scale(txt_inicial,(txt_inicial.get_rect().h*3.1, txt_inicial.get_rect().w*2.5))
txtCreditos = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/creditos.png')
areaTxtCreditos = txtCreditos.get_rect(x=200, y=180)
txtCreditosEscala = pg.transform.scale(txtCreditos, (areaTxtCreditos.w * 1, areaTxtCreditos.h * 1))
agradecimentoPietra = pg.image.load('IMAGENS/INFOS/agradecimentoPietra.png')
respostaCassio = pg.image.load('IMAGENS/INFOS/respostaCassio.png')
agradecimentoCassio = pg.image.load('IMAGENS/INFOS/agradecimentoCassio.png')
respostaPietra = pg.image.load('IMAGENS/INFOS/respostaPietra.png')

# imagem
imagem_pontos_fala = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/pontos_Fala.png')
imagem_cassio = pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/PARADO/1.png')
imagem_pietra = pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/PARADO/1.png')
escolhaPortas = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/escolhaPortas.png')

# pontos de vida
pontos_vida = []
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/1.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/2.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/3.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/4.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/5.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/6.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/7.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/8.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/9.png'))
pontos_vida.append(pg.image.load('IMAGENS/INFOS/PONTOS_DE_VIDA/10.png'))

# dados
lista_dados = [
pg.image.load('IMAGENS/INFOS/DADOS/1.png'),
pg.image.load('IMAGENS/INFOS/DADOS/2.png'),
pg.image.load('IMAGENS/INFOS/DADOS/3.png'),
pg.image.load('IMAGENS/INFOS/DADOS/4.png'),
pg.image.load('IMAGENS/INFOS/DADOS/5.png'),
pg.image.load('IMAGENS/INFOS/DADOS/6.png'),
]

# Carregar imagens
ficha_pietra = pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ficha_pietra.png')
ficha_cassio = pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ficha_cassio.png')

btnJogar = pg.image.load('IMAGENS/BOTÕES/btnJogar.png')
areaBtnJogar = btnJogar.get_rect(x=800 / 2 - btnJogar.get_width() / 2, y=btnJogar.get_height())
btnJogarEscala = pg.transform.scale(btnJogar, (areaBtnJogar.w * 1.05, areaBtnJogar.h * 1.05))

btnCreditos = pg.image.load('IMAGENS/BOTÕES/btnCreditos.png')
areaBtnCreditos = btnCreditos.get_rect(x= 800/ 2 - btnCreditos.get_width() / 2, y=600 / 2 - btnCreditos.get_height() / 2)
btnCreditosEscala = pg.transform.scale(btnCreditos, (areaBtnCreditos.w * 1.05, areaBtnCreditos.h * 1.05))

btnSair = pg.image.load('IMAGENS/BOTÕES/btnSair.png')
areaBtnSair = btnSair.get_rect(x= 800 / 2 - btnSair.get_width() / 2, y= 600 - btnSair.get_height() - 100)
btnSairEscala = pg.transform.scale(btnSair, (areaBtnSair.w * 1.05, areaBtnSair.h * 1.05))

btnVoltar = pg.image.load('IMAGENS/BOTÕES/voltar.png')
areaBtnVoltar = btnVoltar.get_rect(x=10, y=10)

btnContinuar = pg.image.load('IMAGENS/BOTÕES/btnContinuar.png')
areaBtnContinuar = btnContinuar.get_rect(x=250, y=200)
btnContinuarEscala = pg.transform.scale(btnContinuar, (areaBtnContinuar.w * 1.05, areaBtnContinuar.h * 1.05))

imgBatalha = pg.image.load('IMAGENS/FUNDO/fundoBatalha/fundoBatalha2.png')
areaImgBatalha = imgBatalha.get_rect(x=15, y=40)

# Carregar sprites
fundoJogo, fundoMenu, escolhaCassio = [], [], []
escolhaCassioEscala, escolhaPietra, escolhaPietraEscala = [], [], []
spriteCassioParado = []

spriteLista(fundoJogo, 6, 'IMAGENS/FUNDO/fundoJogo/')
spriteLista(fundoMenu, 16, 'IMAGENS/FUNDO/fundoMenu/')

selecaoPersonagens = pg.image.load('IMAGENS/INFOS/TEXTOS SEM FUNDO/selecaoDePersonagens.png')

spriteLista(escolhaCassio, 21, 'IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESCOLHA/')
areaEscolhaCassio = escolhaCassio[0].get_rect(x=250 - escolhaCassio[0].get_width() / 2, y=600 / 2 - escolhaCassio[0].get_height() / 2)
spriteListaEscala(escolhaCassioEscala, escolhaCassio, 21)

spriteLista(escolhaPietra, 23, 'IMAGENS/PERSONAGENS/PIETRA/SPRITE/ESCOLHA/')
areaEscolhaPietra = escolhaPietra[0].get_rect(x=550 - escolhaPietra[0].get_width() / 2, y=600 / 2 - escolhaPietra[0].get_height() / 2)
spriteListaEscala(escolhaPietraEscala, escolhaPietra, 23)

# Sprites
sprites_porta = []
um = pg.image.load('IMAGENS/FUNDO/PORTA/1.png')
sprites_porta.append(pg.image.load('IMAGENS/FUNDO/PORTA/1.png'))
sprites_porta.append(pg.image.load('IMAGENS/FUNDO/PORTA/2.png'))
sprites_porta.append(pg.image.load('IMAGENS/FUNDO/PORTA/3.png'))
sprites_porta.append(pg.image.load('IMAGENS/FUNDO/PORTA/4.png'))

cassio_ataque_especial = [
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/0.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/1.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/2.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/3.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/4.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/5.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/6.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/7.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/8.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/9.png'),
pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ESPECIAL/10.png'),
]

cassio_ataque = []
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/1.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/2.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/3.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/4.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/5.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/6.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/7.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/8.png'))
cassio_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/CÁSSIO/SPRITE/ATAQUE/9.png'))

pietra_ataque = []
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/1.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/2.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/3.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/4.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/5.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/6.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/7.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/8.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/9.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/10.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/11.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/12.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/13.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/14.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/15.png'))
pietra_ataque.append(pg.image.load('IMAGENS/PERSONAGENS/PIETRA/SPRITE/ATAQUE/16.png'))

ghost_ataque = []
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/35.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/36.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/37.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/38.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/39.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/40.png'))
ghost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Ghost/ATAQUE/41.png'))

imp_ataque = []
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/32.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/33.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/34.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/35.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/36.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/37.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/38.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/39.png'))
imp_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Imp/ATAQUE/40.png'))

psionicGoblin_ataque = []
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/32.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/33.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/34.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/35.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/36.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/37.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/38.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/39.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/40.png'))
psionicGoblin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/PsionicGoblin/ATAQUE/41.png'))

assassin_ataque = []
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/32.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/33.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/34.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/35.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/36.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/37.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/38.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/39.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/40.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/41.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/42.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/43.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/44.png'))
assassin_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Assassin/ATAQUE/45.png'))

greyMinotaur_ataque = []
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/31.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/32.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/33.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/34.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/35.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/36.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/37.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/38.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/39.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/40.png'))
greyMinotaur_ataque.append(pg.image.load('IMAGENS/INIMIGOS/GreyMinotaur/ATAQUE/41.png'))

hunterOrc_ataque = []
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/32.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/33.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/34.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/35.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/36.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/37.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/38.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/39.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/40.png'))
hunterOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/HunterOrc/ATAQUE/41.png'))

yellowGhost_ataque = []
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/31.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/32.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/33.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/34.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/35.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/36.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/37.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/38.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/39.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/40.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/41.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/42.png'))
yellowGhost_ataque.append(pg.image.load('IMAGENS/INIMIGOS/YellowGhost/ATAQUE/43.png'))

redOrc_ataque = []
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/31.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/32.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/33.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/34.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/35.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/36.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/37.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/38.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/39.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/40.png'))
redOrc_ataque.append(pg.image.load('IMAGENS/INIMIGOS/RedOrc/ATAQUE/41.png'))

death_ataque = []
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/31.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/32.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/33.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/34.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/35.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/36.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/37.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/38.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/39.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/40.png'))
death_ataque.append(pg.image.load('IMAGENS/INIMIGOS/Death/ATAQUE/41.png'))

evilCleric_ataque = []
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/31.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/32.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/33.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/34.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/35.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/36.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/37.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/38.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/39.png'))
evilCleric_ataque.append(pg.image.load('IMAGENS/INIMIGOS/EvilCleric/ATAQUE/40.png'))


