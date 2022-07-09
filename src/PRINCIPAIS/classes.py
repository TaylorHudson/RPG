import pygame as pg
import loads


# --------------------------- Personagens ---------------------------------------------------------------------
class Cassio(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.atacar_especial = False

        self.cassio_ataque = loads.cassio_ataque
        self.cassio_ataque_especial = loads.cassio_ataque_especial
        self.cont_sprites_ataque = 0
        self.cont_sprites_ataque_especial = 0
        self.image = self.cassio_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack_especial(self):
        self.atacar_especial = True

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar_especial:
            self.cont_sprites_ataque_especial += 1

            if self.cont_sprites_ataque_especial >= len(self.cassio_ataque_especial):
                self.cont_sprites_ataque_especial = 0
                self.atacar_especial = False

            self.image = self.cassio_ataque_especial[self.cont_sprites_ataque_especial]

        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.cassio_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.cassio_ataque[self.cont_sprites_ataque]


class Pietra(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False

        self.pietra_ataque = loads.pietra_ataque
        self.cont_sprites_ataque = 0
        self.image = self.pietra_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.pietra_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.pietra_ataque[self.cont_sprites_ataque]


# -------------------------------------- Inimigos ----------------------------------------------------------------
class Ghost(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.ghost_ataque = loads.ghost_ataque
        self.cont_sprites_ataque = 0
        self.image = self.ghost_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.ghost_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.ghost_ataque[self.cont_sprites_ataque]


class Imp(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False

        self.imp_ataque = loads.imp_ataque
        self.cont_sprites_ataque = 0
        self.image = self.imp_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.imp_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.imp_ataque[self.cont_sprites_ataque]


class PsionicGoblin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False

        self.psionicGoblin_ataque = loads.psionicGoblin_ataque
        self.cont_sprites_ataque = 0
        self.image = self.psionicGoblin_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.psionicGoblin_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.psionicGoblin_ataque[self.cont_sprites_ataque]


class Assassin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.assassin_ataque = loads.assassin_ataque
        self.cont_sprites_ataque = 0
        self.image = self.assassin_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.assassin_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.assassin_ataque[self.cont_sprites_ataque]


class GreyMinotaur(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.greyMinotaur_ataque = loads.greyMinotaur_ataque
        self.cont_sprites_ataque = 0
        self.image = self.greyMinotaur_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.greyMinotaur_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.greyMinotaur_ataque[self.cont_sprites_ataque]


class HunterOrc(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.hunterOrc_ataque = loads.hunterOrc_ataque
        self.cont_sprites_ataque = 0
        self.image = self.hunterOrc_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.hunterOrc_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.hunterOrc_ataque[self.cont_sprites_ataque]


class YellowGhost(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.yellowGhost_ataque = loads.yellowGhost_ataque
        self.cont_sprites_ataque = 0
        self.image = self.yellowGhost_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.yellowGhost_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.yellowGhost_ataque[self.cont_sprites_ataque]


class RedOrc(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.redOrc_ataque = loads.redOrc_ataque
        self.cont_sprites_ataque = 0
        self.image = self.redOrc_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.redOrc_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.redOrc_ataque[self.cont_sprites_ataque]



class Death(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.death_ataque = loads.death_ataque
        self.cont_sprites_ataque = 0
        self.image = self.death_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.death_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.death_ataque[self.cont_sprites_ataque]


class EvilCleric(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.atacar = False
        self.morte = False

        self.evil_ataque = loads.evilCleric_ataque
        self.cont_sprites_ataque = 0
        self.image = self.evil_ataque[self.cont_sprites_ataque]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def atack(self):
        self.atacar = True

    def carregar(self):
        if self.atacar:
            self.cont_sprites_ataque += 1

            if self.cont_sprites_ataque >= len(self.evil_ataque):
                self.cont_sprites_ataque = 0
                self.atacar = False

            self.image = self.evil_ataque[self.cont_sprites_ataque]

#--------------------------------------- Porta ------------------------------------------------------------------
class Porta(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.abre = False

        self.sprites_porta = loads.sprites_porta
        self.cont_porta = 0
        self.image = self.sprites_porta[self.cont_porta]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def abrir(self):
        self.abre = True

    def carregar(self):
        if self.abre:
            self.cont_porta += 1
            if self.cont_porta <= len(self.sprites_porta):
                self.cont_porta = 3
                self.abre = False
            self.image = self.sprites_porta[self.cont_porta]
