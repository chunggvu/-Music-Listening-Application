import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from getPremium import Ui_PremRegWindow
from profileScreen import Ui_ProfileWindow
from changePass import Ui_ChangePasswordWindow
import MySQLdb as mdb
import songs
import time
import os

class Ui_HomeWindow(object):
    id = 0
    premium = 0
        
    def receive_prem(self, get_premium):
        Ui_HomeWindow.premium = get_premium
        
    def receive_id(self, get_id):
        Ui_HomeWindow.id = get_id
        
    def show_btn(self):
        self.music_btn.show()
        
    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()  
        
    def load_song(self):
        self.free_song_list.clear()
        self.music_pack_1.clear()
        self.music_pack_2.clear()
        self.music_pack_3.clear()
        
        db = mdb.connect('localhost','root','','music_app')
        
        # basic pack
        basic_music = db.cursor()
        basic_music.execute("SELECT song_management.name, artist_management.artist_name FROM `song_management` Join `artist_management` ON song_management.artist_id = artist_management.artist_id WHERE song_management.plan_id = '"+str(0)+"'")
        get_basic_music = basic_music.fetchall()
        basic_song_name = [(row[0], row[1]) for row in get_basic_music]
        
        for basic_song in basic_song_name:
            if basic_song not in self.basic_songs_list:
                self.basic_songs_list.append(str(basic_song))
        
        for basic_song_str in self.basic_songs_list:
            basic_song_tuple = eval(basic_song_str)
            
            song_name = basic_song_tuple[0]
            artist_name = basic_song_tuple[1]
            item = QListWidgetItem(f"{song_name} - {artist_name}")
            item_text = f"{song_name} \n {artist_name}"
            icon = QtGui.QIcon('resources3.qrc/music_icon.png')
            item = QListWidgetItem(icon, item_text)
            self.free_song_list.addItem(item)
        
        songs_link = db.cursor()
        songs_link.execute("SELECT `link` FROM `song_management` WHERE plan_id = '"+str(0)+"'")
        
        query_link = songs_link.fetchall()
        links = [row[0] for row in query_link]
        
        for link_value in links:
            self.current_basic_songs.append(link_value)
    
        # pack 1
        pack_1 = db.cursor()
        pack_1.execute("SELECT song_management.name, artist_management.artist_name FROM `song_management` Join `artist_management` ON song_management.artist_id = artist_management.artist_id WHERE song_management.plan_id = '"+str(1)+"'")
        get_music_pack_1 = pack_1.fetchall()
        pack_1_song_name = [(row[0], row[1]) for row in get_music_pack_1]
        
        for pack_1_song in pack_1_song_name:
            if pack_1_song not in self.song_pack_1:
                self.song_pack_1.append(str(pack_1_song))
        
        for pack_1_song_str in self.song_pack_1:
            pack_1_song_tuple = eval(pack_1_song_str)
            
            song_name_1 = pack_1_song_tuple[0]
            artist_name_1 = pack_1_song_tuple[1]
            item_1 = QListWidgetItem(f"{song_name_1} - {artist_name_1}")
            item_text_1 = f"{song_name_1} \n {artist_name_1}"
            item_1 = QListWidgetItem(QIcon('resources3.qrc/music_icon.png'), item_text_1)
            self.music_pack_1.addItem(item_1)
            
        pack_1_songs_link = db.cursor()
        pack_1_songs_link.execute("SELECT `link` FROM `song_management` WHERE plan_id = '"+str(1)+"'")
        
        pack_1_link = pack_1_songs_link.fetchall()
        pack_1_links = [row[0] for row in pack_1_link]
        
        for pack_1_link_value in pack_1_links:
            self.current_song_pack_1.append(pack_1_link_value)
           
        # pack 2
        pack_2 = db.cursor()
        pack_2.execute("SELECT song_management.name, artist_management.artist_name FROM `song_management` Join `artist_management` ON song_management.artist_id = artist_management.artist_id WHERE song_management.plan_id = '"+str(2)+"'")
        get_music_pack_2 = pack_2.fetchall()
        pack_2_song_name = [(row[0], row[1]) for row in get_music_pack_2]
        
        for pack_2_song in pack_2_song_name:
            if pack_2_song not in self.song_pack_2:
                self.song_pack_2.append(str(pack_2_song))
        
        for pack_2_song_str in self.song_pack_2:
            pack_2_song_tuple = eval(pack_2_song_str)
            
            song_name_2 = pack_2_song_tuple[0]
            artist_name_2 = pack_2_song_tuple[1]
            item_2 = QListWidgetItem(f"{song_name_2} - {artist_name_2}")
            item_text_2 = f"{song_name_2} \n {artist_name_2}"
            item_2 = QListWidgetItem(QIcon('resources3.qrc/music_icon.png'), item_text_2)
            self.music_pack_2.addItem(item_2)
            
        pack_2_songs_link = db.cursor()
        pack_2_songs_link.execute("SELECT `link` FROM `song_management` WHERE plan_id = '"+str(2)+"'")
        
        pack_2_link = pack_2_songs_link.fetchall()
        pack_2_links = [row[0] for row in pack_2_link]
        
        for pack_2_link_value in pack_2_links:
            self.current_song_pack_2.append(pack_2_link_value)
           
        # pack 3 
        pack_3 = db.cursor()
        pack_3.execute("SELECT song_management.name, artist_management.artist_name FROM `song_management` Join `artist_management` ON song_management.artist_id = artist_management.artist_id WHERE song_management.plan_id = '"+str(3)+"'")
        get_music_pack_3 = pack_3.fetchall()
        pack_3_song_name = [(row[0], row[1]) for row in get_music_pack_3]
        
        for pack_3_song in pack_3_song_name:
            if pack_3_song not in self.song_pack_3:
                self.song_pack_3.append(str(pack_3_song))
        
        for pack_3_song_str in self.song_pack_3:
            pack_3_song_tuple = eval(pack_3_song_str)
            
            song_name_3 = pack_3_song_tuple[0]
            artist_name_3 = pack_3_song_tuple[1]
            item_3 = QListWidgetItem(f"{song_name_3} - {artist_name_3}")
            item_text_3 = f"{song_name_3} \n {artist_name_3}"
            item_3 = QListWidgetItem(QIcon('resources3.qrc/music_icon.png'), item_text_3)
            self.music_pack_3.addItem(item_3)
        
        pack_3_songs_link = db.cursor()
        pack_3_songs_link.execute("SELECT `link` FROM `song_management` WHERE plan_id = '"+str(3)+"'")
        
        pack_3_link = pack_3_songs_link.fetchall()
        pack_3_links = [row[0] for row in pack_3_link]
        
        for pack_3_link_value in pack_3_links:
            self.current_song_pack_3.append(pack_3_link_value)
    
    def on_item_clicked(self, current_list_widget):
        def handle_item_click(item):
            current_list = current_list_widget
            other_list_widgets = [self.free_song_list, self.music_pack_1, self.music_pack_2, self.music_pack_3]  # Add more list widgets if needed

            for list_widget in other_list_widgets:
                if list_widget is not current_list:
                    list_widget.clearSelection()
            if current_list is self.free_song_list:
                self.play_btn.clicked.connect(self.play_basic_song)
            elif current_list is self.music_pack_1:
                self.play_btn.clicked.connect(self.play_pack_1_song)
            elif current_list is self.music_pack_2:
                self.play_btn.clicked.connect(self.play_pack_2_song)
            elif current_list is self.music_pack_3:
                self.play_btn.clicked.connect(self.play_pack_3_song)                

        return handle_item_click
                    
    # def add_songs(self):
    #     files, _ = QFileDialog.getOpenFileNames(
    #         self, caption='Add Songs', directory=':\\', 
    #         filter="Supported Files (*.mp3;*.mpeg;*.ogg;*.m4a;*.MP3;*.wma;*.acc;*.amr)"
    #     )

    #     if files:
    #         for file in files:
    #             songs.current_songs_list.append(file)
    #             self.free_song_list.addItem(
    #                 QListWidgetItem(
    #                     QIcon('resources3.qrc/music_icon.png'),
    #                     os.path.basename(file)))
                 
    def play_basic_song(self):
        try:
            global stopped
            stopped = False

            current_selection = self.free_song_list.currentRow()
            # current_selection = self.music_pack_2.currentRow()
            # current_selection = self.music_pack_3.currentRow()
            current_song = self.current_basic_songs[current_selection]
            
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Play song error: {e}")
            
    def play_pack_1_song(self):
        try:
            global stopped
            stopped = False

            current_song_pack_1_selection = self.music_pack_1.currentRow()
            current_pack_1_song = self.current_song_pack_1[current_song_pack_1_selection]
            
            song_url = QMediaContent(QUrl.fromLocalFile(current_pack_1_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Play song error: {e}")
            
    def play_pack_2_song(self):
        try:
            global stopped
            stopped = False

            current_song_pack_2_selection = self.music_pack_2.currentRow()
            current_pack_2_song = self.current_song_pack_2[current_song_pack_2_selection]
            
            song_url = QMediaContent(QUrl.fromLocalFile(current_pack_2_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Play song error: {e}")
            
    def play_pack_3_song(self):
        try:
            global stopped
            stopped = False

            current_song_pack_3_selection = self.music_pack_3.currentRow()
            current_pack_3_song = self.current_song_pack_3[current_song_pack_3_selection]
            
            song_url = QMediaContent(QUrl.fromLocalFile(current_pack_3_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Play song error: {e}")
    
    def play_ads(self):
        music_path = 'ads/PocaWavy.mp3'
        media_content = QMediaContent(QUrl.fromLocalFile(music_path))
        self.player.setMedia(media_content)
        self.player.play()
        self.move_slider()
        
    def song_end(self, status):
        if status == QMediaPlayer.EndOfMedia:
            if self.i % 3 == 0:
                self.play_btn.setEnabled(False)
                self.stop_btn.setEnabled(False)
                self.next_btn.setEnabled(False)
                self.previous_btn.setEnabled(False)
                self.pause_btn.setEnabled(False)
                self.play_ads()
            else:
                self.next_song()
            self.i += 1 

    def move_slider(self):
        if stopped:
            return
        else:
            if self.player.state() == QMediaPlayer.PlayingState:
                self.music_slider.setMinimum(0)
                self.music_slider.setMaximum(self.player.duration())
                slider_position = self.player.position()
                self.music_slider.setValue(slider_position)

                current_time = time.strftime('%M:%S', time.localtime(self.player.position() / 1000))
                song_duration = time.strftime('%M:%S', time.localtime(self.player.duration() / 1000))
                self.start_time_label.setText(f"{current_time}")
                self.end_time_label.setText(f"{song_duration}")

    def pause_and_unpause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def stop_song(self):
        try:
            self.player.stop()
            self.music_slider.setValue(0)
            self.start_time_label.setText(f"00:00")
            self.end_time_label.setText(f"00:00")
            self.play_btn.isChecked(False)
        except Exception as e:
            print('Stopping song error: {e}')

    # def addSongToPlaylist(self):
        
    # def default_next(self):
    #     try:
    #         current_media = self.player.media()
    #         current_song_url = current_media.canonicalUrl().path()[1:]
    #         current_song_index = self.current_songs.index(current_song_url)
    #         if current_song_index + 1 == len(self.current_songs):
    #             next_index = 0
    #         else:
    #             next_index = current_song_index + 1
    #         current_song = self.current_songs[next_index]
    #         self.free_song_list.setCurrentRow(next_index) 

    #         song_url = QMediaContent(QUrl.fromLocalFile(current_song))
    #         self.player.setMedia(song_url)
    #         self.player.play()
    #         self.move_slider()

    #     except Exception as e:
    #         print(f"Play song error: {e}")

    # def looped_next(self):
    #     try:
    #         current_media = self.player.media()
    #         current_song_url = current_media.canonicalUrl().path()[1:]
    #         current_song_index = self.current_songs.index(current_song_url)
    #         current_song = self.current_songs[current_song_index]
    #         self.free_song_list.setCurrentRow(current_song_index)     

    #         song_url = QMediaContent(QUrl.fromLocalFile(current_song))
    #         self.player.setMedia(song_url)
    #         self.player.play()
    #         self.move_slider()

    #     except Exception as e:
    #         print(f"Looped song error: {e}")

    # def shuffle_next(self):
    #     try:
    #         song_index = random.randint(0, len(self.current_songs))
    #         current_song = self.current_songs[song_index]
    #         self.free_song_list.setCurrentRow(song_index)     

    #         song_url = QMediaContent(QUrl.fromLocalFile(current_song))
    #         self.player.setMedia(song_url)
    #         self.player.play()
    #         self.move_slider()

    #     except Exception as e:
    #         print(f"Shuffled song error: {e}")

    def next_song(self):
        try:
            current_selection = self.free_song_list.currentRow()

            if current_selection + 1 == len(self.current_basic_songs):
                next_index = 0
            else:
                next_index = current_selection + 1
            current_song = self.current_basic_songs[next_index]
            self.free_song_list.setCurrentRow(next_index)
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Next song error: {e}")

    # def loop_one_song(self):
    #     try:
    #         global is_shuffled
    #         global looped

    #         if not looped:
    #             looped = True
    #             self.shuffle_btn.setEnabled(False)
    #         else:
    #             looped = False
    #             self.shuffle_btn.setEnabled(True)

    #     except Exception as e:
    #         print('Looping song error: {e}')

    # def shuffled_playlist(self):
    #     try:
    #         global is_shuffled
    #         global looped

    #         if not is_shuffled:
    #             is_shuffled = True
    #             self.loop_btn.setEnabled(False)

    #         else:
    #             is_shuffled = False
    #             self.loop_btn.setEnabled(True)
    #     except Exception as e:
    #         print('Shuffle song error: {e}')

    def previous_song(self):
        try:
            current_selection = self.free_song_list.currentRow()

            if current_selection == 0:
                previous_index = len(self.current_basic_songs) - 1
            else:
                previous_index = current_selection - 1

            current_song = self.current_basic_songs[previous_index]
            self.free_song_list.setCurrentRow(previous_index)
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Previous song error: {e}")

    def volume_changed(self):
        try:
            self.current_volume = self.volume_slider.value()
            self.player.setVolume(self.current_volume)
        except Exception as e:
            print(f"Volume change error: {e}")      

    def showHome(self):
        self.stacked_widget.setCurrentIndex(0)

    def showPlaylist(self):
        self.stop_song()
        self.home_btn.setChecked(False)
        self.home_btn_2.setChecked(False)
        self.search_btn.setChecked(False)
        self.search_btn_2.setChecked(False)
        self.download_btn.setChecked(False)
        self.download_btn_2.setChecked(False)
        
        self.library_btn.setChecked(True)
        self.library_btn_2.setChecked(True)
        self.stacked_widget.setCurrentIndex(1)

    # def createPlaylist(self):
    #     try:
    #         from createPlaylist import Ui_CreatePlaylistWindow
    #         self.create_playlist_window = QtWidgets.QMainWindow()
    #         self.ui = Ui_CreatePlaylistWindow()
    #         self.ui.setupUi(self.create_playlist_window)
    #         self.create_playlist_window.show()
    #         sendIdToCreatePlaylist = Ui_CreatePlaylistWindow
    #         sendIdToCreatePlaylist.receiveId(Ui_HomeWindow.id)
    #     except ImportError:
    #         pass 
        
    # def displayPlaylist(self):
    #     db = mdb.connect('localhost','root','','music_app')
    #     query = db.cursor()
        
    #     query.execute("SELECT `playlist_name` FROM playlist_management WHERE user_id = '"+str(Ui_HomeWindow.id)+"'")
    #     get_playlist = query.fetchall()
    #     playlists = [(row[0]) for row in get_playlist]
        
    #     for playlist in playlists:
    #         if playlist not in self.playlist_list:
    #             self.playlist_list.append(str(playlist))
                
    #     for item in self.playlist_list:
    #         self.listWidget.addItem(item)   
       
    def premiumNotice(self):
        self.home_btn.setChecked(True)
        self.download_btn.setChecked(False)
        self.download_btn_2.setChecked(False)
        QMessageBox.information(None, "Premium required", "You need a premium subscription")
        self.stacked_widget.setCurrentIndex(0)
        
    def showDownload(self):
        self.stop_song()
        self.home_btn.setChecked(False)
        self.home_btn_2.setChecked(False)
        self.search_btn.setChecked(False)
        self.search_btn_2.setChecked(False)
        self.library_btn.setChecked(False)
        self.library_btn_2.setChecked(False)
        
        self.download_btn.setChecked(True)
        self.download_btn_2.setChecked(True)
        self.stacked_widget.setCurrentIndex(3)  
                  
    def showSearch(self):
        self.stop_song()
        self.home_btn.setChecked(False)
        self.home_btn_2.setChecked(False)
        self.download_btn.setChecked(False)
        self.download_btn_2.setChecked(False)
        self.library_btn.setChecked(False)
        self.library_btn_2.setChecked(False)
        
        self.search_btn.setChecked(True)
        self.search_btn_2.setChecked(True)
        self.stacked_widget.setCurrentIndex(2)
        
        text = self.search_input.text()
        
        self.search_list.clear()
        db = mdb.connect('localhost','root','','music_app')
        query = db.cursor()
        query.execute("SELECT name FROM `song_management` WHERE name LIKE '"+ text +"%'")
        song = query.fetchall()
        found_song = [row[0] for row in song]
        
        if len(text) == 0:
            self.search_list.clear()
            songs.search_song_list.clear()
        else:
            for item in found_song:
                if item not in songs.search_song_list:
                    songs.search_song_list.append(item)
            for song_name in songs.search_song_list:
                self.search_list.addItem(
                    QListWidgetItem(
                    QIcon('resources3.qrc/music_icon.png'),
                    song_name))
                
    def get_premium(self):
        try:
            from getPremium import Ui_PremRegWindow
            self.premium_window = QtWidgets.QMainWindow()
            self.ui = Ui_PremRegWindow()
            self.ui.setupUi(self.premium_window)
            self.premium_window.show()
            self.stop_song()
            self.closeWindows()
        except ImportError:
            pass
        
    def showProfile(self):
        try:
            from profileScreen import Ui_ProfileWindow
            self.profile_window = QtWidgets.QMainWindow()
            self.ui = Ui_ProfileWindow()
            self.ui.setupUi(self.profile_window)
            self.profile_window.show()
            self.stop_song()
            self.closeWindows()
        except ImportError:
            pass
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 899)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"border:none;\n"
"padding: 0px;\n"
"margin:0px;\n"
"color:#fff\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: black;\n"
"}\n"
"\n"
"#icon_only_widget, #full_menu_widget, #main_widget{\n"
"background-color:#1f1f1f;\n"
"border-radius:6px\n"
"}\n"
"\n"
"#icon_only_widget QPushButton {\n"
"border:none;\n"
"padding:10px 30px;\n"
"border-radius:10px\n"
"}\n"
"\n"
"#icon_only_widget QPushButton:hover {\n"
"border-radius:0px;\n"
"background-color: rgba(236, 236, 236, 0.1);\n"
"}\n"
"\n"
"#full_menu_widget QPushButton {\n"
"border:none;\n"
"padding:10px 30px;\n"
"border-radius:10px;\n"
"color: gray\n"
"}\n"
"\n"
"#full_menu_widget QPushButton:hover {\n"
"border-radius:0px;\n"
"background-color: rgba(236, 236, 236, 0.1);\n"
"}\n"
"\n"
"#full_menu_widget QPushButton:checked {\n"
"color:white;\n"
"}\n"
"\n"
"#search_input{\n"
"border:none;\n"
"padding: 15px 10px;\n"
"border-radius: 20px;\n"
"background-color: #2A2A2A;\n"
"color:white;\n"
"}\n"
"\n"
"#search_input:hover {\n"
"border: 1px solid gray\n"
"}\n"
"\n"
"#search_input:focus {\n"
"border: 2px solid white\n"
"}\n"
"\n"
"#explore_prem{\n"
"background-color:white;\n"
"border-radius: 18px;\n"
"padding:10px;\n"
"color:#121212;\n"
"}\n"
"\n"
"#explore_prem:hover{\n"
"background-color:#121212;\n"
"color:white\n"
"}\n"
"\n"
"#add_music_btn {\n"
"border: 1px solid white;\n"
"border_radius: 6px;\n"
"padding:10px 8px\n"
"}\n"
"\n"
"#add_music_btn:hover {\n"
"background-color:white;\n"
"color:black\n"
"}\n"
"\n"
"#create_playlist_btn {\n"
"background-color:white;\n"
"padding: 10px 20px;\n"
"border-radius: 20px;\n"
"color:#121212;\n"
"}\n"
"\n"
"#free_song_list, #music_pack_1, #music_pack_2, #music_pack_3, #search_list, #listWidget{\n"
"background-color: #1f1f1f;\n"
"selection-background-color: rgba(255,255,255,100);;\n"
"selection-color: rgb(66, 66, 66);\n"
"}\n"
"\n"
"#widget QPushButton{\n"
"border-radius: 6px;\n"
"margin: 0 10px\n"
"}\n"
"\n"
"#widget QPushButton:hover{\n"
"background-color: rgba(255,255,255,100)\n"
"}\n"
"\n"
"#widget QPushButton:checked{\n"
"background-color: rgba(255,255,255,100);\n"
"}\n"
"\n"
"#stacked_widget {\n"
"border-top:10px solid black;\n"
"}\n"
"\n"
".QListWidget{\n"
"padding:10px;\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
".QListWidget:Item {\n"
"padding:5px;\n"
"margin:10px \n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logo_layout = QtWidgets.QHBoxLayout()
        self.logo_layout.setContentsMargins(-1, -1, -1, 0)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName("logo_layout")
        self.label = QtWidgets.QLabel(self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources3.qrc/icons8-music-50.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo_layout.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addLayout(self.logo_layout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources3.qrc/House.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QtCore.QSize(40, 40))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)
        self.home_btn.setObjectName("home_btn")
        self.verticalLayout.addWidget(self.home_btn)
        self.search_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources3.qrc/icons8-search-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QtCore.QSize(40, 40))
        self.search_btn.setCheckable(True)
        self.search_btn.setAutoExclusive(True)
        self.search_btn.setObjectName("search_btn")
        self.verticalLayout.addWidget(self.search_btn)
        self.library_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.library_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources3.qrc/Playlist.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.library_btn.setIcon(icon2)
        self.library_btn.setIconSize(QtCore.QSize(40, 40))
        self.library_btn.setCheckable(True)
        self.library_btn.setAutoExclusive(True)
        self.library_btn.setObjectName("library_btn")
        self.verticalLayout.addWidget(self.library_btn)
        self.download_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.download_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources3.qrc/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn.setIcon(icon3)
        self.download_btn.setIconSize(QtCore.QSize(40, 40))
        self.download_btn.setObjectName("download_btn")
        self.verticalLayout.addWidget(self.download_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 522, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2, 0, QtCore.Qt.AlignLeft)
        self.search_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.search_btn_2.setFont(font)
        self.search_btn_2.setIcon(icon1)
        self.search_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.search_btn_2.setCheckable(True)
        self.search_btn_2.setAutoExclusive(True)
        self.search_btn_2.setObjectName("search_btn_2")
        self.verticalLayout_2.addWidget(self.search_btn_2, 0, QtCore.Qt.AlignLeft)
        self.library_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.library_btn_2.setFont(font)
        self.library_btn_2.setIcon(icon2)
        self.library_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.library_btn_2.setCheckable(True)
        self.library_btn_2.setAutoExclusive(True)
        self.library_btn_2.setObjectName("library_btn_2")
        self.verticalLayout_2.addWidget(self.library_btn_2)
        self.download_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.download_btn_2.setFont(font)
        self.download_btn_2.setIcon(icon3)
        self.download_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.download_btn_2.setObjectName("download_btn_2")
        self.verticalLayout_2.addWidget(self.download_btn_2, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 511, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_page = QtWidgets.QWidget(self.main_widget)
        self.header_page.setMinimumSize(QtCore.QSize(0, 60))
        self.header_page.setObjectName("header_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_page)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_btn = QtWidgets.QPushButton(self.header_page)
        self.menu_btn.setMinimumSize(QtCore.QSize(44, 40))
        self.menu_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources3.qrc/icons8-menu-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QtCore.QSize(40, 40))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_3.addWidget(self.menu_btn, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.search_box = QtWidgets.QHBoxLayout()
        self.search_box.setContentsMargins(-1, -1, 0, -1)
        self.search_box.setSpacing(0)
        self.search_box.setObjectName("search_box")
        self.search_input = QtWidgets.QLineEdit(self.header_page)
        self.search_input.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.search_input.setFont(font)
        self.search_input.setObjectName("search_input")
        self.search_box.addWidget(self.search_input)
        self.horizontalLayout_3.addLayout(self.search_box)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.explore_prem = QtWidgets.QPushButton(self.header_page)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.explore_prem.setFont(font)
        self.explore_prem.setObjectName("explore_prem")
        self.horizontalLayout_2.addWidget(self.explore_prem)
        self.account_btn = QtWidgets.QPushButton(self.header_page)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.account_btn.setFont(font)
        self.account_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources3.qrc/icons8-male-user-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_btn.setIcon(icon5)
        self.account_btn.setIconSize(QtCore.QSize(40, 40))
        self.account_btn.setObjectName("account_btn")
        self.horizontalLayout_2.addWidget(self.account_btn, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.header_page)
        self.stacked_widget = QtWidgets.QStackedWidget(self.main_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.home_widget = QtWidgets.QWidget()
        self.home_widget.setObjectName("home_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.home_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.music_list = QtWidgets.QWidget(self.home_widget)
        self.music_list.setObjectName("music_list")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.music_list)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.basic_pack = QtWidgets.QLabel(self.music_list)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.basic_pack.setFont(font)
        self.basic_pack.setObjectName("basic_pack")
        self.verticalLayout_7.addWidget(self.basic_pack)
        self.free_song_list = QtWidgets.QListWidget(self.music_list)
        self.free_song_list.setObjectName("free_song_list")
        self.verticalLayout_7.addWidget(self.free_song_list)
        self.pack_1 = QtWidgets.QLabel(self.music_list)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.pack_1.setFont(font)
        self.pack_1.setObjectName("pack_1")
        self.verticalLayout_7.addWidget(self.pack_1)
        self.music_pack_1 = QtWidgets.QListWidget(self.music_list)
        self.music_pack_1.setObjectName("music_pack_1")
        self.verticalLayout_7.addWidget(self.music_pack_1)
        self.pack_2 = QtWidgets.QLabel(self.music_list)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.pack_2.setFont(font)
        self.pack_2.setObjectName("pack_2")
        self.verticalLayout_7.addWidget(self.pack_2)
        self.music_pack_2 = QtWidgets.QListWidget(self.music_list)
        self.music_pack_2.setObjectName("music_pack_2")
        self.verticalLayout_7.addWidget(self.music_pack_2)
        self.pack_3 = QtWidgets.QLabel(self.music_list)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.pack_3.setFont(font)
        self.pack_3.setObjectName("pack_3")
        self.verticalLayout_7.addWidget(self.pack_3)
        self.music_pack_3 = QtWidgets.QListWidget(self.music_list)
        self.music_pack_3.setObjectName("music_pack_3")
        self.verticalLayout_7.addWidget(self.music_pack_3)
        self.verticalLayout_6.addWidget(self.music_list)
        self.music_btn = QtWidgets.QWidget(self.home_widget)
        self.music_btn.setObjectName("music_btn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.music_btn)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.music_btn)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.previous_btn = QtWidgets.QPushButton(self.widget)
        self.previous_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources3.qrc/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn.setIcon(icon6)
        self.previous_btn.setIconSize(QtCore.QSize(40, 40))
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout_6.addWidget(self.previous_btn)
        self.pause_btn = QtWidgets.QPushButton(self.widget)
        self.pause_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources3.qrc/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn.setIcon(icon7)
        self.pause_btn.setIconSize(QtCore.QSize(40, 40))
        self.pause_btn.setCheckable(False)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout_6.addWidget(self.pause_btn)
        self.play_btn = QtWidgets.QPushButton(self.widget)
        self.play_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources3.qrc/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon8)
        self.play_btn.setIconSize(QtCore.QSize(40, 40))
        self.play_btn.setCheckable(False)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout_6.addWidget(self.play_btn)
        self.stop_btn = QtWidgets.QPushButton(self.widget)
        self.stop_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources3.qrc/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn.setIcon(icon9)
        self.stop_btn.setIconSize(QtCore.QSize(40, 40))
        self.stop_btn.setCheckable(False)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_6.addWidget(self.stop_btn)
        self.next_btn = QtWidgets.QPushButton(self.widget)
        self.next_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources3.qrc/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon10)
        self.next_btn.setIconSize(QtCore.QSize(40, 40))
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_6.addWidget(self.next_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources3.qrc/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("")
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_time_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.start_time_label.setFont(font)
        self.start_time_label.setObjectName("start_time_label")
        self.horizontalLayout_5.addWidget(self.start_time_label)
        self.music_slider = QtWidgets.QSlider(self.widget)
        self.music_slider.setOrientation(QtCore.Qt.Horizontal)
        self.music_slider.setObjectName("music_slider")
        self.horizontalLayout_5.addWidget(self.music_slider)
        self.end_time_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.end_time_label.setFont(font)
        self.end_time_label.setObjectName("end_time_label")
        self.horizontalLayout_5.addWidget(self.end_time_label)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.music_btn)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.music_btn)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.toolButton = QtWidgets.QToolButton(self.music_btn)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources3.qrc/volume_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon12)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_4.addWidget(self.toolButton)
        self.volume_slider = QtWidgets.QSlider(self.music_btn)
        self.volume_slider.setMinimumSize(QtCore.QSize(0, 0))
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout_4.addWidget(self.volume_slider, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.music_btn)
        self.stacked_widget.addWidget(self.home_widget)
        self.playlist_widget = QtWidgets.QWidget()
        self.playlist_widget.setObjectName("playlist_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.playlist_widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.create_playlist_btn = QtWidgets.QPushButton(self.playlist_widget)
        self.create_playlist_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.create_playlist_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.create_playlist_btn.setFont(font)
        self.create_playlist_btn.setObjectName("create_playlist_btn")
        self.verticalLayout_8.addWidget(self.create_playlist_btn, 0, QtCore.Qt.AlignHCenter)
        self.listWidget = QtWidgets.QListWidget(self.playlist_widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_8.addWidget(self.listWidget)
        self.stacked_widget.addWidget(self.playlist_widget)
        self.search_widget = QtWidgets.QWidget()
        self.search_widget.setObjectName("search_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.search_widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.search_list = QtWidgets.QListWidget(self.search_widget)
        self.search_list.setObjectName("search_list")
        self.verticalLayout_10.addWidget(self.search_list)
        self.stacked_widget.addWidget(self.search_widget)
        self.favorite_widget = QtWidgets.QWidget()
        self.favorite_widget.setObjectName("favorite_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.favorite_widget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.favorite_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.stacked_widget.addWidget(self.favorite_widget)
        self.verticalLayout_5.addWidget(self.stacked_widget)
        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        self.menu_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.menu_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn.setChecked) # type: ignore
        self.library_btn.toggled['bool'].connect(self.library_btn_2.setChecked) # type: ignore
        self.library_btn_2.toggled['bool'].connect(self.library_btn.setChecked) # type: ignore
        self.search_btn.toggled['bool'].connect(self.search_btn_2.setChecked) # type: ignore
        self.search_btn_2.toggled['bool'].connect(self.search_btn.setChecked) # type: ignore
        self.download_btn.toggled['bool'].connect(self.download_btn_2.setChecked) # type: ignore
        self.download_btn_2.toggled['bool'].connect(self.download_btn.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "MUSIC"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.search_btn_2.setText(_translate("MainWindow", "Search"))
        self.library_btn_2.setText(_translate("MainWindow", "Your playlist"))
        self.download_btn_2.setText(_translate("MainWindow", "Download"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "What do you want to listen to?"))
        self.explore_prem.setText(_translate("MainWindow", "Explore Premium"))
        self.basic_pack.setText(_translate("MainWindow", "Basic pack"))
        self.pack_1.setText(_translate("MainWindow", "Pack 1"))
        self.pack_2.setText(_translate("MainWindow", "Pack 2"))
        self.pack_3.setText(_translate("MainWindow", "Pack 3"))
        self.start_time_label.setText(_translate("MainWindow", "00:00"))
        self.end_time_label.setText(_translate("MainWindow", "00:00"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.create_playlist_btn.setText(_translate("MainWindow", "Create your playlist"))
        self.label_2.setText(_translate("MainWindow", "Download"))
        
        self.i = 1
        self.basic_songs_list = []
        self.current_basic_songs = []
        self.song_pack_1 = []
        self.current_song_pack_1 = []
        self.song_pack_2 = []
        self.current_song_pack_2 = []
        self.song_pack_3 = []
        self.current_song_pack_3 = []
        
        self.free_song_list.setViewMode(QtWidgets.QListView.IconMode)
        self.free_song_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.free_song_list.setWrapping(False)
        
        self.music_pack_1.setViewMode(QtWidgets.QListView.IconMode)
        self.music_pack_1.setFlow(QtWidgets.QListView.LeftToRight)
        self.music_pack_1.setWrapping(False)
        
        self.music_pack_2.setViewMode(QtWidgets.QListView.IconMode)
        self.music_pack_2.setFlow(QtWidgets.QListView.LeftToRight)
        self.music_pack_2.setWrapping(False)
        
        self.music_pack_3.setViewMode(QtWidgets.QListView.IconMode)
        self.music_pack_3.setFlow(QtWidgets.QListView.LeftToRight)
        self.music_pack_3.setWrapping(False)
        
        self.icon_only_widget.hide()
        self.home_btn_2.setChecked(True)        
        self.home_btn.clicked.connect(self.showHome)
        self.home_btn_2.clicked.connect(self.showHome)      
        self.search_btn.clicked.connect(self.showSearch)
        self.search_btn_2.clicked.connect(self.showSearch)
        self.search_input.textChanged.connect(self.showSearch)    
        self.library_btn.clicked.connect(self.showPlaylist)
        self.library_btn_2.clicked.connect(self.showPlaylist)  
        # self.pushButton_2.clicked.connect(self.addSongToPlaylist)
        # self.create_playlist_btn.clicked.connect(self.createPlaylist)
        self.account_btn.clicked.connect(self.showProfile)        
        self.explore_prem.clicked.connect(self.get_premium)
        self.explore_prem.clicked.connect(MainWindow.close)
        
        self.playlist_list = []

        if Ui_HomeWindow.premium == 0:
            self.download_btn.clicked.connect(self.premiumNotice)
            self.download_btn_2.clicked.connect(self.premiumNotice)
        elif Ui_HomeWindow.premium == 1:
            self.explore_prem.hide()
            self.download_btn.clicked.connect(self.showDownload)
            self.download_btn_2.clicked.connect(self.showDownload)
            
        sendIdToPremReg = Ui_PremRegWindow
        sendIdToPremReg.receive_id(Ui_HomeWindow.id)
        
        sendIdToProfile = Ui_ProfileWindow
        sendIdToProfile.receive_id(Ui_HomeWindow.id)
        
        # sendIdToChangePass = Ui_ProfileWindow
        # sendIdToChangePass.receive_id(Ui_HomeWindow.id)
        
        if Ui_HomeWindow.premium == 1:
            db = mdb.connect('localhost','root','','music_app')
            plan_id = db.cursor()
            plan_id.execute("SELECT `plan_id` FROM premium_payment_management WHERE user_id = '"+str(Ui_HomeWindow.id)+"'")
            
            get_plan_id = plan_id.fetchone()[0]
        elif Ui_HomeWindow.premium == 0:
            get_plan_id = 0
        
        self.music_pack_1.setEnabled(False)
        self.music_pack_2.setEnabled(False)
        self.music_pack_3.setEnabled(False)
        
        self.pack_1.hide()
        self.music_pack_1.hide()
        self.pack_2.hide()
        self.music_pack_2.hide()
        self.pack_3.hide()
        self.music_pack_3.hide()
        
        if Ui_HomeWindow.premium == 0:
            self.music_pack_1.setEnabled(False)
            self.music_pack_2.setEnabled(False)
            self.music_pack_3.setEnabled(False)
            
            self.pack_1.hide()
            self.music_pack_1.hide()
            self.pack_2.hide()
            self.music_pack_2.hide()
            self.pack_3.hide()
            self.music_pack_3.hide()
        elif Ui_HomeWindow.premium == 1:
            if get_plan_id == 1:
                self.pack_1.show()
                self.music_pack_1.show()
                self.music_pack_1.setEnabled(True)
            elif get_plan_id == 2:
                self.pack_1.show()
                self.music_pack_1.show()
                self.music_pack_1.setEnabled(True)
                
                self.pack_2.show()
                self.music_pack_2.show()
                self.music_pack_2.setEnabled(True)
            elif get_plan_id == 3:
                self.pack_1.show()
                self.music_pack_1.show()
                self.music_pack_1.setEnabled(True)
                
                self.pack_2.show()
                self.music_pack_2.show()
                self.music_pack_2.setEnabled(True)
                
                self.pack_3.show()
                self.music_pack_3.show()
                self.music_pack_3.setEnabled(True)
            elif get_plan_id == 4:
                self.pack_1.show()
                self.music_pack_1.show()
                self.music_pack_1.setEnabled(True)
                
                self.pack_2.show()
                self.music_pack_2.show()
                self.music_pack_2.setEnabled(True)
                
                self.pack_3.show()
                self.music_pack_3.show()
                self.music_pack_3.setEnabled(True)
        
        global stopped
        global looped
        global is_shuffled

        stopped = False
        looped = False
        is_shuffled = False
        
        self.player = QMediaPlayer()
        self.current_volume = 50
        self.player.setVolume(self.current_volume)
        
        self.timer = QTimer(MainWindow)
        self.timer.start(1000)
        self.timer.timeout.connect(self.move_slider)
        self.volume_slider.sliderMoved[int].connect(lambda: self.volume_changed())
        self.music_slider.sliderMoved[int].connect(lambda: self.player.setPosition(self.music_slider.value()))
        
        self.music_btn.hide()
        self.player.mediaStatusChanged.connect(self.song_end)

        self.free_song_list.currentItemChanged.connect(self.show_btn)
        self.music_pack_1.currentItemChanged.connect(self.show_btn)
        self.music_pack_2.currentItemChanged.connect(self.show_btn)
        self.music_pack_3.currentItemChanged.connect(self.show_btn)
        self.search_list.currentItemChanged.connect(self.show_btn)
        
        self.free_song_list.itemClicked.connect(self.on_item_clicked(self.free_song_list))
        self.music_pack_1.itemClicked.connect(self.on_item_clicked(self.music_pack_1))
        self.music_pack_2.itemClicked.connect(self.on_item_clicked(self.music_pack_2))
        self.music_pack_3.itemClicked.connect(self.on_item_clicked(self.music_pack_3))
        
        self.pause_btn.clicked.connect(self.pause_and_unpause)
        self.stop_btn.clicked.connect(self.stop_song)
        self.next_btn.clicked.connect(self.next_song)
        self.previous_btn.clicked.connect(self.previous_song)
        # self.loop_btn.clicked.connect(self.loop_one_song)
        # self.shuffle_btn.clicked.connect(self.shuffled_playlist)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
