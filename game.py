import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
game_state = 'MENU'
sound_on = True

# Botões do jogo
start_button = Rect((WIDTH - 200) // 2, 300, 200, 50)
sound_button = Rect((WIDTH - 200) // 2, 370, 200, 50)
quit_button  = Rect((WIDTH - 200) // 2, 440, 200, 50)
menu_return_button = Rect((WIDTH - 300) // 2, 500, 300, 50)

# Inicia a tocar a música de fundo
music.play('theme.wav')
music.set_volume(1)

# Classe do herói
class Hero(Actor):
    # Iniciando o herói no jogo
    def __init__(self):
        super().__init__('player_idle', (400, 200))
        self.speed = 5

        self.images_walk = ['player_walk1', 'player_walk2']
        self.timer = 0
        self.frame_index = 0

    # Movimenta o herói
    def update(self):
        is_moving = False # Começa assumindo que ele está parado

        # Movimentação do personagem
        if keyboard.right and self.x < WIDTH - 150:
            self.x += self.speed
            is_moving = True

        if keyboard.left and self.x > 135:
            self.x -= self.speed
            is_moving = True

        if keyboard.up and self.y > 175:
            self.y -= self.speed
            is_moving = True

        if keyboard.down and self.y < 250:
            self.y += self.speed
            is_moving = True

        # Animação do personagem
        if is_moving:
            self.timer += 1
            if self.timer > 10:
                self.timer = 0
                self.frame_index += 1

                if self.frame_index >= len(self.images_walk):
                    self.frame_index = 0

                self.image = self.images_walk[self.frame_index]
        else:
            self.image = 'player_idle'


# Classe da bala
class Bullet(Actor):
    # Inicia a bala onde o herói está
    def __init__(self, x, y):
        super().__init__('bullet', (x, y))
        self.speed = 10

    # A bala segue em linha reta
    def update(self):
        self.y += self.speed


# Classe do zumbi
class Zombie(Actor):
    # Inicia o zumbi
    def __init__(self):
        x = random.randint(135, WIDTH-150)
        y = 650

        super().__init__('zombie_walk0', (x, y))
        self.speed = 2

        self.images_walk = ['zombie_walk0', 'zombie_walk1']

        self.timer = 0
        self.frame_index = 0

    # Movimenta o herói
    def update(self):
        self.y -= self.speed
        self.timer += 1

        if self.timer > 15:
            self.timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.images_walk):
                self.frame_index = 0

            self.image = self.images_walk[self.frame_index]



# Variáveis
my_hero = Hero()
bullets = []
zombies = []
spawn_timer = 0

# Função que faz os desenhos
def draw():
    screen.clear()

    # Caso do menu
    if game_state == 'MENU':
        screen.blit('background', (0, 0))

        # Título
        screen.draw.text("FARM DEFENDER", center=(WIDTH/2, 150), fontsize=60, color="orange", shadow=(1,1))

        # Botão jogar
        screen.draw.filled_rect(start_button, "green")
        screen.draw.text("JOGAR", center=start_button.center, fontsize=30, color="white")

        # Botão do som
        cor_som = "blue" if sound_on else "gray"
        texto_som = "SOM: ON" if sound_on else "SOM: OFF"
        screen.draw.filled_rect(sound_button, cor_som)
        screen.draw.text(texto_som, center=sound_button.center, fontsize=30, color="white")

        # Botão sair
        screen.draw.filled_rect(quit_button, "red")
        screen.draw.text("SAIR", center=quit_button.center, fontsize=30, color="white")

        # Dica visual extra
        screen.draw.text("Use o MOUSE para clicar", center=(WIDTH/2, 550), fontsize=20, color="white")

    # Caso do play
    elif game_state == 'PLAY':
        screen.blit('background', (0, 0))

        # Desenha o herói
        my_hero.draw()

        # Desenha as balas
        for b in bullets:
            b.draw()

        # Desenha os zumbis
        for z in zombies:
            z.draw()

        # Desenha o score
        screen.draw.text(f"SCORE: {score}", (10, 10), fontsize=30, color="white")

    # Caso do game over
    elif game_state == 'GAME_OVER':
        screen.fill((100, 0, 0))
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=80, color="white")
        screen.draw.text(f"Zombies Killed: {score}", center=(WIDTH/2, HEIGHT/2 + 60), fontsize=40, color="yellow")
        screen.draw.filled_rect(menu_return_button, "blue")
        screen.draw.text("VOLTAR AO MENU", center=menu_return_button.center, fontsize=30, color="white")


# Função que aciona o tiro
def on_key_down(key):
    global game_state, score, zombies, bullets

    if game_state == 'PLAY' and key == keys.SPACE:
        new_bullet = Bullet(my_hero.x, my_hero.y)
        bullets.append(new_bullet)

        if sound_on:
            sounds.shoot.play()

    if key == keys.RETURN and (game_state == 'MENU' or game_state == 'GAME_OVER'):
        game_state = 'PLAY'
        score = 0
        zombies = []
        bullets = []
        my_hero.pos = (400, 200)


# Função que aciona o botão do mouse
def on_mouse_down(pos):
    global game_state, sound_on, score, zombies, bullets, my_hero

    if game_state == 'MENU':

        # Clique no botão play
        if start_button.collidepoint(pos):
            game_state = 'PLAY'
            score = 0
            zombies = []
            bullets = []
            my_hero.pos = (400, 200)

        # Clique no botão som
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on

            # Aplica a mudança na música
            if sound_on:
                music.play('theme.wav')
                music.set_volume(1)
            else:
                music.stop()

        # Clique no botão sair
        elif quit_button.collidepoint(pos):
            quit()

    # Clique para reiniciar na tela de Game Over
    elif game_state == 'GAME_OVER':
        if menu_return_button.collidepoint(pos):
            game_state = 'MENU'


# Função update
def update():
    global spawn_timer, score, game_state

    if game_state == 'PLAY':
        # Atualiza o herói
        my_hero.update()

        # Atualiza as balas
        for b in bullets:
            b.update()

        # Gera os zumbis
        spawn_timer += 1
        if spawn_timer > 100:
            spawn_timer = 0
            new_zombie = Zombie()
            zombies.append(new_zombie)

        # Atualiza os zumbis
        for z in zombies:
            z.update()

        # Código da colisão
        for z in zombies[:]:
            hit = False

            if z.y < 250:
                game_state = 'GAME_OVER'

            for b in bullets[:]:
                if z.colliderect(b):
                    bullets.remove(b)
                    hit = True
                    if sound_on:
                        sounds.hit.play()
                    break

            if hit:
                zombies.remove(z)
                global score
                score += 1


pgzrun.go()
