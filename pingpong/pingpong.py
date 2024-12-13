import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Dimensi layar dan konstanta lainnya
LAYAR_LEBAR, LAYAR_TINGGI = 800, 400
FPS = 60
PADDLE_W, PADDLE_H = 15, 100
BOLA_UKURAN = 15
WARNA_PUTIH = (255, 255, 255)
WARNA_HITAM = (0, 0, 0)
KECEPATAN_PADDLE = 10
BOLA_AWAL_KECEPATAN_X, BOLA_AWAL_KECEPATAN_Y = 5, 5
PENAMBAHAN_KECEPATAN = 0.5
RESET_KECEPATAN = 5

# Inisialisasi layar permainan
layar = pygame.display.set_mode((LAYAR_LEBAR, LAYAR_TINGGI))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# Objek Paddle dan Bola
paddle_kiri = pygame.Rect(30, LAYAR_TINGGI // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
paddle_kanan = pygame.Rect(LAYAR_LEBAR - 30 - PADDLE_W, LAYAR_TINGGI // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
bola = pygame.Rect(LAYAR_LEBAR // 2 - BOLA_UKURAN // 2, LAYAR_TINGGI // 2 - BOLA_UKURAN // 2, BOLA_UKURAN, BOLA_UKURAN)

# Skor pemain
skor_kiri = 0
skor_kanan = 0

# Font untuk skor dan teks
font_skor = pygame.font.Font(None, 36)
font_gol = pygame.font.Font(None, 72)

# Variabel game
running = True
teks_gol = ""
waktu_gol = 0
kecepatan_bola_x, kecepatan_bola_y = BOLA_AWAL_KECEPATAN_X, BOLA_AWAL_KECEPATAN_Y

while running:
    layar.fill(WARNA_HITAM)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol Paddle
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_w] and paddle_kiri.top > 0:
        paddle_kiri.y -= KECEPATAN_PADDLE
    if tombol[pygame.K_s] and paddle_kiri.bottom < LAYAR_TINGGI:
        paddle_kiri.y += KECEPATAN_PADDLE
    if tombol[pygame.K_UP] and paddle_kanan.top > 0:
        paddle_kanan.y -= KECEPATAN_PADDLE
    if tombol[pygame.K_DOWN] and paddle_kanan.bottom < LAYAR_TINGGI:
        paddle_kanan.y += KECEPATAN_PADDLE

    # Gerakan Bola
    bola.x += kecepatan_bola_x
    bola.y += kecepatan_bola_y

    # Pantulan bola dengan dinding atas/bawah
    if bola.top <= 0 or bola.bottom >= LAYAR_TINGGI:
        kecepatan_bola_y = -kecepatan_bola_y

    # Pantulan bola dengan Paddle
    if bola.colliderect(paddle_kiri) or bola.colliderect(paddle_kanan):
        kecepatan_bola_x = -kecepatan_bola_x
        kecepatan_bola_x += PENAMBAHAN_KECEPATAN if kecepatan_bola_x > 0 else -PENAMBAHAN_KECEPATAN
        kecepatan_bola_y += PENAMBAHAN_KECEPATAN if kecepatan_bola_y > 0 else -PENAMBAHAN_KECEPATAN

    # Cek gol dan reset bola
    if bola.left <= 0:  # Gawang kanan
        skor_kanan += 1
        bola.x, bola.y = LAYAR_LEBAR // 2 - BOLA_UKURAN // 2, LAYAR_TINGGI // 2 - BOLA_UKURAN // 2
        kecepatan_bola_x, kecepatan_bola_y = RESET_KECEPATAN, RESET_KECEPATAN
        teks_gol = "GOLLL!!!"
        waktu_gol = pygame.time.get_ticks()

    if bola.right >= LAYAR_LEBAR:  # Gawang kiri
        skor_kiri += 1
        bola.x, bola.y = LAYAR_LEBAR // 2 - BOLA_UKURAN // 2, LAYAR_TINGGI // 2 - BOLA_UKURAN // 2
        kecepatan_bola_x, kecepatan_bola_y = -RESET_KECEPATAN, RESET_KECEPATAN
        teks_gol = "GOLLL!!!"
        waktu_gol = pygame.time.get_ticks()

    # Gambar Paddle, Bola, dan Gawang
    pygame.draw.rect(layar, WARNA_PUTIH, paddle_kiri)
    pygame.draw.rect(layar, WARNA_PUTIH, paddle_kanan)
    pygame.draw.ellipse(layar, WARNA_PUTIH, bola)
    pygame.draw.line(layar, WARNA_PUTIH, (0, 0), (0, LAYAR_TINGGI), 5)
    pygame.draw.line(layar, WARNA_PUTIH, (LAYAR_LEBAR, 0), (LAYAR_LEBAR, LAYAR_TINGGI), 5)

    # Tampilkan Skor
    teks_skor_kiri = font_skor.render(str(skor_kiri), True, WARNA_PUTIH)
    teks_skor_kanan = font_skor.render(str(skor_kanan), True, WARNA_PUTIH)
    layar.blit(teks_skor_kiri, (LAYAR_LEBAR // 4, 20))
    layar.blit(teks_skor_kanan, (LAYAR_LEBAR * 3 // 4 - teks_skor_kanan.get_width(), 20))

    # Tampilkan teks "GOLLL!!!" jika ada gol
    if teks_gol:
        teks_tampilkan = font_gol.render(teks_gol, True, WARNA_PUTIH)
        layar.blit(teks_tampilkan, (LAYAR_LEBAR // 2 - teks_tampilkan.get_width() // 2, LAYAR_TINGGI // 3))
        if pygame.time.get_ticks() - waktu_gol > 1000:  # Hilangkan teks setelah 1 detik
            teks_gol = ""

    # Update layar
    pygame.display.flip()
    clock.tick(FPS)

# Keluar dari Pygame
pygame.quit()
sys.exit()
