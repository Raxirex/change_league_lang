import os
import tkinter as tk
from tkinter import ttk, filedialog

def change_language():
    league_path = league_path_entry.get().strip()
    selected_language = language_var.get()
    config_path = os.path.join(league_path, 'Config', 'LeagueClientSettings.yaml')

    if not league_path or not os.path.exists(config_path):
        error_label.config(text="Invalid League of Legends path.")
        return

    try:
        with open(config_path, 'r') as file:
            content = file.readlines()

        for i, line in enumerate(content):
            if 'locale:' in line:
                content[i] = f"  locale: \"{selected_language}\"\n"

        with open(config_path, 'w') as file:
            file.writelines(content)

        error_label.config(text="")
        status_bar.config(text="Language changed successfully!")
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")

def browse_path():
    path = filedialog.askdirectory()
    if path:
        league_path_entry.delete(0, tk.END)
        league_path_entry.insert(0, path)

root = tk.Tk()
root.title("League of Legends Language Changer")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0)

league_path_label = ttk.Label(main_frame, text="League of Legends Path:")
league_path_label.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
league_path_entry = ttk.Entry(main_frame, width=40)
league_path_entry.grid(row=0, column=1, pady=(0, 10), sticky=tk.W)
browse_button = ttk.Button(main_frame, text="Browse", command=browse_path)
browse_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky=tk.W)

language_label = ttk.Label(main_frame, text="Select Language:")
language_label.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
language_var = tk.StringVar()
language_combobox = ttk.Combobox(main_frame, textvariable=language_var, width=38, state="readonly")
language_combobox["values"] = ("en_US", "es_ES", "de_DE", "fr_FR", "it_IT", "pl_PL", "ro_RO", "el_GR", "ru_RU", "tr_TR", "ko_KR", "zh_TW", "ja_JP")
language_combobox.grid(row=1, column=1, pady=(0, 10), sticky=tk.W)

change_button = ttk.Button(main_frame, text="Change Language", command=change_language)
change_button.grid(row=2, column=1, pady=(0, 10), sticky=tk.W)

error_label = ttk.Label(main_frame, text="", foreground="red")
error_label.grid(row=3, column=1, sticky=tk.W)

status_bar = ttk.Label(main_frame, text="", relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(row=4, column=0, columnspan=3, sticky="we")

root.mainloop()
