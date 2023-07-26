import cv2 # read image/ camera / video input
import threading #file d'execution pour effectuer des taches simultanément

#capture video 
class VideoCamera(object):
    def __del__(self):
        self.video.release() #fonction de suppression
    def initialisation(self):
        self.video = cv2.VideoCapture(0) 
        (self.grabbed, self.frame) = self.video.read() #grapped:bool l'etat de lecture. frame stocke l'image captuée 
        threading.Thread(target=self.update, args=()).start()#met à jour en continu le frame capturé dans un thread séparé.
    
    def get_frame(self):
        image = self.frame #affectation
        _, jpeg = cv2.imencode('.jpg',image)#encode l'image en format jpeg
        return jpeg.tobytes() # renvoie les octects de l'image

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()