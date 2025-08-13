import cv2
import time

caminho_video = 'media/race.mp4'

video = cv2.VideoCapture(caminho_video)

if not video.isOpened():
    print("Erro ao abrir o vídeo.")
    raise FileNotFoundError(f"Não consegui abrir o vídeo: {caminho_video}")

while True:
    ok, frame = video.read()
    if not ok:
        
        video.release()
        raise RuntimeError("Falha ao ler o primeiro frame.")
        break

    cv2.imshow('Aula 12_08', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
