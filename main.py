import os
import shutil
from tkinter import Tk, Button, filedialog, messagebox, Label

class FileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("920x250")

        ascii_art_title = """                                                     
                                                     .-'''-.                                                                                               
              .---.                                 '   _    \                                                                                             
          .--.|   |      __.....__                /   /` '.   \                                _..._   .--.                __.....__                       
     _.._ |__||   |  .-''         '.             .   |     \  '           .--./)             .'     '. |__|            .-''         '.                     
   .' .._|.--.|   | /     .-''"'-.  `.           |   '      |  '.-,.--.  /.''\\             .   .-.   ..--.           /     .-''"'-.  `. .-,.--.           
   | '    |  ||   |/     /________\   \          \    \     / / |  .-. || |  | |      __    |  '   '  ||  |          /     /________\   \|  .-. |          
 __| |__  |  ||   ||                  |           `.   ` ..' /  | |  | | \`-' /    .:--.'.  |  |   |  ||  |.--------.|                  || |  | |          
|__   __| |  ||   |\    .-------------'              '-...-'`   | |  | | /("'`    / |   \ | |  |   |  ||  ||____    |\    .-------------'| |  | |          
   | |    |  ||   | \    '-.____...---.                         | |  '-  \ '---.  `" __ | | |  |   |  ||  |    /   /  \    '-.____...---.| |  '-           
   | |    |__||   |  `.             .'                          | |       /'""'.\  .'.''| | |  |   |  ||__|  .'   /    `.             .' | |               
   | |        '---'    `''-...... -'                            | |      ||     ||/ /   | |_|  |   |  |     /    /___    `''-...... -'   | |               
   | |                                                          |_|      \'. __// \ \._,\ '/|  |   |  |    |         |                   |_|               
   |_|                                                                    `'---'   `--'  `" '--'   '--'    |_________|                                     """

        label = Label(self.root, text=ascii_art_title, font=("Courier", 10))
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        btn = Button(self.root, text="Select Folder to Organize", command=self.select_directory)
        btn.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    def organize_files(self, directory):
        file_types = {
            'Music': ['.mp3', '.wav', '.flac'],
            'Videos': ['.mp4', '.mkv', '.flv', '.mpeg', '.mov', '.avi', '.wmv', '.m4v'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.yaml', '.json', '.xml', '.html', '.md', '.pptx',
                          '.doc', '.pem', '.pub', '.key', '.crt', '.csr', '.p12', '.pfx', '.p7b', '.p7r', '.p7c',
                          '.py', '.js', '.dotx', '.rtf', '.RTF', '.ipynb', '.yml', '.YML', '.yaml', '.YAML', '.json',
                          '.db'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.HEIC', '.HEIF', '.tif', '.tiff', '.bmp', '.svg', '.ico',
                       '.JPG', '.heic'],
        }

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_ext = os.path.splitext(filename)[1]
                if file_ext in ['.zip', '.dmg', '.pkg', '.bin', '.ova', '.tar']:
                    os.remove(filepath)
                    continue
                for category, extensions in file_types.items():
                    if file_ext in extensions:
                        category_path = os.path.join(directory, category)
                        if not os.path.exists(category_path):
                            os.makedirs(category_path)
                        shutil.move(filepath, os.path.join(category_path, filename))
                        break

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.organize_files(directory)
            messagebox.showinfo("Success", "Files organized successfully!")

if __name__ == "__main__":
    root = Tk()
    organizer = FileOrganizer(root)
    root.mainloop()