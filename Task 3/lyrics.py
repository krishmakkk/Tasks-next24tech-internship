import tkinter as tk
from tkinter import messagebox, ttk
import lyricsgenius
import threading

# Function to get the top 10 songs by the artist
def get_top_songs():
    def fetch():
        token = "t7hSbULchG2T9YTuGNAun19tSXwy9qv5mA0fsYqa6OlPIOjnn1iSNjsHhITFeaey"
        genius = lyricsgenius.Genius(token)

        artist_name = artist_entry.get()
        status_label.config(text="Loading...")

        if artist_name:
            try:
                artist = genius.search_artist(artist_name, max_songs=10, sort="title")
                if artist and artist.songs:
                    song_titles = [song.title for song in artist.songs]
                    song_combobox['values'] = song_titles
                    if song_titles:
                        song_combobox.current(0)
                        status_label.config(text="Songs loaded successfully.")
                    else:
                        song_combobox.set('No songs found')
                        status_label.config(text="No songs found.")
                else:
                    messagebox.showerror("Error", "Artist not found or no songs available!")
                    status_label.config(text="")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                status_label.config(text="")
        else:
            messagebox.showwarning("Input Error", "Please enter the artist name.")
            status_label.config(text="")
    
    threading.Thread(target=fetch).start()

# Function to get the song lyrics
def get_lyrics():
    token = "NKIMYvxBD8NhSzltTJC7RBdgGPYNp0irZk1MZKdZCcAwKFmtijYqoBu5VovoU99A"
    genius = lyricsgenius.Genius(token)

    artist_name = artist_entry.get()
    song_title = song_combobox.get()

    if artist_name and song_title:
        try:
            song = genius.search_song(song_title, artist_name)
            if song:
                lyrics_text.delete(1.0, tk.END)
                lyrics_text.insert(tk.END, song.lyrics)
            else:
                messagebox.showerror("Error", "Song not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")

# Creating the GUI window
root = tk.Tk()
root.title("Lyrics Finder")
root.geometry("700x600")

# Main frame
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Artist label and entry
artist_label = ttk.Label(main_frame, text="Artist Name:")
artist_label.grid(row=0, column=0, pady=5, sticky=tk.W)
artist_entry = ttk.Entry(main_frame, width=50)
artist_entry.grid(row=0, column=1, pady=5, padx=10)

# Get top songs button
top_songs_button = ttk.Button(main_frame, text="Get Top Songs", command=get_top_songs)
top_songs_button.grid(row=0, column=2, pady=5, padx=10)

# Song label and combobox
song_label = ttk.Label(main_frame, text="Song Title:")
song_label.grid(row=1, column=0, pady=5, sticky=tk.W)
song_combobox = ttk.Combobox(main_frame, width=47)
song_combobox.grid(row=1, column=1, pady=5, padx=10)

# Search button
search_button = ttk.Button(main_frame, text="Get Lyrics", command=get_lyrics)
search_button.grid(row=1, column=2, pady=5, padx=10)

# Status label to display loading status
status_label = ttk.Label(main_frame, text="")
status_label.grid(row=2, column=0, columnspan=3, pady=5)

# Text box to display lyrics
lyrics_text = tk.Text(main_frame, wrap='word', height=20, width=80)
lyrics_text.grid(row=3, column=0, columnspan=3, pady=10, padx=10)

# Quit button
quit_button = ttk.Button(main_frame, text="Quit", command=root.quit)
quit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Add some styling
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))

# Run the application
root.mainloop()
