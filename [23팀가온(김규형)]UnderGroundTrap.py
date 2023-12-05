#release/minor/fix/develop
#alpha 1.0.0.0
#설정 키변경 rect조정, 동굴 이벤트 때마다 재생성 수정

import pygame
import random
from moviepy.editor import VideoFileClip

pygame.init()

screen_W, screen_L = 1280, 720
screen = pygame.display.set_mode((screen_W, screen_L))
pygame.display.set_caption("UnderGroundTrap [UGT]")
clock = pygame.time.Clock()
#font
game_font = pygame.font.Font(None, 40)
screen.blit(pygame.image.load('data/img/background/KAON.png'), (0,0))
pygame.display.update()
#background images
Intro_Background = pygame.image.load('data/img/background/Intro_background.png')
Menu_Background = pygame.image.load('data/img/background/Menu_background.png')
cave = pygame.image.load('data/img/background/cave.png')

#ui images
setting_ui = pygame.image.load('data/img/ui/setting_ui.png')
setting_bar = pygame.image.load('data/img/ui/bar.png')

quit_ui = pygame.image.load('data/img/ui/quit_ui.png')
temp_ui = pygame.image.load('data/img/ui/temp_ui.png')

unfilled_star = pygame.image.load('data/img/ui/unfilled_star.png')
filled_star = pygame.image.load('data/img/ui/filled_star.png')

ingame_ui = pygame.image.load('data/img/ui/ingame_ui.png')

init_ui = pygame.image.load('data/img/ui/init_ui.png')

result_ui = []
for i in range(5):
    result_ui.append(pygame.image.load('data/img/ui/result_ui_{0}.png'.format(i)))
infinite_result_ui = [pygame.image.load('data/img/ui/infi_result_ui.png'), pygame.image.load('data/img/ui/infi_result_ui_new.png')]

#button images
Me_B_stage_N = pygame.image.load('data/img/ui/button_menu_stage_normal.png')
Me_B_stage_H = pygame.image.load('data/img/ui/button_menu_stage_hover.png')

Me_B_setting_N = pygame.image.load('data/img/ui/button_menu_setting_normal.png')
Me_B_setting_H = pygame.image.load('data/img/ui/button_menu_setting_hover.png')

Me_B_infinite_N = pygame.image.load('data/img/ui/button_menu_infinite_normal.png')
Me_B_infinite_H = pygame.image.load('data/img/ui/button_menu_infinite_hover.png')

sest_B_forbidden_stage = pygame.image.load('data/img/ui/button_sest_forbidden_stage.png')

Sein_B_easy_N = pygame.image.load('data/img/ui/button_sein_easy_normal.png')
Sein_B_easy_H = pygame.image.load('data/img/ui/button_sein_easy_hover.png')

Sein_B_normal_N = pygame.image.load('data/img/ui/button_sein_normal_normal.png')
Sein_B_normal_H = pygame.image.load('data/img/ui/button_sein_normal_hover.png')

Sein_B_hard_N = pygame.image.load('data/img/ui/button_sein_hard_normal.png')
Sein_B_hard_H = pygame.image.load('data/img/ui/button_sein_hard_hover.png')

Sein_B_expert_N = pygame.image.load('data/img/ui/button_sein_expert_normal.png')
Sein_B_expert_H = pygame.image.load('data/img/ui/button_sein_expert_hover.png')

Sein_B_impossible_N = pygame.image.load('data/img/ui/button_sein_impossible_normal.png')
Sein_B_impossible_H = pygame.image.load('data/img/ui/button_sein_impossible_hover.png')

B_setting_N = pygame.image.load('data/img/ui/button_setting_normal.png')
B_setting_H = pygame.image.load('data/img/ui/button_setting_hover.png')

B_return_N = pygame.image.load('data/img/ui/button_return_normal.png')
B_return_H = pygame.image.load('data/img/ui/button_return_hover.png')

Q_B_quit_N = pygame.image.load('data/img/ui/button_quit_quit_normal.png')
Q_B_quit_H = pygame.image.load('data/img/ui/button_quit_quit_hover.png')

Q_B_cancel_N = pygame.image.load('data/img/ui/button_quit_cancel_normal.png')
Q_B_cancel_H = pygame.image.load('data/img/ui/button_quit_cancel_hover.png')

T_B_join_N = pygame.image.load('data/img/ui/button_temp_join_normal.png')
T_B_join_H = pygame.image.load('data/img/ui/button_temp_join_hover.png')

T_B_restart_N = pygame.image.load('data/img/ui/button_temp_restart_normal.png')
T_B_restart_H = pygame.image.load('data/img/ui/button_temp_restart_hover.png')

T_B_main_N = pygame.image.load('data/img/ui/button_temp_main_normal.png')
T_B_main_H = pygame.image.load('data/img/ui/button_temp_main_hover.png')

R_B_restart_N = pygame.image.load('data/img/ui/button_result_restart_normal.png')
R_B_restart_H = pygame.image.load('data/img/ui/button_result_restart_hover.png')

R_B_main_N = pygame.image.load('data/img/ui/button_result_main_normal.png')
R_B_main_H = pygame.image.load('data/img/ui/button_result_main_hover.png')

S_B_key_N = pygame.image.load('data/img/ui/button_setting_key_normal.png')
S_B_key_H = pygame.image.load('data/img/ui/button_setting_key_hover.png')

S_B_init_N = pygame.image.load('data/img/ui/button_setting_init_normal.png')
S_B_init_H = pygame.image.load('data/img/ui/button_setting_init_hover.png')

S_B_full_N = pygame.image.load('data/img/ui/button_setting_full_normal.png')
S_B_full_H = pygame.image.load('data/img/ui/button_setting_full_hover.png')

S_B_window_N = pygame.image.load('data/img/ui/button_setting_window_normal.png')
S_B_window_H = pygame.image.load('data/img/ui/button_setting_window_hover.png')

T_B_next_N = pygame.image.load('data/img/ui/button_tut_next_normal.png')
T_B_next_H = pygame.image.load('data/img/ui/button_tut_next_hover.png')

T_B_skip_N = pygame.image.load('data/img/ui/button_tut_skip_normal.png')
T_B_skip_H = pygame.image.load('data/img/ui/button_tut_skip_hover.png')

T_B_undo_N = pygame.image.load('data/img/ui/button_tut_undo_normal.png')
T_B_undo_H = pygame.image.load('data/img/ui/button_tut_undo_hover.png')
tut_ui = []
for i in range(1,6):
    tut_ui.append(pygame.image.load('data/img/ui/tut_{0}.png'.format(i)))
#objectives images
player_move_img = []
for i in range(1,7):
    player_move_img.append(pygame.image.load('data/img/objective/player/player_move_{0}.png'.format(i)))
enemy_a_move_img = []
for i in range(1,7):
    enemy_a_move_img.append(pygame.image.load('data/img/objective/enemy_a/enemy_a_move_{0}.png'.format(i)))
enemy_b_move_img = []
for i in range(1,7):
    enemy_b_move_img.append(pygame.image.load('data/img/objective/enemy_b/enemy_b_move_{0}.png'.format(i)))
player_attack_img = pygame.image.load('data/img/objective/player/player_attack.png')
attack_a_img = pygame.image.load('data/img/objective/attack_a.png')
attack_b_img = pygame.image.load('data/img/objective/attack_b.png')
#bgm
main_bgm = pygame.mixer.Sound('data/sound/bgm/main_bgm.mp3')
ingame_bgm = pygame.mixer.Sound('data/sound/bgm/ingame_bgm.mp3')
etc_bgm = pygame.mixer.Sound('data/sound/bgm/etc_bgm.mp3')
#effect sound
click_sound = pygame.mixer.Sound('data/sound/effect/click.mp3')
banned_click_sound = pygame.mixer.Sound('data/sound/effect/banned_click.mp3')
cancel_sound = pygame.mixer.Sound('data/sound/effect/cancel.mp3')
step_sound = pygame.mixer.Sound('data/sound/effect/step.mp3')
sword_sound = pygame.mixer.Sound('data/sound/effect/sword.mp3')
hit_sound = []
for i in range(1, 4):
    hit_sound.append(pygame.mixer.Sound('data/sound/effect/hit{0}.mp3'.format(i)))

#video
tut_intro_video = VideoFileClip("data/video/tut_intro.mp4")
ending_video = VideoFileClip("data/video/ending.mp4")

def getSurface(t, clip=ending_video, srf=None):
    frame = clip.get_frame(t=t)
    
    if srf is None:
        return pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    else:
        pygame.surfarray.blit_array(srf, frame.swapaxes(0, 1))
        return srf
surface = getSurface(0)

with open('data/playerdata/setting.txt', 'r', encoding='utf8') as file:
    f = [i.replace('\n','') for i in file]
    try:
        master_sound = float(f[0])
    except:
        master_sound = 1.0
    try:
        bgm_sound = float(f[1])
    except:
        bgm_sound = 1.0
    try:
        effect_sound = float(f[2])
    except:
        effect_sound = 1.0
    master_sound_X = 300*master_sound+304
    bgm_sound_X = 300*bgm_sound+304
    effect_sound_X = 300*effect_sound+304
    K = [0 for _ in range(11)]
    K_V = [0 for _ in range(11)]
    for i in range(11):
        try:
            K[i] = int(f[3+i])
        except:
            K[i] = 49+i
        K_V[i] = pygame.key.name(K[i])
    
    for i in range(11):
        if K_V[i] == '':
            if K[i] == 1:
                K_V[i] = 'L Click'
            elif K[i] == 2:
                K_V[i] = 'W Click'
            elif K[i] == 3:
                K_V[i] = 'R Click'
with open('data/playerdata/playerdata.txt', 'r', encoding = 'utf8') as file:
    f = [i.replace('\n', '') for i in file]
    tut = f[0]
    stage = int(f[1])
    star = []
    for i in range(2, 12):
        star.append(int(f[i]))
    high_time = []
    for i in range(12, 17):
        high_time.append(float(f[i]))
    ending = f[17]
    
#sound
main_bgm.set_volume(master_sound*bgm_sound)
ingame_bgm.set_volume(master_sound*bgm_sound)
etc_bgm.set_volume(master_sound*bgm_sound)

click_sound.set_volume(master_sound*effect_sound)
banned_click_sound.set_volume(master_sound*effect_sound)
cancel_sound.set_volume(master_sound*effect_sound)
step_sound.set_volume(master_sound*effect_sound)
sword_sound.set_volume(master_sound*effect_sound)
for i in range(3):
    hit_sound[i].set_volume(master_sound*effect_sound)

#setting element
class bar():
    def __init__(self, x, y):
        self.y = y
        self.x = x #max = 604, min = 304
        self.rect = pygame.Rect(self.x, self.y, 15, 59)
        self.drag = False
    def move(self, event):
        if event.pos[0] >= 290 and event.pos[0] <= 619:
            self.x = event.pos[0]
            self.drag = True
        if event.pos[0] <= 304 and event.pos[0] >= 290:
            self.x = 304
        if event.pos[0] >= 604 and event.pos[0] <= 619:
            self.x = 604
    def draw(self):
        screen.blit(setting_bar, (self.x, self.y))

bar_a = bar(master_sound_X, 262)
bar_b = bar(bgm_sound_X, 375)
bar_c = bar(effect_sound_X, 492)

class Button():
    def __init__(self, N, H, W, L, X_time, X_div, Y_time, Y_div):
        self.N = N
        self.H = H
        self.W = W
        self.L = L
        self.X_time = X_time
        self.Y_time = Y_time
        self.X_div = X_div
        self.Y_div = Y_div
        self.rect = pygame.Rect((self.X_time*(screen_W - self.W)//self.X_div), (self.Y_time*(screen_L - self.L)//self.Y_div), self.W, self.L)
        self.state = self.N
    def draw(self):
        screen.blit(self.state, self.rect)

#button
#normal, hover, width, legth, x_time, X_div, Y_time, Y_div
Me_B_stage = Button(Me_B_stage_N, Me_B_stage_H, 700, 156, 1, 2, 1, 8)
Me_B_infinite = Button(Me_B_infinite_N, Me_B_infinite_H, 700, 156, 1, 2, 1, 2)
Me_B_setting = Button(Me_B_setting_N, Me_B_setting_H, 700, 156, 1, 2, 7, 8)
Sein_B = []
Sein_B.append(Button(Sein_B_easy_N, Sein_B_easy_H, 500, 111, 1, 5, 1, 10))
Sein_B.append(Button(Sein_B_normal_N, Sein_B_normal_H, 500, 111, 1, 5, 3, 10))
Sein_B.append(Button(Sein_B_hard_N, Sein_B_hard_H, 500, 111, 1, 5, 1, 2))
Sein_B.append(Button(Sein_B_expert_N, Sein_B_expert_H, 500, 111, 1, 5, 7, 10))
Sein_B.append(Button(Sein_B_impossible_N, Sein_B_impossible_H, 500, 111, 1, 5, 9, 10))
Sest_B = []
for i in range(1, 6):
    Sest_B.append(Button(pygame.image.load('data/img/ui/button_sest_{0}_normal.png'.format(i)), pygame.image.load('data/img/ui/button_sest_{0}_hover.png'.format(i)),156, 156, i, 6, 1, 3))
for i in range(6, 11):
    Sest_B.append(Button(pygame.image.load('data/img/ui/button_sest_{0}_normal.png'.format(i)), pygame.image.load('data/img/ui/button_sest_{0}_hover.png'.format(i)),156, 156, i-5, 6, 2, 3))

B_setting = Button(B_setting_N, B_setting_H, 70, 70, 1, 1, 1, 1)
B_return = Button(B_return_N, B_return_H, 70, 70, 1, 1, 1, 1)
Q_B_quit = Button(Q_B_quit_N, Q_B_quit_H, 200, 60, 1, 1, 1, 1)
Q_B_cancel = Button(Q_B_cancel_N, Q_B_cancel_H, 200, 60, 1, 1, 1, 1)
T_B_join = Button(T_B_join_N, T_B_join_H, 200, 60, 1, 2, 2, 5)
T_B_restart = Button(T_B_restart_N, T_B_restart_H, 200, 60, 1, 2, 1, 2)
T_B_main = Button(T_B_main_N, T_B_main_H, 200, 60, 1, 2, 3, 5)
R_B_restart = Button(R_B_restart_N, R_B_restart_H, 300, 100, 1, 2, 1, 2)
R_B_main = Button(R_B_main_N, R_B_main_H, 300, 100, 1, 2, 3, 5)
S_B_init = Button(S_B_init_N, S_B_init_H, 200, 60, 1, 2, 3, 5)
I_B_init = Button(S_B_init_N, S_B_init_H, 200, 60, 1, 2, 3, 5)
S_B_window_change = Button(S_B_window_N, S_B_window_H, 200, 60, 1, 2, 3, 5)
T_B_next = Button(T_B_next_N, T_B_next_H, 200, 60, 1, 1, 1, 1)
T_B_skip = Button(T_B_skip_N, T_B_skip_H, 200, 60, 1, 1, 1, 1)
T_B_undo = Button(T_B_undo_N, T_B_undo_H, 200, 60, 1, 1, 1, 1)
B_setting.rect.x, B_setting.rect.y = 10, 10
B_return.rect.x, B_return.rect.y = 10, 640
Q_B_quit.rect.x, Q_B_quit.rect.y = 440, 425
Q_B_cancel.rect.x, Q_B_cancel.rect.y = 640, 425
R_B_restart.rect.x, R_B_restart.rect.y = 800, 350
R_B_main.rect.x, R_B_main.rect.y = 800, 480
S_B_init.rect.x, S_B_init.rect.y = 919, 480
S_B_window_change.rect.x, S_B_window_change.rect.y = 919, 240
I_B_init.rect.x, I_B_init.rect.y = 440, 425
T_B_next.rect.x, T_B_next.rect.y = 1070, 650
T_B_skip.rect.x, T_B_skip.rect.y = 1070, 10
T_B_undo.rect.x, T_B_undo.rect.y = 10, 650
for i in range(stage+1, 10):
    Sest_B[i].N = sest_B_forbidden_stage
    Sest_B[i].H = sest_B_forbidden_stage

S_B_key = [Button(S_B_key_N, S_B_key_H, 122, 26, 1, 1, 1, 1) for _ in range(11)]
for i in range(11):
    S_B_key[i].rect.center = (821, 216 + (37.5*i))

def Button_state_reset():
    Me_B_stage.state = Me_B_stage.N
    Me_B_infinite.state = Me_B_infinite.N
    Me_B_setting.state = Me_B_setting.N
    for i in range(5):
        Sein_B[i].state = Sein_B[i].N
    for i in range(10):
        Sest_B[i].state = Sest_B[i].N
    B_setting.state = B_setting.N
    B_return.state = B_return.N
    Q_B_quit.state = Q_B_quit.N
    Q_B_cancel.state = Q_B_cancel.N
    T_B_join.state = T_B_join.N
    T_B_restart.state = T_B_restart.N
    T_B_main.state = T_B_main.N
    R_B_restart.state = R_B_restart.N
    R_B_main.state = R_B_main.N
    S_B_init.state = S_B_init.N
    S_B_window_change.state = S_B_window_change.N
    I_B_init.state = I_B_init.N
    T_B_next.state = T_B_next.N
    T_B_skip.state = T_B_skip.N
    T_B_undo.state = T_B_undo.N

star_V = []
for i in range(10):
    star_V.append([Sest_B[i].rect.x, Sest_B[i].rect.x+53, Sest_B[i].rect.x+106, Sest_B[i].rect.y-25, star[i]])

#var
stage_cave = [2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
stage_enemy = [10, 15, 20, 25, 32, 40, 50, 70, 85, 100]
stage_time = [10, 7, 5, 4, 3, 2, 1, 0.7, 0.6, 0.5]
stage_attack = [20, 30, 37, 40, 45, 60, 70, 80, 100, 110]
stage_damage = [1, 3, 5, 7, 10, 10, 15, 20, 25, 30]
stage_speed = [80, 100, 120, 150, 170, 200, 220, 250, 270, 300]
hp = 100

#easy, normal, hard, expert, impossible
infinite_cave = [3, 5, 7, 9, 9]
infinite_attack = [3, 2, 2, 1, 1]
infinite_damage = [5, 10, 40, 50, 100]
infinite_speed = [80, 150, 200, 250, 350]
infinite_time = [7, 5, 2, 1, 0.4]

P_stage = 0
P_stage_speed = 0
P_stage_cave = 0
P_stage_enemy = 0
P_stage_time = 0
P_stage_attack = 0
P_infinite_attack = 0
P_stage_damage = 0
P_summon_enemy = 0
P_killed_enemy = 0
attack_waste = False
infi_timer_1 = 0
infi_timer_2 = 0
infi_timer_h = 0
infi_timer_m = 0
infi_timer_s = 0.0
total_attack = 0
enemy_list = []
attack_list = []
cavex = []
cavey = []
player = 0
player_Type = 'move'
player_state = 0
start_time = pygame.time.get_ticks()
tut_l = 0
#---------------------------------------------------------------------------------------------------
#reset
def intro():
    Button_state_reset()
    screen.blit(Intro_Background, (0, 0))
    
def menu():
    Button_state_reset()
    screen.blit(Menu_Background, (0, 0))
    Me_B_stage.draw()
    Me_B_infinite.draw()
    Me_B_setting.draw()

def set():
    Button_state_reset()
    screen.blit(Menu_Background, (0, 0))
    screen.blit(setting_ui, ((screen_W-1000)//2, (screen_L-500)//2))
    B_return.draw()
    bar_a.draw()
    bar_b.draw()
    bar_c.draw()
    S_B_init.draw()
    S_B_window_change.draw()
    
    master_sound_V = game_font.render(str(int(master_sound*100))+'/100',True, 'white')
    master_sound_V_rect = master_sound_V.get_rect()
    master_sound_V_rect.center = (454, 292)
    screen.blit(master_sound_V, master_sound_V_rect)

    bgm_sound_V = game_font.render(str(int(bgm_sound*100))+'/100',True, 'white')
    bgm_sound_V_rect = bgm_sound_V.get_rect()
    bgm_sound_V_rect.center = (454, 405)
    screen.blit(bgm_sound_V, bgm_sound_V_rect)

    effect_sound_V = game_font.render(str(int(effect_sound*100))+'/100',True, 'white')
    effect_sound_V_rect = effect_sound_V.get_rect()
    effect_sound_V_rect.center = (454, 522)
    screen.blit(effect_sound_V, effect_sound_V_rect)

    K_V_text = [pygame.font.Font(None, 40).render(i,True, 'black') for i in K_V]
    K_V_rect = [i.get_rect() for i in K_V_text]
    for i in range(11):
        K_V_rect[i].center = (821, 216 + (37.5*i))
    for i in range(11):
        S_B_key[i].state = S_B_key[i].N
        S_B_key[i].draw()
        screen.blit(K_V_text[i], K_V_rect[i])

def sest():
    Button_state_reset()
    screen.blit(Menu_Background, (0, 0))
    for i in range(10):
        Sest_B[i].draw()
    B_setting.draw()
    B_return.draw()
    star_V = []
    for i in range(10):
        star_V.append([Sest_B[i].rect.x, Sest_B[i].rect.x+53, Sest_B[i].rect.x+106, Sest_B[i].rect.y-25, star[i]])
    for i in range(10):
        if star_V[i][4] == 0:
            screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
            screen.blit(unfilled_star, (star_V[i][1], star_V[i][3]))
            screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
        elif star_V[i][4] == 1:
            screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
            screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
            screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
        elif star_V[i][4] == 2:
            screen.blit(filled_star, (star_V[i][0], star_V[i][3]+20))
            screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
            screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
        elif star_V[i][4] == 3:
            screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
            screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
            screen.blit(filled_star, (star_V[i][2], star_V[i][3]+20))
        elif star_V[i][4] == 4:
            screen.blit(filled_star, (star_V[i][0], star_V[i][3]+20))
            screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
            screen.blit(filled_star, (star_V[i][2], star_V[i][3]+20))
        
def sein():
    Button_state_reset()
    screen.blit(Menu_Background, (0, 0))
    for i in range(5):
        Sein_B[i].draw()
    B_setting.draw()
    B_return.draw()
    sein_text = []
    sein_text_rect = []
    for i in range(5):
        high_h = 0
        high_m = 0
        high_s = 0
        high_temp = high_time[i]
        while high_temp >= 3600:
            high_h += 1
            high_temp -= 3600
        while high_temp >= 60:
            high_m += 1
            high_temp -= 60
        high_s = high_temp
        sein_text.append(pygame.font.Font(None, 70).render(str(high_h)+':'+str(high_m)+':'+str(round(high_s, 3)),True, '#FFFFFF'))
        sein_text_rect.append(sein_text[i].get_rect())
        sein_text_rect[i].x, sein_text_rect[i].y = 700, Sein_B[i].rect.y+35
        screen.blit(sein_text[i], sein_text_rect[i])

def quit():
    Button_state_reset()
    screen.blit(quit_ui, ((screen_W-400)//2, (screen_L-250)//2))
    Q_B_quit.draw()
    Q_B_cancel.draw()

def ingame():
    global cavex, cavey, P_stage, P_stage_cave, enemy_list, attack_list, player, hp, start_time, P_type, infi_timer_1, infi_timer_2
    global P_summon_enemy, P_killed_enemy, attack_waste
    ingame_bgm.play(-1)
    enemy_list = []
    attack_list = []
    player = 0
    hp = 100
    P_summon_enemy = 0
    P_killed_enemy = 0
    attack_waste = False
    infi_timer_1 = 0
    infi_timer_2 = 0
    start_time = pygame.time.get_ticks()
    step_sound.play(-1)
    Button_state_reset()
    screen.fill((0, 0, 0))
    cavex = [random.randrange(-1280, 0) for _ in range(P_stage_cave)]
    if P_stage_cave % 2 == 0:
        cavey = [280, 360, 200, 440, 120, 520, 40, 600]
    else:
        cavey = [320, 240, 400, 160, 480, 80, 560, 0, 640]
    temp_cavey = [cavey[i] for i in range(P_stage_cave)]
    temp_cavey.sort()
    cavey = temp_cavey
    for i in range(P_stage_cave):
        screen.blit(cave, (cavex[i], cavey[i]))
    if P_type == 'infinite':
        infi_timer_1 = pygame.time.get_ticks()

def temp():
    Button_state_reset()
    screen.blit(temp_ui, ((screen_W-250)//2, (screen_L-400)//2))
    T_B_join.draw()
    T_B_restart.draw()
    T_B_main.draw()

def stage_result(temp_star):
    Button_state_reset()
    screen.blit(result_ui[temp_star], ((screen_W-1000)//2, (screen_L-500)//2))
    R_B_restart.draw()
    R_B_main.draw()
    stage_text = pygame.font.Font(None, 70).render('stage '+str(P_stage+1),True, '#000000')
    stage_text_rect = stage_text.get_rect()
    stage_text_rect.x, stage_text_rect.y = 300, 540
    screen.blit(stage_text, stage_text_rect)
    
def infinite_result(infi_r, h, m, s):
    Button_state_reset()
    global P_summon_enemy, P_killed_enemy, total_attack
    screen.blit(infinite_result_ui[infi_r], ((screen_W-1000)//2, (screen_L-500)//2))
    R_B_restart.draw()
    R_B_main.draw()

    infi_result_text_main = pygame.font.Font(None, 100).render(str(h)+':'+str(m)+':'+str(round(s, 3)),True, '#000000')
    infi_result_text_main_rect = infi_result_text_main.get_rect()
    infi_result_text_main_rect.x, infi_result_text_main_rect.y = 500, 150
    screen.blit(infi_result_text_main, infi_result_text_main_rect)


    infi_result_text_1 = pygame.font.Font(None, 70).render(str(total_attack),True, '#3F91B5')
    infi_result_text_1_rect = infi_result_text_1.get_rect()
    infi_result_text_1_rect.x, infi_result_text_1_rect.y = 320, 300
    screen.blit(infi_result_text_1, infi_result_text_1_rect)


    infi_result_text_2 = pygame.font.Font(None, 70).render(str(P_killed_enemy),True, '#3F91B5')
    infi_result_text_2_rect = infi_result_text_2.get_rect()
    infi_result_text_2_rect.x, infi_result_text_2_rect.y = 320, 380
    screen.blit(infi_result_text_2, infi_result_text_2_rect)


    infi_result_text_3 = pygame.font.Font(None, 70).render(str(P_summon_enemy), True, '#F03A17')
    infi_result_text_3_rect = infi_result_text_3.get_rect()
    infi_result_text_3_rect.x, infi_result_text_3_rect.y = 320, 460
    screen.blit(infi_result_text_3, infi_result_text_3_rect)

    if P_stage == 0:
        stage_text_text = 'easy'
    elif P_stage == 1:
        stage_text_text = 'normal'
    elif P_stage == 2:
        stage_text_text = 'hard'
    elif P_stage == 3:
        stage_text_text = 'expert'
    elif P_stage == 4:
        stage_text_text = 'master'
    stage_text = pygame.font.Font(None, 70).render(stage_text_text,True, '#000000')
    stage_text_rect = stage_text.get_rect()
    stage_text_rect.x, stage_text_rect.y = 320, 540
    screen.blit(stage_text, stage_text_rect)

def init():
    screen.blit(init_ui, ((screen_W-400)//2, (screen_L-250)//2))
    I_B_init.draw()
    Q_B_cancel.draw()
#-----------------------------------------------------------------------------------------------------
class enemy():
    def __init__(self, x, y, type):
        global cavey
        self.x = x
        self.y = y
        self.type = type
        self.state = 0
        if self.type == 1:
            self.img = enemy_b_move_img[0]
        else:
            self.img = enemy_b_move_img[0]
        self.y_pos = cavey[self.y]+12
        self.rect = pygame.Rect(self.x, self.y_pos, 37, 55)
    def update(self):
        if elapsed_time % (1*100) >= 0 and elapsed_time % (1*100) <= dt:
            if self.state == 5:
                self.state = 0
            else:
                self.state += 1
        if self.type == 1:
            self.img = enemy_a_move_img[self.state]
        else:
            self.img = enemy_b_move_img[self.state]
        self.rect.x = self.x
        screen.blit(self.img, self.rect)
        
class attack():
    def __init__(self, x, y, type):
        global cavey
        self.x = x
        self.y = y
        self.type = type
        if self.type == 1:
            self.img = attack_a_img
        else:
            self.img = attack_b_img
        self.y_pos = cavey[self.y]+13
        self.rect = pygame.Rect(self.x, self.y_pos, 24, 54)
    def update(self):
        self.rect.x = self.x
        screen.blit(self.img, self.rect)

def player_img(elapsed_time, dt):
    global player_move_img, player_state, player_Type
    if player_Type == 'move':
        if elapsed_time % (1*100) >= 0 and elapsed_time % (1*100) <= dt:
            if player_state == 5:
                player_state = 0 
            else:
                player_state += 1
        return player_move_img[player_state]
    if player_Type == 'attack':
        if elapsed_time % (1*150) >= 0 and elapsed_time % (1*150) <= dt:
            if player_state == 1:
                player_state -= 1
            else:
                player_Type = 'move'
                player_state = 1
                return player_move_img[1]
        return player_attack_img
        
#game
G_Play = True #G_Play == 게임 창 on/off 여부
G_Type = 'loading' #G_Type == 게임 창 종류
Temp_Type = ''
main_bgm.play(-1)
forbidden_key = [4, 5, 27, 127, 1073741882, 1073741893, 1073741884, 1073741885, 
                 1073741886, 1073741887, 1073741888, 1073741889, 1073741890, 
                 1073741891, 1073741892, 1073741893, 1073741894, 1073741895, 
                 1073741896, 1073741897, 1073741898, 1073741899, 1073741900, 
                 1073741901, 1073741902]
changing_key = -1
fullscreen = False
infi_r = 0
video_t = 0
while G_Play:
    dt = clock.tick(60)
    main_bgm.set_volume(master_sound*bgm_sound)
    ingame_bgm.set_volume(master_sound*bgm_sound)
    etc_bgm.set_volume(master_sound*bgm_sound)
    click_sound.set_volume(master_sound*effect_sound)
    banned_click_sound.set_volume(master_sound*effect_sound)
    cancel_sound.set_volume(master_sound*effect_sound)
    step_sound.set_volume(master_sound*effect_sound*0.2)
    sword_sound.set_volume(master_sound*effect_sound)
    for i in range(3):
        hit_sound[i].set_volume(master_sound*effect_sound)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit
            quit_Temp_Type = G_Type
            G_Type = 'quit'
            if quit_Temp_Type == 'Inplay':
                step_sound.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen == False:
                    screen = pygame.display.set_mode((screen_W, screen_L))
                else:
                    screen = pygame.display.set_mode((screen_W, screen_L), pygame.FULLSCREEN)
        
        if G_Type == 'quit':
            screen.blit(quit_ui, ((screen_W-400)//2, (screen_L-250)//2))
            Q_B_quit.draw()
            Q_B_cancel.draw()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    G_Type = quit_Temp_Type
                    if G_Type == 'Inplay':
                        step_sound.play(-1)
                    Q_B_quit.state = Q_B_quit.N
                    Q_B_cancel.state = Q_B_cancel.N
                if event.key == 13:
                    G_Play = False
            if event.type == pygame.MOUSEMOTION:
                if Q_B_quit.rect.collidepoint(event.pos):
                    Q_B_quit.state = Q_B_quit.H
                else:
                    Q_B_quit.state = Q_B_quit.N
                if Q_B_cancel.rect.collidepoint(event.pos):
                    Q_B_cancel.state = Q_B_cancel.H
                else:
                    Q_B_cancel.state = Q_B_cancel.N
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Q_B_quit.rect.collidepoint(event.pos):
                    click_sound.play()
                    G_Play = False
                if Q_B_cancel.rect.collidepoint(event.pos):
                    click_sound.play()
                    G_Type = quit_Temp_Type
                    if G_Type == 'Inplay':
                        step_sound.play(-1)
                    Q_B_quit.state = Q_B_quit.N
                    Q_B_cancel.state = Q_B_cancel.N

        elif G_Type == 'Intro':

            screen.blit(Intro_Background, (0, 0))
            
            if event.type == pygame.KEYDOWN:
                if event.key != 27:
                    if tut == 'True':
                        G_Type = "Menu"
                        menu()
                    else:
                        main_bgm.stop()
                        etc_bgm.play(-1)
                        G_Type = 'tut'
                elif event.key == 27:
                    quit_Temp_Type = G_Type
                    G_Type = 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tut == 'True':
                    G_Type = "Menu"
                    menu()
                else:
                    main_bgm.stop()
                    etc_bgm.play(-1)
                    G_Type = 'tut'

        elif G_Type == 'Menu':

            screen.blit(Menu_Background, (0, 0))
            Me_B_stage.draw()
            Me_B_infinite.draw()
            Me_B_setting.draw()

            if event.type == pygame.KEYUP:
                if event.key == 27:
                    G_Type = "Intro"
                    intro()
            elif event.type == pygame.MOUSEMOTION:
                if Me_B_infinite.rect.collidepoint(event.pos):
                    Me_B_infinite.state = Me_B_infinite.H
                else:
                    Me_B_infinite.state = Me_B_infinite.N
                if Me_B_stage.rect.collidepoint(event.pos):
                    Me_B_stage.state = Me_B_stage.H
                else:
                    Me_B_stage.state = Me_B_stage.N
                if Me_B_setting.rect.collidepoint(event.pos):
                    Me_B_setting.state = Me_B_setting.H
                else:
                    Me_B_setting.state = Me_B_setting.N
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Me_B_infinite.rect.collidepoint(event.pos):
                    G_Type = "Select_infinite"
                    click_sound.play()
                    sein()
                if Me_B_stage.rect.collidepoint(event.pos):
                    G_Type = "Select_stage"
                    click_sound.play()
                    sest()
                if Me_B_setting.rect.collidepoint(event.pos):
                    G_Type = "Set"
                    Temp_Type = "Menu"
                    click_sound.play()
                    set()
    
        elif G_Type == 'Set':

            screen.blit(Menu_Background, (0, 0))
            B_return.draw()
            screen.blit(setting_ui, ((screen_W-1000)//2, (screen_L-500)//2))
            bar_a.draw()
            bar_b.draw()
            bar_c.draw()
            S_B_init.draw()
            S_B_window_change.draw()

            master_sound_V = game_font.render(str(int(master_sound*100))+'/100',True, 'white')
            master_sound_V_rect = master_sound_V.get_rect()
            master_sound_V_rect.center = (454, 292)
            screen.blit(master_sound_V, master_sound_V_rect)

            bgm_sound_V = game_font.render(str(int(bgm_sound*100))+'/100',True, 'white')
            bgm_sound_V_rect = bgm_sound_V.get_rect()
            bgm_sound_V_rect.center = (454, 405)
            screen.blit(bgm_sound_V, bgm_sound_V_rect)

            effect_sound_V = game_font.render(str(int(effect_sound*100))+'/100',True, 'white')
            effect_sound_V_rect = effect_sound_V.get_rect()
            effect_sound_V_rect.center = (454, 522)
            screen.blit(effect_sound_V, effect_sound_V_rect)
            
            K_V_text = [pygame.font.Font(None, 40).render(i,True, 'black') for i in K_V]
            K_V_rect = [i.get_rect() for i in K_V_text]
            for i in range(11):
                K_V_rect[i].center = (821, 216 + (37.5*i))
            for i in range(11):
                S_B_key[i].draw()
                screen.blit(K_V_text[i], K_V_rect[i])

            if changing_key != -1:
                if event.type == pygame.KEYDOWN:
                    if not event.key in K and not event.key in forbidden_key:
                        K[changing_key] = event.key
                        K_V[changing_key] = pygame.key.name(event.key)
                    changing_key = -1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not event.button in K and not event.button in forbidden_key:
                        K[changing_key] = event.button
                        if event.button == 1:
                            K_V[changing_key] = 'L click'
                        elif event.button == 2:
                            K_V[changing_key] = 'W Click'
                        elif event.button == 3:
                            K_V[changing_key] = 'R Click'
                        elif event.button == 6:
                            K_V[changing_key] = 'S1 Click'
                        elif event.button == 7:
                            K_V[changing_key] = 'S2 Click'
                    changing_key = -1
            else:
                if event.type == pygame.KEYUP:
                    if event.key == 27:
                        G_Type = Temp_Type
                        Temp_Type = ''
                        if G_Type == 'Menu':
                            menu()
                        elif G_Type == "Select_stage":
                            sest()
                        elif G_Type == 'Select_infinite':
                            sein()
                elif event.type == pygame.MOUSEMOTION:
                    if B_return.rect.collidepoint(event.pos):
                        B_return.state = B_return.H
                    else:
                        B_return.state = B_return.N
                    if S_B_window_change.rect.collidepoint(event.pos):
                        S_B_window_change.state = S_B_window_change.H
                    else:
                        S_B_window_change.state = S_B_window_change.N
                    if S_B_init.rect.collidepoint(event.pos):
                        S_B_init.state = S_B_init.H
                    else:
                        S_B_init.state = S_B_init.N
                    for i in range(11):
                        if S_B_key[i].rect.collidepoint(event.pos):
                            S_B_key[i].state = S_B_key[i].H
                        else:
                            S_B_key[i].state = S_B_key[i].N
                    if bar_a.drag == True:
                        bar_a.move(event)
                        master_sound = (bar_a.x-304)/300
                    if bar_b.drag == True:
                        bar_b.move(event)
                        bgm_sound = (bar_b.x-304)/300
                    if bar_c.drag == True:
                        bar_c.move(event)
                        effect_sound = (bar_c.x-304)/300
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in range(11):
                        if S_B_key[i].rect.collidepoint(event.pos):
                            changing_key = i
                            click_sound.play()
                    if S_B_window_change.rect.collidepoint(event.pos):
                        click_sound.play()
                        if fullscreen:
                            S_B_window_change.N = S_B_window_N
                            S_B_window_change.H = S_B_window_H
                            S_B_window_change.state = S_B_window_H
                        if not fullscreen:
                            S_B_window_change.N = S_B_full_N
                            S_B_window_change.H = S_B_full_H
                            S_B_window_change.state = S_B_full_H
                        fullscreen = not fullscreen
                        if fullscreen == False:
                            screen = pygame.display.set_mode((screen_W, screen_L))
                        else:
                            screen = pygame.display.set_mode((screen_W, screen_L), pygame.FULLSCREEN)
                    if S_B_init.rect.collidepoint(event.pos):
                        G_Type = 'Init'
                        click_sound.play()
                        init()
                    if B_return.rect.collidepoint(event.pos):
                        G_Type = Temp_Type
                        click_sound.play()
                        Temp_Type = ''
                        if G_Type == 'Menu':
                            menu()
                        elif G_Type == "Select_stage":
                            sest()
                        elif G_Type == 'Select_infinite':
                            sein()
                    if event.pos[1] >= 262 and event.pos[1] <= 321:
                        bar_a.move(event)
                        click_sound.play()
                        master_sound = (bar_a.x-304)/300
                    if event.pos[1] >= 375 and event.pos[1] <= 434:
                        bar_b.move(event)
                        click_sound.play()
                        bgm_sound = (bar_b.x-304)/300
                    if event.pos[1] >= 492 and event.pos[1] <= 551:
                        bar_c.move(event)
                        click_sound.play()
                        effect_sound = (bar_c.x-304)/300
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    if bar_a.drag == True:
                        bar_a.drag = False
                        master_sound = (bar_a.x-304)/300
                    if bar_b.drag == True:
                        bar_b.drag = False
                        bgm_sound = (bar_b.x-304)/300
                    if bar_c.drag == True:
                        bar_c.drag = False
                        effect_sound = (bar_c.x-304)/300
            
        elif G_Type == 'Select_stage':

            screen.blit(Menu_Background, (0, 0))
            for i in range(10):
                Sest_B[i].draw()
            B_setting.draw()
            B_return.draw()
            star_V = []
            for i in range(10):
                star_V.append([Sest_B[i].rect.x, Sest_B[i].rect.x+53, Sest_B[i].rect.x+106, Sest_B[i].rect.y-25, star[i]])
            for i in range(10):
                if star_V[i][4] == 0:
                    screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
                    screen.blit(unfilled_star, (star_V[i][1], star_V[i][3]))
                    screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
                elif star_V[i][4] == 1:
                    screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
                    screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
                    screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
                elif star_V[i][4] == 2:
                    screen.blit(filled_star, (star_V[i][0], star_V[i][3]+20))
                    screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
                    screen.blit(unfilled_star, (star_V[i][2], star_V[i][3]+20))
                elif star_V[i][4] == 3:
                    screen.blit(unfilled_star, (star_V[i][0], star_V[i][3]+20))
                    screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
                    screen.blit(filled_star, (star_V[i][2], star_V[i][3]+20))
                elif star_V[i][4] == 4:
                    screen.blit(filled_star, (star_V[i][0], star_V[i][3]+20))
                    screen.blit(filled_star, (star_V[i][1], star_V[i][3]))
                    screen.blit(filled_star, (star_V[i][2], star_V[i][3]+20))
                
            
            if event.type == pygame.KEYUP:
                if event.key == 27:
                    G_Type = "Menu"
                    menu()
            elif event.type == pygame.MOUSEMOTION:
                for i in range(10):
                    if Sest_B[i].rect.collidepoint(event.pos):
                        Sest_B[i].state = Sest_B[i].H
                    else:
                        Sest_B[i].state = Sest_B[i].N
                if B_setting.rect.collidepoint(event.pos):
                    B_setting.state = B_setting.H
                else:
                    B_setting.state = B_setting.N
                if B_return.rect.collidepoint(event.pos):
                    B_return.state = B_return.H
                else:
                    B_return.state = B_return.N
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if B_setting.rect.collidepoint(event.pos):
                    G_Type = "Set"
                    Temp_Type = "Select_stage"
                    click_sound.play()
                    set()
                
                if B_return.rect.collidepoint(event.pos):
                    G_Type = "Menu"
                    click_sound.play()
                    menu()
                for i in range(10):
                    if Sest_B[i].rect.collidepoint(event.pos):
                        if stage >= i:
                            click_sound.play()
                            G_Type = "Inplay"
                            P_stage = i
                            P_type = 'stage'
                            P_stage_attack = stage_attack[P_stage]
                            P_stage_cave = stage_cave[P_stage]
                            P_stage_damage = stage_damage[P_stage]
                            P_stage_enemy = stage_enemy[P_stage]
                            P_stage_speed = stage_speed[P_stage]
                            P_stage_time = stage_time[P_stage]
                            main_bgm.stop()
                            ingame()
                        else:
                            banned_click_sound.play()

        elif G_Type == 'Select_infinite':

            screen.blit(Menu_Background, (0, 0))
            for i in  range(5):
                Sein_B[i].draw()
            B_setting.draw()
            B_return.draw()
            sein_text = []
            sein_text_rect = []
            for i in range(5):
                high_h = 0
                high_m = 0
                high_s = 0
                high_temp = high_time[i]
                while high_temp >= 3600:
                    high_h += 1
                    high_temp -= 3600
                while high_temp >= 60:
                    high_m += 1
                    high_temp -= 60
                high_s = high_temp
                sein_text.append(pygame.font.Font(None, 70).render(str(high_h)+':'+str(high_m)+':'+str(round(high_s, 3)),True, '#FFFFFF'))
                sein_text_rect.append(sein_text[i].get_rect())
                sein_text_rect[i].x, sein_text_rect[i].y = 700, Sein_B[i].rect.y+35
                screen.blit(sein_text[i], sein_text_rect[i])
            
            if event.type == pygame.KEYUP:
                if event.key == 27:
                    G_Type = "Menu"
                    menu()
            elif event.type == pygame.MOUSEMOTION:
                for i in range(5):
                    if Sein_B[i].rect.collidepoint(event.pos):
                        Sein_B[i].state = Sein_B[i].H
                    else:
                        Sein_B[i].state = Sein_B[i].N
                if B_setting.rect.collidepoint(event.pos):
                    B_setting.state = B_setting.H
                else:
                    B_setting.state = B_setting.N
                if B_return.rect.collidepoint(event.pos):
                    B_return.state = B_return.H
                else:
                    B_return.state = B_return.N
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if B_setting.rect.collidepoint(event.pos):
                    G_Type = "Set"
                    Temp_Type = "Select_infinite"
                    click_sound.play()
                    set()
                if B_return.rect.collidepoint(event.pos):
                    G_Type = "Menu"
                    click_sound.play()
                    menu()
                for i in range(5):
                    if Sein_B[i].rect.collidepoint(event.pos):
                        click_sound.play()
                        G_Type = "Inplay"
                        P_stage = i
                        P_type = 'infinite'
                        P_infinite_attack = infinite_attack[P_stage]
                        P_stage_attack = 10
                        P_stage_cave = infinite_cave[P_stage]
                        P_stage_damage = infinite_damage[P_stage]
                        P_stage_speed = infinite_speed[P_stage]
                        P_stage_time = infinite_time[P_stage]
                        main_bgm.stop()
                        ingame()
                    
        elif G_Type == 'Inplay':
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    G_Type = "Temp"
                    step_sound.stop()
                    temp()
                for i in range(9):
                    if event.key == K[i]:
                        if P_stage_cave > i:
                            player = i
                if event.key == K[9]:
                    if P_stage_attack > 0:
                        sword_sound.play()
                        attack_list.append(attack(150, player, 1))
                        P_stage_attack -= 1
                        player_Type = 'attack'
                        total_attack += 1
                        player_state = 1
                if event.key == K[10]:
                    if P_stage_attack > 0:
                        sword_sound.play()
                        attack_list.append(attack(150, player, 2))
                        P_stage_attack -= 1
                        player_Type = 'attack'
                        total_attack += 1
                        player_state = 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(9):
                    if event.button == K[i]:
                        if P_stage_cave > i:
                            player = i
                if event.button == K[9]:
                    if P_stage_attack > 0:
                        sword_sound.play()
                        attack_list.append(attack(150, player, 1))
                        P_stage_attack -= 1
                        player_Type = 'attack'
                        player_state = 1
                        total_attack += 1
                if event.button == K[10]:
                    if P_stage_attack > 0:
                        sword_sound.play()
                        attack_list.append(attack(150, player, 2))
                        P_stage_attack -= 1
                        player_Type = 'attack'
                        player_state = 1
                        total_attack += 1
                if event.button == 5:
                    if player < P_stage_cave-1:
                        player += 1
                if event.button == 4:
                    if player > 0:
                        player -= 1
        
        elif G_Type == 'tut':
            if tut_l == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        G_Type = 'Intro'
                        etc_bgm.stop()
                        main_bgm.play(-1)
                        intro()
                    if event.key == 13:
                        video_t = 40
                elif event.type == pygame.MOUSEMOTION:
                    if T_B_skip.rect.collidepoint(event.pos):
                        T_B_skip.state = T_B_skip.H
                    else:
                        T_B_skip.state = T_B_skip.N
                    if T_B_undo.rect.collidepoint(event.pos):
                        T_B_undo.state = T_B_undo.H
                    else:
                        T_B_undo.state = T_B_undo.N
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if T_B_skip.rect.collidepoint(event.pos):
                        video_t = 40
                        click_sound.play()
                    if T_B_undo.rect.collidepoint(event.pos):
                        G_Type = 'Intro'
                        etc_bgm.stop()
                        main_bgm.play(-1)
                        intro()
                        click_sound.play()
            if 1 <= tut_l and tut_l <= 5:
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        if tut_l == 5:
                            step_sound.play(-1)
                            etc_bgm.stop()
                            ingame_bgm.play(-1)
                        tut_l += 1
                    if event.key == pygame.K_BACKSPACE:
                        if tut_l == 1:
                            video_t = 0
                        tut_l -= 1
                elif event.type == pygame.MOUSEMOTION:
                    if T_B_undo.rect.collidepoint(event.pos):
                        T_B_undo.state = T_B_undo.H
                    else:
                        T_B_undo.state = T_B_undo.N
                    if T_B_next.rect.collidepoint(event.pos):
                        T_B_next.state = T_B_next.H
                    else:
                        T_B_next.state = T_B_next.N
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if T_B_next.rect.collidepoint(event.pos):
                        if tut_l == 5:
                            step_sound.play(-1)
                            etc_bgm.stop()
                            ingame_bgm.play(-1)
                        tut_l += 1
                        click_sound.play()
                    if T_B_undo.rect.collidepoint(event.pos):
                        if tut_l == 1:
                            video_t = 0
                        tut_l -= 1
                        click_sound.play()
            elif tut_l == 6:
                if event.type == pygame.KEYDOWN:
                    for i in range(9):
                        if event.key == K[i]:
                            if P_stage_cave > i:
                                player = i
                    if event.key == K[9]:
                        if P_stage_attack > 0:
                            sword_sound.play()
                            attack_list.append(attack(150, player, 1))
                            P_stage_attack -= 1
                            player_Type = 'attack'
                            total_attack += 1
                            player_state = 1
                    if event.key == K[10]:
                        if P_stage_attack > 0:
                            sword_sound.play()
                            attack_list.append(attack(150, player, 2))
                            P_stage_attack -= 1
                            player_Type = 'attack'
                            total_attack += 1
                            player_state = 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(9):
                        if event.button == K[i]:
                            if P_stage_cave > i:
                                player = i
                    if event.button == K[9]:
                        if P_stage_attack > 0:
                            sword_sound.play()
                            attack_list.append(attack(150, player, 1))
                            P_stage_attack -= 1
                            player_Type = 'attack'
                            player_state = 1
                            total_attack += 1
                    if event.button == K[10]:
                        if P_stage_attack > 0:
                            sword_sound.play()
                            attack_list.append(attack(150, player, 2))
                            P_stage_attack -= 1
                            player_Type = 'attack'
                            player_state = 1
                            total_attack += 1
                    if event.button == 5:
                        if player < P_stage_cave-1:
                            player += 1
                    if event.button == 4:
                        if player > 0:
                            player -= 1

        elif G_Type == 'Temp':
            screen.blit(temp_ui, ((screen_W-250)//2, (screen_L-400)//2))
            T_B_join.draw()
            T_B_restart.draw()
            T_B_main.draw()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    G_Type = 'Inplay'
                    step_sound.play(-1)
                    T_B_join.state = T_B_join.N
                    T_B_restart.state = T_B_restart.N
                    T_B_main.state = T_B_main.N
            if event.type == pygame.MOUSEMOTION:
                if T_B_join.rect.collidepoint(event.pos):
                    T_B_join.state = T_B_join.H
                else:
                    T_B_join.state = T_B_join.N
                if T_B_restart.rect.collidepoint(event.pos):
                    T_B_restart.state = T_B_restart.H
                else:
                    T_B_restart.state = T_B_restart.N
                if T_B_main.rect.collidepoint(event.pos):
                    T_B_main.state = T_B_main.H
                else:
                    T_B_main.state = T_B_main.N
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if T_B_join.rect.collidepoint(event.pos):
                    click_sound.play()
                    G_Type = 'Inplay'
                    step_sound.play(-1)
                    T_B_join.state = T_B_join.N
                    T_B_restart.state = T_B_restart.N
                    T_B_main.state = T_B_main.N
                if T_B_restart.rect.collidepoint(event.pos):
                    click_sound.play()
                    if P_type == 'stage':
                        P_stage_attack = stage_attack[P_stage]
                        P_stage_cave = stage_cave[P_stage]
                        P_stage_damage = stage_damage[P_stage]
                        P_stage_enemy = stage_enemy[P_stage]
                        P_stage_speed = stage_speed[P_stage]
                        P_stage_time = stage_time[P_stage]
                    if P_type == 'infinite':
                        P_infinite_attack = infinite_attack[P_stage]
                        P_stage_attack = 10
                        P_stage_cave = infinite_cave[P_stage]
                        P_stage_damage = infinite_damage[P_stage]
                        P_stage_speed = infinite_speed[P_stage]
                        P_stage_time = infinite_time[P_stage]
                    ingame()
                    step_sound.play(-1)
                    G_Type = 'Inplay'
                if T_B_main.rect.collidepoint(event.pos):
                    click_sound.play()
                    G_Type = 'Menu'
                    ingame_bgm.stop()
                    main_bgm.play(-1)
                    menu()
        
        elif G_Type == 'Infinite_Result':
            screen.blit(infinite_result_ui[infi_r], ((screen_W-1000)//2, (screen_L-500)//2))
            R_B_restart.draw()
            R_B_main.draw()
            if P_stage == 0:
                stage_text_text = 'easy'
            elif P_stage == 1:
                stage_text_text = 'normal'
            elif P_stage == 2:
                stage_text_text = 'hard'
            elif P_stage == 3:
                stage_text_text = 'expert'
            elif P_stage == 4:
                stage_text_text = 'impossible'
            stage_text = pygame.font.Font(None, 70).render(stage_text_text,True, '#000000')
            stage_text_rect = stage_text.get_rect()
            stage_text_rect.x, stage_text_rect.y = 320, 540
            screen.blit(stage_text, stage_text_rect)

            infi_result_text_main = pygame.font.Font(None, 100).render(str(infi_timer_h)+':'+str(infi_timer_m)+':'+str(round(infi_timer_s, 3)),True, '#000000')
            infi_result_text_main_rect = infi_result_text_main.get_rect()
            infi_result_text_main_rect.x, infi_result_text_main_rect.y = 500, 150
            screen.blit(infi_result_text_main, infi_result_text_main_rect)


            infi_result_text_1 = pygame.font.Font(None, 70).render(str(total_attack),True, '#3F91B5')
            infi_result_text_1_rect = infi_result_text_1.get_rect()
            infi_result_text_1_rect.x, infi_result_text_1_rect.y = 320, 300
            screen.blit(infi_result_text_1, infi_result_text_1_rect)


            infi_result_text_2 = pygame.font.Font(None, 70).render(str(P_killed_enemy),True, '#3F91B5')
            infi_result_text_2_rect = infi_result_text_2.get_rect()
            infi_result_text_2_rect.x, infi_result_text_2_rect.y = 320, 380
            screen.blit(infi_result_text_2, infi_result_text_2_rect)


            infi_result_text_3 = pygame.font.Font(None, 70).render(str(P_summon_enemy),True, '#F03A17')
            infi_result_text_3_rect = infi_result_text_3.get_rect()
            infi_result_text_3_rect.x, infi_result_text_3_rect.y = 320, 460
            screen.blit(infi_result_text_3, infi_result_text_3_rect)

            if event.type == pygame.MOUSEMOTION:
                if R_B_restart.rect.collidepoint(event.pos):
                    R_B_restart.state = R_B_restart.H
                else:
                    R_B_restart.state = R_B_restart.N
                if R_B_main.rect.collidepoint(event.pos):
                    R_B_main.state = R_B_main.H
                else:
                    R_B_main.state = R_B_main.N
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if R_B_restart.rect.collidepoint(event.pos):
                    click_sound.play()
                    P_infinite_attack = infinite_attack[P_stage]
                    P_stage_attack = 10
                    P_stage_cave = infinite_cave[P_stage]
                    P_stage_damage = infinite_damage[P_stage]
                    P_stage_speed = infinite_speed[P_stage]
                    P_stage_time = infinite_time[P_stage]
                    ingame_bgm.stop()
                    ingame()
                    G_Type = 'Inplay'
                if R_B_main.rect.collidepoint(event.pos):
                    click_sound.play()
                    G_Type = 'Menu'
                    ingame_bgm.stop()
                    main_bgm.play(-1)
                    menu()

        elif G_Type == 'Stage_Result':
            screen.blit(result_ui[temp_star], ((screen_W-1000)//2, (screen_L-500)//2))
            R_B_restart.draw()
            R_B_main.draw()
            stage_text = pygame.font.Font(None, 70).render('stage '+str(P_stage+1),True, '#000000')
            stage_text_rect = stage_text.get_rect()
            stage_text_rect.x, stage_text_rect.y = 300, 540
            screen.blit(stage_text, stage_text_rect)

            if event.type == pygame.MOUSEMOTION:
                if R_B_restart.rect.collidepoint(event.pos):
                    R_B_restart.state = R_B_restart.H
                else:
                    R_B_restart.state = R_B_restart.N
                if R_B_main.rect.collidepoint(event.pos):
                    R_B_main.state = R_B_main.H
                else:
                    R_B_main.state = R_B_main.N
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if R_B_restart.rect.collidepoint(event.pos):
                    click_sound.play()
                    P_stage_attack = stage_attack[P_stage]
                    P_stage_cave = stage_cave[P_stage]
                    P_stage_damage = stage_damage[P_stage]
                    P_stage_enemy = stage_enemy[P_stage]
                    P_stage_speed = stage_speed[P_stage]
                    P_stage_time = stage_time[P_stage]
                    ingame_bgm.stop()
                    ingame()
                    G_Type = 'Inplay'
                if R_B_main.rect.collidepoint(event.pos):
                    click_sound.play()
                    if stage == 10 and ending == 'False':
                        ingame_bgm.stop()
                        video_t = 0
                        ending = 'True'
                        G_Type = 'ending'
                        etc_bgm.play()
                    else:
                        G_Type = 'Menu'
                        ingame_bgm.stop()
                        main_bgm.play(-1)
                    menu()

        elif G_Type == 'Init':
            screen.blit(init_ui, ((screen_W-400)//2, (screen_L-250)//2))
            I_B_init.draw()
            Q_B_cancel.draw()
            if event.type == pygame.KEYUP:
                if event.key == 27:
                    G_Type = 'Set'
                    set()
                if event.key == 13:
                    tut = False
                    stage = 0
                    for i in range(10):
                        star[i] = 0
                    for i in range(5):
                        high_time[i] = 0.0
                    G_Play = False
            elif event.type == pygame.MOUSEMOTION:
                if I_B_init.rect.collidepoint(event.pos):
                    I_B_init.state = I_B_init.H
                else:
                    I_B_init.state = I_B_init.N
                if Q_B_cancel.rect.collidepoint(event.pos):
                    Q_B_cancel.state = Q_B_cancel.H
                else:
                    Q_B_cancel.state = Q_B_cancel.N
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if I_B_init.rect.collidepoint(event.pos):
                    click_sound.play()
                    tut = 'False'
                    stage = 0
                    for i in range(10):
                        star[i] = 0
                    for i in range(5):
                        high_time[i] = 0.0
                    ending = 'False'
                    G_Play = False
                if Q_B_cancel.rect.collidepoint(event.pos):
                    G_Type = 'Set'
                    click_sound.play()
                    set()

        elif G_Type == 'ending':
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    if video_t < 12:
                        video_t = 12
                    else:
                        video_t = 39.9
            elif event.type == pygame.MOUSEMOTION:
                if T_B_skip.rect.collidepoint(event.pos):
                    T_B_skip.state = T_B_skip.H
                else:
                    T_B_skip.state = T_B_skip.N
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if T_B_skip.rect.collidepoint(event.pos):
                    if video_t < 12:
                        video_t = 12
                    else:
                        video_t = 39.9
                    click_sound.play()
                
    if G_Type == 'Inplay':
        screen.fill((0, 0, 0))
        elapsed_time = pygame.time.get_ticks() - start_time
        if P_type == 'infinite':
            infi_timer_2 = (pygame.time.get_ticks() - infi_timer_1)/1000
            temp_infi_timer = infi_timer_2
            infi_timer_h = 0
            infi_timer_m = 0
            infi_timer_s = 0
            while temp_infi_timer >= 3600:
                infi_timer_h += 1
                temp_infi_timer -= 3600
            while temp_infi_timer >= 60:
                infi_timer_m += 1
                temp_infi_timer -= 60
            infi_timer_s = temp_infi_timer
        #cave
        cavex = [i-1 for i in cavex]
        cavex2 = [i+2559 for i in cavex]
        for i in range(len(cavex)):
            if cavex[i] < -2560:
                cavex[i] = 0
        for i in range(P_stage_cave):
            screen.blit(cave, (cavex[i], cavey[i]))
            screen.blit(cave, (cavex2[i], cavey[i]))
        screen.blit(ingame_ui, (0,0))

        hp_text = pygame.font.Font(None, 30).render(str(int(hp))+'/100',True, '#FC5230')
        hp_text_rect = hp_text.get_rect()
        hp_text_rect.center = (50, 130)
        screen.blit(hp_text, hp_text_rect)

        if P_type == 'stage':
            attack_text = pygame.font.Font(None, 30).render(str(int(P_stage_attack))+'/'+str(int(stage_attack[P_stage])),True, '#3F91B5')
            enemy_text = pygame.font.Font(None, 30).render(str(int(P_stage_enemy))+'/'+str(int(stage_enemy[P_stage])),True, '#F03A17')
        else:
            attack_text = pygame.font.Font(None, 30).render(str(int(P_stage_attack)),True, '#3F91B5')
            attack_text_i = pygame.font.Font(None, 20).render('(+'+str(int(infinite_attack[P_stage]))+'attack/kill)',True, '#3F91B5')
            enemy_text = pygame.font.Font(None, 30).render(str(int(P_killed_enemy))+'/'+str(int(P_summon_enemy)),True, '#F03A17')
            infi_timer_text = pygame.font.Font(None, 30).render(str(infi_timer_h)+':'+str(infi_timer_m)+':'+str(round(infi_timer_s, 1)),True, '#FFFFFF')
            attack_text_i_rect = attack_text_i.get_rect()
            attack_text_i_rect.center = (50, 400)
            infi_timer_text_rect = infi_timer_text.get_rect()
            infi_timer_text_rect.center = (50, 670)
            screen.blit(infi_timer_text, infi_timer_text_rect)
            screen.blit(attack_text_i, attack_text_i_rect)
        attack_text_rect = attack_text.get_rect()
        attack_text_rect.center = (50, 380)

        enemy_text_rect = enemy_text.get_rect()
        enemy_text_rect.center = (50, 600)
        screen.blit(attack_text, attack_text_rect)
        screen.blit(enemy_text, enemy_text_rect)

        if elapsed_time > dt and elapsed_time % (P_stage_time*1000) >= 0 and elapsed_time % (P_stage_time*1000) < dt-1:
            if P_type == 'stage' and P_stage_enemy > 0:
                P_stage_enemy -= 1
                e = random.choice([1, 2])
                s = random.randrange(0, P_stage_cave)
                enemy_list.append(enemy(1280, s, e))
                P_summon_enemy += 1
            elif P_type == 'infinite':
                e = random.choice([1, 2])
                s = random.randrange(0, P_stage_cave)
                enemy_list.append(enemy(1280, s, e))
                P_summon_enemy += 1

        temp_enemy_list = [i for i in enemy_list if i.x > 150]
        hp -= P_stage_damage*(len(enemy_list)-len(temp_enemy_list))
        if len(enemy_list)!=len(temp_enemy_list):
            random.choice(hit_sound).play()
        enemy_list = temp_enemy_list

        temp_attack_list = [i for i in attack_list if i.x < 1200]
        if len(attack_list) != len(temp_attack_list):
            attack_waste = True
        attack_list = temp_attack_list

        screen.blit(player_img(elapsed_time, dt), (150, cavey[player]+12))

        for i in temp_attack_list:
            for j in temp_enemy_list:
                if j.rect.colliderect(i.rect):
                    if i.type == j.type:
                        try:
                            attack_list.remove(i)
                        except:
                            pass
                        try:
                            enemy_list.remove(j)
                        except:
                            pass
                        if P_type == 'infinite':
                            P_stage_attack += P_infinite_attack
                        P_killed_enemy += 1
                    else:
                        try:
                            attack_list.remove(i)
                            attack_waste = True
                        except:
                            pass

        #게임 오버
        if hp <= 0:
            if P_type == 'stage':
                temp_star = 0
                stage_result(temp_star)
                step_sound.stop()
                G_Type = 'Stage_Result'
                continue
            else:
                if high_time[P_stage] >= infi_timer_2:
                    infi_r = 0
                else:
                    high_time[P_stage] = infi_timer_2
                    infi_r = 1
                step_sound.stop()
                G_Type = 'Infinite_Result'
                infinite_result(infi_r, infi_timer_h, infi_timer_m, infi_timer_s)
                continue
        #stage clear
        if P_type == 'stage' and hp > 0 and len(enemy_list) == 0 and P_stage_enemy <= 0:
            temp_star = 1
            if hp == 100:
                temp_star = 2
                if attack_waste == False and len(attack_list) == 0:
                    temp_star = 4
            elif attack_waste == False and len(attack_list) == 0:
                temp_star = 3
            if star[P_stage] < temp_star:
                star[P_stage] = temp_star
            if stage <= P_stage:
                stage = P_stage+1
            step_sound.stop()
            if stage != 10:
                Sest_B[stage].N = pygame.image.load('data/img/ui/button_sest_{0}_normal.png'.format(stage+1))
                Sest_B[stage].H = pygame.image.load('data/img/ui/button_sest_{0}_hover.png'.format(stage+1))
            G_Type = 'Stage_Result'
            stage_result(temp_star)
            continue
        
        for i in range(len(attack_list)):
            attack_list[i].x += 5
            attack_list[i].update()
        for i in range(len(enemy_list)):
            enemy_list[i].x -= (P_stage_speed*dt)/1000
            enemy_list[i].update()
                    
    if G_Type == 'loading':
        G_Type = 'Intro'
        intro()
    
    if G_Type == 'tut':
        if tut_l == 0:
            screen.blit(getSurface(video_t, tut_intro_video, surface), (0, 0))
            T_B_skip.draw()
            T_B_undo.draw()
            pygame.display.flip()
            video_t += 1/60
            if video_t >= 40:
                tut_l = 1
                P_stage = 0
                P_type = 'tut'
                P_stage_attack = 999
                P_stage_cave = 2
                P_stage_enemy = 3
                P_stage_damage = 1
                P_stage_speed = 70
                P_stage_time = 10
                enemy_list = []
                attack_list = []
                player = 0
                hp = 100
                P_summon_enemy = 0
                P_killed_enemy = 0
                attack_waste = False
                infi_timer_1 = 0
                infi_timer_2 = 0
                start_time = pygame.time.get_ticks()
                Button_state_reset()
                screen.fill((0, 0, 0))
                cavex = [random.randrange(-1280, 0) for _ in range(P_stage_cave)]
                if P_stage_cave % 2 == 0:
                    cavey = [280, 360, 200, 440, 120, 520, 40, 600]
                else:
                    cavey = [320, 240, 400, 160, 480, 80, 560, 0, 640]
                temp_cavey = [cavey[i] for i in range(P_stage_cave)]
                temp_cavey.sort()
                cavey = temp_cavey
                for i in range(P_stage_cave):
                    screen.blit(cave, (cavex[i], cavey[i]))
                screen.blit(ingame_ui, (0,0))
                hp_text = pygame.font.Font(None, 30).render(str(int(hp))+'/100',True, '#FC5230')
                hp_text_rect = hp_text.get_rect()
                hp_text_rect.center = (50, 130)
                screen.blit(hp_text, hp_text_rect)

                attack_text = pygame.font.Font(None, 30).render(str(int(P_stage_attack))+'/'+str(int(999)),True, '#3F91B5')
                enemy_text = pygame.font.Font(None, 30).render(str(int(P_stage_enemy))+'/'+str(int(3)),True, '#F03A17')
                attack_text_rect = attack_text.get_rect()
                attack_text_rect.center = (50, 380)

                enemy_text_rect = enemy_text.get_rect()
                enemy_text_rect.center = (50, 600)
                screen.blit(attack_text, attack_text_rect)
                screen.blit(enemy_text, enemy_text_rect)
                screen.blit(pygame.image.load('data/img/objective/player/player.png'), (150, cavey[0]+12))
        if 1 <= tut_l and tut_l <= 5:
            screen.fill((0, 0, 0))
            for i in range(P_stage_cave):
                screen.blit(cave, (cavex[i], cavey[i]))
            screen.blit(ingame_ui, (0,0))
            screen.blit(hp_text, hp_text_rect)
            screen.blit(attack_text, attack_text_rect)
            screen.blit(enemy_text, enemy_text_rect)
            screen.blit(pygame.image.load('data/img/objective/player/player.png'), (150, cavey[0]+12))
            screen.blit(tut_ui[tut_l-1], (0,0))
            T_B_next.draw()
            T_B_undo.draw()
        if tut_l == 6:
            screen.fill((0, 0, 0))
            elapsed_time = pygame.time.get_ticks() - start_time
            #cave
            cavex = [i-1 for i in cavex]
            cavex2 = [i+2559 for i in cavex]
            for i in range(len(cavex)):
                if cavex[i] < -2560:
                    cavex[i] = 0
            for i in range(P_stage_cave):
                screen.blit(cave, (cavex[i], cavey[i]))
                screen.blit(cave, (cavex2[i], cavey[i]))
            screen.blit(ingame_ui, (0,0))

            hp_text = pygame.font.Font(None, 30).render(str(int(hp))+'/100',True, '#FC5230')
            hp_text_rect = hp_text.get_rect()
            hp_text_rect.center = (50, 130)
            screen.blit(hp_text, hp_text_rect)
            
            attack_text = pygame.font.Font(None, 30).render(str(int(P_stage_attack))+'/'+str(int(999)),True, '#3F91B5')
            enemy_text = pygame.font.Font(None, 30).render(str(int(P_stage_enemy))+'/'+str(int(3)),True, '#F03A17')
            attack_text_rect = attack_text.get_rect()
            attack_text_rect.center = (50, 380)

            enemy_text_rect = enemy_text.get_rect()
            enemy_text_rect.center = (50, 600)
            screen.blit(attack_text, attack_text_rect)
            screen.blit(enemy_text, enemy_text_rect)

            if elapsed_time > dt and elapsed_time % (P_stage_time*1000) >= 0 and elapsed_time % (P_stage_time*1000) < dt-1:
                if P_stage_enemy > 0:
                    P_stage_enemy -= 1
                    e = random.choice([1, 2])
                    s = random.randrange(0, P_stage_cave)
                    enemy_list.append(enemy(1280, s, e))
                    P_summon_enemy += 1

            temp_enemy_list = [i for i in enemy_list if i.x > 150]
            hp -= P_stage_damage*(len(enemy_list)-len(temp_enemy_list))
            if len(enemy_list)!=len(temp_enemy_list):
                random.choice(hit_sound).play()
            enemy_list = temp_enemy_list

            temp_attack_list = [i for i in attack_list if i.x < 1200]
            if len(attack_list) != len(temp_attack_list):
                attack_waste = True
            attack_list = temp_attack_list

            screen.blit(player_img(elapsed_time, dt), (150, cavey[player]+12))

            for i in temp_attack_list:
                for j in temp_enemy_list:
                    if j.rect.colliderect(i.rect):
                        if i.type == j.type:
                            try:
                                attack_list.remove(i)
                            except:
                                pass
                            try:
                                enemy_list.remove(j)
                            except:
                                pass
                            P_killed_enemy += 1
                        else:
                            try:
                                attack_list.remove(i)
                                attack_waste = True
                            except:
                                pass
            #stage clear
            if hp > 0 and len(enemy_list) == 0 and P_stage_enemy <= 0:
                step_sound.stop()
                tut = 'True'
                G_Type = "Menu"
                ingame_bgm.stop()
                main_bgm.play(-1)
                menu()
                continue
        
            for i in range(len(attack_list)):
                attack_list[i].x += 5
                attack_list[i].update()
            for i in range(len(enemy_list)):
                enemy_list[i].x -= (P_stage_speed*dt)/1000
                enemy_list[i].update()

    if G_Type == 'ending':
        screen.blit(getSurface(video_t, ending_video, surface), (0, 0))
        T_B_skip.draw()
        pygame.display.flip()
        video_t += 1/60
        if video_t >= 40:
            etc_bgm.stop()
            main_bgm.play(-1)
            G_Type = 'Intro'
            intro()
    
    pygame.display.update()

#save
with open('data/playerdata/setting.txt', 'w', encoding='utf8') as f:
    f.write(str(master_sound))
    f.write('\n')
    f.write(str(bgm_sound))
    f.write('\n')
    f.write(str(effect_sound))
    f.write('\n')
    for i in range(11):
        f.write(str(K[i]))
        f.write('\n')

with open('data/playerdata/playerdata.txt', 'w', encoding='utf8') as f:
    f.write(str(tut))
    f.write('\n')
    f.write(str(stage))
    for i in range(10):
        f.write('\n')
        f.write(str(star[i]))
    for i in range(5):
        f.write('\n')
        f.write(str(high_time[i]))
    f.write('\n')
    f.write(str(ending))

#종료
pygame.quit()