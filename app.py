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

    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()

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

        except :
            showerror( title = "Invalid Link", message = "Invalid Link Passed!!")

    def downloderPage(self) :

        # Defining Structure
        video_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        video_page.pack( fill = "both", expand = True )

        # Heading
        video_page.create_text( 700, 120, text = "YouTube Video Downloder", 
                            font = ( "Georgia", 42, "bold" ), fill = "#1c54df" )

        # Link Entry Box
        refLink = ctk.CTkEntry( master = video_page, 
                                 placeholder_text = "Insert Video/Playlist Link Here", text_font = ( "Georgia", 20 ), 
                                  width = 550, height = 30, corner_radius = 14,
                                   placeholder_text_color = "#666666", text_color = "#191919", 
                                    fg_color = "#e1f5ff", bg_color = "black", 
                                     border_color = "white", border_width = 3)
        refLink_win = video_page.create_window( 325, 320-120, anchor = "nw", window = refLink )

        display_area = ctk.CTkFrame( master = video_page, 
                                      width = 800, height = 400, corner_radius = 30,
                                       bg_color = "black", fg_color = "grey",
                                        border_color = "white", border_width = 6)
        display_area.place_configure( x = 270, y = 300, anchor = "nw")

        # Label in frame
        frm_label = ctk.CTkLabel( master = display_area, 
                                   text = "NOTE:-\nDon't insert or enter\nshared video link.\nEnter link of video or\nplaylist after opening the\nvideo and playlist.", text_font = ("Georgia", 20),
                                    width = 200, height = 50, corner_radius = 15,
                                     bg_color = "grey", fg_color = "white", text_color = "red"  )
        frm_label.place_configure( x = 300, y = 120, anchor = "nw" )

        refLink.bind('<Return>', lambda event = None : self.checkandDownload( refLink.get(), display_area, video_page ) )

        # Download Button
        download_bt = ctk.CTkButton( master = video_page, 
                                      text = "Download", text_font = ( "Georgia", 20 ), 
                                       width = 100, height = 40, corner_radius = 18,
                                        bg_color = "black", fg_color = "red", 
                                         hover_color = "#ff5359", border_width = 0, 
                                          command = lambda : self.checkandDownload( refLink.get(), display_area, video_page ) )
        download_bt_win = video_page.create_window( 1030, 320-120, anchor = "nw", window = download_bt )

        # Return Button
        ret_bt = ctk.CTkButton( master = video_page, 
                                 text = "Back", text_font = ( "Georgia", 20 ), 
                                  width = 100, height = 50, corner_radius = 18,
                                   bg_color = "black", fg_color = "red", 
                                    hover_color = "#ff5359", border_width = 0, 
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

        # Heading
        first_page.create_text( 400, 119, text = "Video Downloader", 
                                font = ( "Georgia", 42, "bold" ), fill = "#ec1c24" )

        # Next Page Button
        next_bt = ctk.CTkButton( master = first_page, 
                                  text = "Let's Go ->", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 40, corner_radius = 18,
                                    bg_color = "#fecc8f", fg_color = "#ec1c24", 
                                     hover_color = "#ff5359", border_width = 0,
                                      text_color = "white",
                                       command = lambda : self.change( first_page, self.downloderPage) )
        next_bt_win = first_page.create_window( 320, 720, anchor = "nw", window = next_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    download_class = VideoDownloder()
    download_class.firstPage()
