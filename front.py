import tkinter as tk
from back import IRCClient
from tkinter import messagebox

catppuccin = {
    "background": "#11111b",
    "foreground": "#bac2de",
    "accent": "#b4befe",
    "highlight": "#b4befe",
    "input_bg": "#11111b",
    "input_fg": "#bac2de",
    "button_bg": "#181825",
    "button_fg": "#bac2de",
    "border_color": "#babbf1" 
}

class LavenderIRC:
    def __init__(self, root):
        self.root = root
        self.root.title("LavenderIRC")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg=catppuccin["background"])

        self.connection_frame = tk.Frame(self.root, bg=catppuccin["background"])
        self.connection_frame.pack(pady=20)

        self.widgets()

        self.is_editing = False 

    def widgets(self):

        # LOGO
        logo_label = tk.Label(
            self.root,
            text = "LavenderIRC",
            font = ("Helvetica", 16, "bold"),
            bg = catppuccin["background"],
            fg = catppuccin["foreground"],
        )
        logo_label.pack(pady = 10, padx = 10, anchor = tk.NW)

        self.server_frame = tk.LabelFrame(
            self.connection_frame,
            text="Server:",
            bg=catppuccin["background"],
            fg=catppuccin["foreground"],
            bd=2,  
            relief=tk.FLAT,  
            highlightthickness=0, 
            highlightbackground=catppuccin["border_color"],  
        )
        self.server_frame.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.X)

        self.port_frame = tk.LabelFrame(
            self.connection_frame,
            text="Port:",
            bg=catppuccin["background"],
            fg=catppuccin["foreground"],
            bd=2,  
            relief=tk.FLAT,  
            highlightthickness=0,  
            highlightbackground=catppuccin["border_color"],  
        )
        self.port_frame.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.X)

        self.nick_frame = tk.LabelFrame(
            self.connection_frame,
            text="Nickname:",
            bg=catppuccin["background"],
            fg=catppuccin["foreground"],
            bd=2,  
            relief=tk.FLAT,  
            highlightthickness=0,  
            highlightbackground=catppuccin["border_color"],  
        )
        self.nick_frame.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.X)

        self.channel_frame = tk.LabelFrame(
            self.connection_frame,
            text="Channel:",
            bg=catppuccin["background"],
            fg=catppuccin["foreground"],
            bd=2,  
            relief=tk.FLAT,  
            highlightthickness=0,  
            highlightbackground=catppuccin["border_color"],  
        )
        self.channel_frame.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.X)

        # SERVER INPUT BOX
        self.server_entry = tk.Entry(
            self.server_frame,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightbackground=catppuccin["border_color"],  
            highlightthickness=2,  
            highlightcolor=catppuccin["border_color"], 
        )
        self.server_entry.pack(pady=5, padx=5, fill=tk.X)

        # PORT INPUT BOX
        self.port_entry = tk.Entry(
            self.port_frame,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=catppuccin["border_color"],
            highlightcolor=catppuccin["border_color"],   
        )
        self.port_entry.pack(pady=5, padx=5, fill=tk.X)

        # NICKNAME INPUT BOX
        self.nick_entry = tk.Entry(
            self.nick_frame,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=catppuccin["border_color"],
            highlightcolor=catppuccin["border_color"],   
        )
        self.nick_entry.pack(pady=5, padx=5, fill=tk.X)

        # CHANNEL INPUT BOX
        self.channel_entry = tk.Entry(
            self.channel_frame,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=catppuccin["border_color"],
            highlightcolor=catppuccin["border_color"],   
        )
        self.channel_entry.pack(pady=5, padx=5, fill=tk.X)

        # CONNECT BUTTON
        self.connect_button = tk.Button(
            self.root,
            text="Connect",
            command=self.establish_connection,
            bg=catppuccin["button_bg"],
            fg=catppuccin["button_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightcolor=catppuccin["border_color"],
            highlightbackground=catppuccin["border_color"], 
        )
        self.connect_button.pack(pady=20, side=tk.TOP, fill=tk.NONE, expand=False)

        # DISCONNECT BUTTON
        self.disconnect_button = tk.Button(
            self.root,
            text="Disconnect",
            command=self.disconnect,
            bg=catppuccin["button_bg"],
            fg=catppuccin["button_fg"],
            bd=2,  
            relief=tk.FLAT,
            highlightcolor=catppuccin["border_color"], 
        )
        self.disconnect_button.pack_forget()

        # EDIT CONNECTION BUTTON
        self.edit_connection_button = tk.Button(
            self.root,
            text="Edit Connection",
            command=self.toggle_edit_connection,
            bg=catppuccin["button_bg"],
            fg=catppuccin["button_fg"],
            bd=2,
            highlightcolor=catppuccin["border_color"],   
            relief=tk.FLAT,
        )
        self.edit_connection_button.pack_forget()

        # DISPLAY AREA
        self.text_area = tk.Text(
            self.root,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            bd=0,
            highlightthickness=0,
            highlightbackground=catppuccin["border_color"],  
            relief=tk.FLAT,
            state=tk.DISABLED, 
            cursor="",
            selectbackground=catppuccin["background"],
        )
        self.text_area.pack(
            pady=5,
            padx=10,
            fill=tk.BOTH,
            expand=True
        )

        # MESSAGE INPUT
        self.entry = tk.Entry(
            self.root,
            bg=catppuccin["input_bg"],
            fg=catppuccin["input_fg"],
            insertbackground=catppuccin["input_fg"],
            highlightbackground=catppuccin["border_color"],
            bd=2,
            highlightthickness=2,
            highlightcolor=catppuccin["border_color"], 
            relief=tk.FLAT,
            selectbackground=catppuccin["background"],
        )
        self.entry.pack(
            pady=5,
            padx=10,
            fill=tk.X,
            side=tk.LEFT,
            expand=True
        )
        self.entry.bind("<Return>", self.send_message)

    def establish_connection(self):
        server = self.server_entry.get()
        port = self.port_entry.get()
        nickname = self.nick_entry.get()
        channel = self.channel_entry.get()

        self.client = IRCClient(server, port, nickname, channel, self.update_text_area)
        self.client.start()

        self.hide_connection_inputs()

        self.disconnect_button.pack(pady=10, side=tk.RIGHT)
        self.edit_connection_button.pack(pady=10, side=tk.RIGHT)

        self.connect_button.pack_forget()
        self.root.after(1500, self.clear_chat)

    def hide_connection_inputs(self):
        self.connection_frame.pack_forget()

    def show_connection_inputs(self):
        self.connection_frame.pack(pady=20)

    def toggle_edit_connection(self):
        if self.is_editing:
            self.hide_connection_inputs()
            self.is_editing = False
        else:
            self.show_connection_inputs()
            self.is_editing = True

    def disconnect(self):
        if hasattr(self, 'client') and self.client:
            self.client.stop()
            del self.client 
        self.show_connection_inputs()
        self.disconnect_button.pack_forget()
        self.edit_connection_button.pack_forget()
        self.connect_button.pack(pady=20)

    def send_message(self, event):
        if hasattr(self, 'client') and self.client:
            message = self.entry.get()
            if message.strip():
                self.client.send_message(message) 
                self.entry.delete(0, tk.END)

    def update_text_area(self, message):
        self.text_area.config(state=tk.NORMAL)  
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)  
        self.text_area.config(state=tk.DISABLED)  

    def clear_chat(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = LavenderIRC(root)
    root.mainloop()
