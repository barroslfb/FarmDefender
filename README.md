# Farm Defender

Farm Defender é um jogo arcade 2D top-down desenvolvido em Python com a biblioteca [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/). O jogador controla um herói que precisa defender o topo da tela (sua fazenda) contra hordas de zumbis que sobem continuamente. 

Se um zumbi ultrapassar a linha de defesa, é Game Over.

## 📋 Funcionalidades

* **Menu Interativo:** Inicie o jogo, ligue/desligue a música de fundo e saia da aplicação usando o mouse.
* **Movimentação Fluida:** Controle o personagem em 4 direções (Cima, Baixo, Esquerda, Direita) respeitando os limites do cenário.
* **Animação de Sprites:** O herói e os zumbis possuem ciclos de animação (caminhada/idle) baseados em frames.
* **Sistema de Pontuação:** Cada zumbi eliminado incrementa o score do jogador.
* **Aumento de Dificuldade:** Geração contínua (spawn) de inimigos em posições aleatórias no eixo X.
* **Efeitos Sonoros:** Feedback de áudio para disparos, acertos nos inimigos e música de fundo contínua (com opção de mute).

## 🎮 Controles

| Ação | Tecla / Input |
| :--- | :--- |
| **Movimentar o Herói** | Setas do Teclado (`↑`, `↓`, `←`, `→`) |
| **Atirar** | `Espaço` |
| **Interagir com Menus** | `Clique do Mouse` |
| **Iniciar via Teclado** | `Enter` (Na tela inicial ou de Game Over) |

## 🚀 Como executar o projeto

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. É necessário instalar a biblioteca `pgzrun` (Pygame Zero).

```bash
pip install pgzero
