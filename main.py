import os
import sys
import time
import threading
import keyboard

from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from pycaw.pycaw import AudioUtilities





class VideoPlayer(QMainWindow):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("Фоновый режим")
        
        self.set_system_volume_to_10_percent()
        
        keyboard.block_key('left windows')
        keyboard.block_key('right windows')
        keyboard.block_key('tab')
        keyboard.block_key('alt')
        keyboard.block_key('shift')
        keyboard.block_key('escape')
        
        for i in range(1, 13):
            try:
                keyboard.block_key(f'f{i}')
            except:
                pass

        self.video_widget = QVideoWidget()
        self.setCentralWidget(self.video_widget)
        
        
        self.audio_output = QAudioOutput()
        
        
        self.audio_output.setVolume(0.2)
        
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self.video_widget)
        
        
        abs_video_path = os.path.abspath(video_path)
        self.player.setSource(QUrl.fromLocalFile(abs_video_path))
        
        
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        
        
        self.setWindowFlags(self.windowFlags() | 
                            Qt.WindowType.WindowStaysOnTopHint | 
                            Qt.WindowType.CustomizeWindowHint)
        self.showFullScreen()
        
        self.setCursor(Qt.CursorShape.BlankCursor)
        
        
        self.player.play()
        
        
        threading.Thread(target=self.start_shutdown_timer, daemon=True).start()

    def set_system_volume_to_10_percent(self):
        try:
            device = AudioUtilities.GetSpeakers()
            if device:
                device.volume_percent = 20
                print("Starting")
        except Exception as e:
            print(f"Hello dev :)")

    def start_shutdown_timer(self):
        """1"""
        time.sleep(178.0)
        self.close_app()


    def close_app(self):
        """g"""
        try:
            keyboard.unhook_all()
        except:
            pass
        
        try:
            if hasattr(self, 'player') and self.player:
                self.player.stop()
        except:
            pass
            
        try:
            self.close()
            os._exit(0)  
        except:
            sys.exit()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    VIDEO_FILE = os.path.join(BASE_DIR, "video.mp4")
    
    
    if not os.path.exists(VIDEO_FILE):
        print(f"no video found")
        sys.exit()

    app = QApplication(sys.argv)
    player = VideoPlayer(VIDEO_FILE)
    sys.exit(app.exec())
