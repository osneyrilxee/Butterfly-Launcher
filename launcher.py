import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog

# Theme configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ButterflyLauncher(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Butterfly-Launcher")
    self.geometry("520x420")
    self.resizable(False, False)

    # Main title
    self.label_title = ctk.CTkLabel(
        self,
        text="BUTTERFLY LAUNCHER",
        font=ctk.CTkFont(size=20, weight="bold"),
    )
    self.label_title.pack(pady=(20, 10))

    # 1. Game Build Directory Selection
    self.frame_path = ctk.CTkFrame(self)
    self.frame_path.pack(pady=10, padx=20, fill="x")

    self.entry_path = ctk.CTkEntry(
        self.frame_path, placeholder_text="Path to game build folder..."
    )
    self.entry_path.pack(side="left", padx=10, pady=10, expand=True, fill="x")

    self.btn_browse = ctk.CTkButton(
        self.frame_path, text="Browse", width=90, command=self.browse_folder
    )
    self.btn_browse.pack(side="right", padx=10, pady=10)

    # 2. In-Game Username
    self.entry_username = ctk.CTkEntry(
        self, placeholder_text="Enter your username (e.g., Player1)"
    )
    self.entry_username.pack(pady=10, padx=20, fill="x")
    self.entry_username.insert(0, "Player1")

    # 3. Season Selection
    self.combo_season = ctk.CTkOptionMenu(
        self, values=["Season 4 (v4.5)", "Season 6 (v6.21)", "Season 12 (v12.41)"]
    )
    self.combo_season.pack(pady=10, padx=20, fill="x")

    # 4. Option: Local Server Redirection
    self.switch_console = ctk.CTkSwitch(
        self, text="Redirect to local server (127.0.0.1)"
    )
    self.switch_console.pack(pady=15)
    self.switch_console.select()

    # 5. Launch Button
    self.btn_launch = ctk.CTkButton(
        self,
        text="LAUNCH GAME",
        font=ctk.CTkFont(size=16, weight="bold"),
        fg_color="#28a745",
        hover_color="#218838",
        height=45,
        command=self.launch_game,
    )
    self.btn_launch.pack(pady=(10, 20), padx=20, fill="x")

    # Status label
    self.label_status = ctk.CTkLabel(self, text="Ready to launch", text_color="gray")
    self.label_status.pack(pady=5)

  def browse_folder(self):
    folder = filedialog.askdirectory()
    if folder:
      self.entry_path.delete(0, "end")
      self.entry_path.insert(0, folder)

  def launch_game(self):
    game_dir = self.entry_path.get()
    username = self.entry_username.get()

    if not game_dir:
      self.label_status.configure(
          text="Error: Please select a game folder!", text_color="red"
      )
      return

    # Standard relative path to Fortnite Shipping executable
    exe_path = os.path.join(
        game_dir,
        "FortniteGame",
        "Binaries",
        "Win64",
        "FortniteClient-Win64-Shipping.exe",
    )

    if not os.path.exists(exe_path):
      self.label_status.configure(
          text="Error: FortniteClient-Win64-Shipping.exe not found!",
          text_color="red",
      )
      return

    # Standard Fortnite launch arguments
    launch_args = [
        exe_path,
        "-epicapp=Fortnite",
        "-epicenv=Prod",
        "-epiclocale=en-us",
        f"-username={username}",
        "-log",
    ]

    # If local redirection is enabled
    if self.switch_console.get():
      launch_args.append("-http=127.0.0.1")

    try:
      self.label_status.configure(
          text="Launching in progress...", text_color="green"
      )
      # Launch process independently
      subprocess.Popen(launch_args, cwd=os.path.dirname(exe_path))
    except Exception as e:
      self.label_status.configure(
          text=f"Launch error: {str(e)}", text_color="red"
      )


if __name__ == "__main__":
  app = ButterflyLauncher()
  app.mainloop()