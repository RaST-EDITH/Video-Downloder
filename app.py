# Library and Modules used 
import os                                                    # pip install os ( In case if not present )
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3
from PIL import Image ,ImageTk                               # pip install pillow==9.3.0
from pytube import YouTube, Playlist                         # pip install pytube==15.0.0
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo

class VideoDownloder :
    
    def __init__(self) :

        ctk.set_appearance_mode( "dark" )
        ctk.set_default_color_theme( "dark-blue" )
        self.width = 1200
        self.height = 700
        self.root = ctk.CTk()
        self.root.title( "Video Downloader" )
        self.root.geometry( "1200x700+200+80" )
        self.root.resizable( False, False )
        self.first_back_image = self.Imgo( os.path.join( os.getcwd(), r"Design\FrontPage.jpg" ), 1498, 875)
        self.second_back_image = self.Imgo( os.path.join( os.getcwd(), r"Design\SecondPage.jpg" ), 1498, 875)
        self.back = self.Imgo( os.path.join( os.getcwd(), r"Design\arrow.png" ), 40, 30 )

    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()

    def Imgo( self, file, w, h ) :

        # Image processing
        img = Image.open(file)
        pht = ImageTk.PhotoImage( img.resize((w,h), Image.Resampling.LANCZOS ))
        return pht

    def checkandDownload( self, link, frame, can ) :

        try :

            if ( 'youtube' in link ) :

                if ( 'watch' in link ) :

                    # Getting path of folder from dialog
                    open_folder = filedialog.askdirectory( initialdir = os.getcwd() ,title = "Browse Folder")
                    if ( open_folder == "" ) :
                        showerror( title = "Empty Field", message = "Enter or Select proper path")
                    
                    else :

                        from pytube import YouTube
                        ref = YouTube(link)
                        showinfo( title = "Started...", message = "Downloading Started\n     Successfully" )
                        ref.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(open_folder)

                        details = {
                            # "image" : ref.thumbnail_url,
                            "title" : ref.title,
                            "views" : ref.views,
                            "author" : ref.author,
                            "status" : "Video Downloaded\nSuceesfully\n",
                            "path" : ref.title + ".mp4"
                        }

                        frame.destroy()

                        # Frame
                        frame = ctk.CTkFrame( master = can, 
                                               width = 800, height = 400, corner_radius = 30,
                                                bg_color = "black", fg_color = "grey",
                                                 border_color = "white", border_width = 6)
                        frame.place_configure( x = 270, y = 300, anchor = "nw")

                        # Title Label
                        if ( len(details["title"]) > 70 ) :
                            details["title"] = details["title"][:69] + "..."

                        title = ctk.CTkLabel( master = frame, 
                                               text = details["title"], text_font = ("Georgia", 20),
                                                height = 50, corner_radius = 15,
                                                 bg_color = "grey", fg_color = "white", text_color = "red"  )
                        title.place_configure( x = 50, y = 50, anchor = "nw" )

                        # Author Label
                        author = ctk.CTkLabel( master = frame, 
                                                text = "Author", text_font = ("Georgia", 18),
                                                 width = 100, height = 50, corner_radius = 15,
                                                  bg_color = "grey", fg_color = "white", text_color = "red"  )
                        author.place_configure( x = 50, y = 140, anchor = "nw" )

                        author_val = ctk.CTkLabel( master = frame, 
                                                    text = details["author"], text_font = ("Georgia", 18),
                                                     width = 100, height = 50, corner_radius = 15,
                                                      bg_color = "grey", fg_color = "white", text_color = "red"  )
                        author_val.place_configure( x = 100, y = 220, anchor = "nw" )

                        # Views Label
                        views = ctk.CTkLabel( master = frame, 
                                               text = "Views", text_font = ("Georgia", 18),
                                                width = 100, height = 50, corner_radius = 15,
                                                 bg_color = "grey", fg_color = "white", text_color = "red"  )
                        views.place_configure( x = 50, y = 300, anchor = "nw" )

                        views_val = ctk.CTkLabel( master = frame, 
                                                   text = details["views"], text_font = ("Georgia", 18),
                                                    width = 100, height = 50, corner_radius = 15,
                                                     bg_color = "grey", fg_color = "white", text_color = "red"  )
                        views_val.place_configure( x = 100, y = 380, anchor = "nw" )

                        # Status Label
                        status_chk = ctk.CTkLabel( master = frame, 
                                                    text = details["status"], text_font = ("Georgia", 18),
                                                     width = 360, height = 230, corner_radius = 15,
                                                      bg_color = "grey", fg_color = "white", text_color = "red"  )
                        status_chk.place_configure( x = 500, y = 150, anchor = "nw" )

                        # File Open Button
                        open_bt = ctk.CTkButton( master = can, 
                                                  text = "Open >", text_font = ( "Georgia", 18), 
                                                   width = 100, height = 40, corner_radius = 15,
                                                    bg_color = "white", fg_color = "red", 
                                                     hover_color = "#ff5359", border_width = 0, 
                                                      command = lambda : os.startfile( open_folder) )
                        open_bt_win = can.create_window( 930, 650, anchor = "nw", window = open_bt )
                
                elif ( 'playlist' in link ) :

                    # Getting path of folder from dialog
                    open_folder = filedialog.askdirectory( initialdir = os.getcwd() ,title = "Browse Folder")
                    if ( open_folder == "" ) :
                        showerror( title = "Empty Field", message = "Enter or Select proper path")
                    
                    else :

                        from pytube import Playlist
                        all_videos = Playlist(link)
                        details = {
                            "title" : all_videos.title,
                            "Number of videos" : all_videos.length,
                            "owner" : all_videos.owner,
                            "views" : all_videos.views,
                            "status" : "Playlist Downloaded\nSuccessfully\n"
                        }

                        showinfo( title = "Started..", message = "Playlist Downloading\n         Started" )
                        for vid in all_videos.videos :
                            vid.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(os.path.join(open_folder, all_videos.title))

                        frame.destroy()

                        # Frame
                        frame = ctk.CTkFrame( master = can, 
                                               width = 800, height = 400, corner_radius = 30,
                                                bg_color = "black", fg_color = "grey",
                                                 border_color = "white", border_width = 6)
                        frame.place_configure( x = 270, y = 300, anchor = "nw")

                        # Title Label
                        if ( len(details["title"]) > 70 ) :
                            details["title"] = details["title"][:69] + "..."

                        title = ctk.CTkLabel( master = frame, 
                                               text = details["title"], text_font = ("Georgia", 18),
                                                height = 50, corner_radius = 15,
                                                 bg_color = "grey", fg_color = "white", text_color = "red"  )
                        title.place_configure( x = 50, y = 50, anchor = "nw" )

                        # Author Label
                        author = ctk.CTkLabel( master = frame, 
                                                text = "Owner", text_font = ("Georgia", 15),
                                                 width = 100, height = 40, corner_radius = 15,
                                                  bg_color = "grey", fg_color = "white", text_color = "red"  )
                        author.place_configure( x = 50, y = 130, anchor = "nw" )

                        author_val = ctk.CTkLabel( master = frame, 
                                                    text = details["owner"], text_font = ("Georgia", 15),
                                                     width = 100, height = 40, corner_radius = 15,
                                                      bg_color = "grey", fg_color = "white", text_color = "red"  )
                        author_val.place_configure( x = 100, y = 200-10, anchor = "nw" )

                        # Views Label
                        views = ctk.CTkLabel( master = frame, 
                                               text = "Views", text_font = ("Georgia", 15),
                                                width = 100, height = 40, corner_radius = 15,
                                                 bg_color = "grey", fg_color = "white", text_color = "red"  )
                        views.place_configure( x = 50, y = 300-50, anchor = "nw" )

                        views_val = ctk.CTkLabel( master = frame, 
                                                   text = details["views"], text_font = ("Georgia", 15),
                                                    width = 100, height = 40, corner_radius = 15,
                                                     bg_color = "grey", fg_color = "white", text_color = "red"  )
                        views_val.place_configure( x = 100, y = 380-70, anchor = "nw" )

                        # Number of Videos Label
                        vid_count = ctk.CTkLabel( master = frame, 
                                                   text = "Views", text_font = ("Georgia", 15),
                                                    width = 100, height = 40, corner_radius = 15,
                                                     bg_color = "grey", fg_color = "white", text_color = "red"  )
                        vid_count.place_configure( x = 50, y = 370, anchor = "nw" )

                        vid_count_val = ctk.CTkLabel( master = frame, 
                                                       text = details["Number of videos"], text_font = ("Georgia", 15),
                                                        width = 100, height = 40, corner_radius = 15,
                                                         bg_color = "grey", fg_color = "white", text_color = "red"  )
                        vid_count_val.place_configure( x = 100, y = 430, anchor = "nw" )

                        # Status Label
                        status_chk = ctk.CTkLabel( master = frame, 
                                                    text = details["status"], text_font = ("Georgia", 18),
                                                     width = 360, height = 230, corner_radius = 15,
                                                      bg_color = "grey", fg_color = "white", text_color = "red"  )
                        status_chk.place_configure( x = 500, y = 150, anchor = "nw" )

                        # File Open Button
                        open_bt = ctk.CTkButton( master = can, 
                                                  text = "Open >", text_font = ( "Georgia", 18), 
                                                   width = 100, height = 40, corner_radius = 15,
                                                    bg_color = "white", fg_color = "red", 
                                                     hover_color = "#ff5359", border_width = 0, 
                                                      command = lambda : os.startfile( os.path.join(open_folder, all_videos.title)) )
                        open_bt_win = can.create_window( 930, 650, anchor = "nw", window = open_bt )

                else :
                    showerror( title = "Invalid Link", message = "Invalid Link Passed")
        
            else :
                showerror( title = "Invalid Link", message = "Invalid Link Passed!")

        except :
            showerror( title = "Invalid Link", message = "Invalid Link Passed!!")

    def downloderPage(self) :

        # Defining Structure
        video_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        video_page.pack( fill = "both", expand = True )

        # Background Image
        video_page.create_image( 0, 0, image = self.second_back_image , anchor = "nw")

        # Heading
        video_page.create_text( 720, 195, text = "YouTube Video Downloder", 
                            font = ( "Georgia", 36, "bold" ), fill = "#ec1c24" )

        # Link Entry Box
        refLink = ctk.CTkEntry( master = video_page, 
                                 placeholder_text = "Insert Video/Playlist Link Here", text_font = ( "Georgia", 20 ), 
                                  width = 570, height = 30, corner_radius = 14,
                                   placeholder_text_color = "#666666", text_color = "#191919", 
                                    fg_color = "#e1f5ff", bg_color = "#e7e7e7", 
                                     border_color = "white", border_width = 3)
        refLink_win = video_page.create_window( 300, 240, anchor = "nw", window = refLink )

        display_area = ctk.CTkFrame( master = video_page, 
                                      width = 765, height = 360, corner_radius = 25,
                                       bg_color = "#e7e7e7", fg_color = "grey",
                                        border_color = "white", border_width = 4)
        display_area.place_configure( x = 280, y = 300, anchor = "nw")

        # Label in frame
        frm_label = ctk.CTkLabel( master = display_area, 
                                   text = "NOTE:-\nDon't insert or enter\nshared video link.\nEnter link of video or\nplaylist after opening the\nvideo and playlist.", 
                                    text_font = ("Georgia", 18), width = 200, height = 50, corner_radius = 15,
                                     bg_color = "grey", fg_color = "white", text_color = "red"  )
        frm_label.place_configure( x = 300, y = 110, anchor = "nw" )

        refLink.bind('<Return>', lambda event = None : self.checkandDownload( refLink.get(), display_area, video_page ) )

        # Download Button
        download_bt = ctk.CTkButton( master = video_page, 
                                      text = "Download", text_font = ( "Georgia", 20 ), 
                                       width = 50, height = 38, corner_radius = 18,
                                        bg_color = "#e7e7e7", fg_color = "red", 
                                         hover_color = "#ff5359", border_width = 0, text_color = "white",
                                          command = lambda : self.checkandDownload( refLink.get(), display_area, video_page ) )
        download_bt_win = video_page.create_window( 1025, 240, anchor = "nw", window = download_bt )

        # Return Button
        ret_bt = ctk.CTkButton( master = video_page, 
                                image = self.back, text = None,
                                  width = 60, height = 40, corner_radius = 23,
                                   bg_color = "#f54343", fg_color = "red", 
                                    hover_color = "#ff5359", border_width = 4, border_color = "white",
                                     command = lambda : self.change( video_page, self.firstPage) )
        ret_bt_win = video_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

        self.root.mainloop()

    def firstPage(self) :

        # Defining Structure
        first_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        first_page.pack( fill = "both", expand = True )

        # Background Image
        first_page.create_image( 0, 0, image = self.first_back_image , anchor = "nw")

        # Heading
        first_page.create_text( 1100-40, 300-40, text = "      Video\nDownloader", 
                                font = ( "Georgia", 40, "bold" ), fill = "#ec1c24" )
        first_page.create_text( 1060, 400, text = "Your personalized YouTube", 
                                font = ( "Georgia", 20, "bold"), fill = "black" )
        first_page.create_text( 1070, 400+40, text = "Video and Playlist", 
                                font = ( "Georgia", 20, "bold"), fill = "black" )
        first_page.create_text( 1070, 400+80, text = "Downloader.", 
                                font = ( "Georgia", 20, "bold"), fill = "black" )


        # Next Page Button
        next_bt = ctk.CTkButton( master = first_page, 
                                  text = "Let's Go ->", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 40, corner_radius = 18,
                                    bg_color = "#e6e6e6", fg_color = "#ec1c24", 
                                     hover_color = "#ff5359", border_width = 0,
                                      text_color = "white",
                                       command = lambda : self.change( first_page, self.downloderPage) )
        next_bt_win = first_page.create_window( 1000-30, 600, anchor = "nw", window = next_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    download_class = VideoDownloder()
    download_class.firstPage()
