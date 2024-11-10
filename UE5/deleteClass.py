if __name__ == '__main__':

    from pathlib import Path
    import tkinter as tk
    from tkinter import filedialog
    from shutil import rmtree
    from datetime import datetime
    from time import sleep

    ### TK setup ###

    root = tk.Tk()
    root.title("Delete File")
    root.resizable(width=tk.FALSE, height=tk.FALSE)

    # Frames for the program functionalities
    inputFrame = tk.Frame(root, height=64)
    inputFrame.grid(row=0, column=0, columnspan=3)

    messageFrame = tk.Frame(root)
    messageFrame.grid(row=1, column=0, columnspan=3)

    submitFrame = tk.Frame(root, height=64)
    submitFrame.grid(row=2, column=0, columnspan=3)



    ### Input frame ###

    # Callback for selecting all in widget, event.widget has to be tk.Entry
    def onclickSelect(event:tk.Event) -> None:
        root.after(50, selectText, event.widget)

    # Select everything in widget
    def selectText(widget:tk.Entry) -> None:
        widget.select_range(0, 'end')
        widget.icursor('end')

    # Open file explorer popup and replace the outputEntry text
    def searchFile(outputEntry:tk.Entry) -> None:
        file = filedialog.askopenfilename(initialdir = path_entry.get())
        if file:
            outputEntry.delete(0, tk.END)
            outputEntry.insert(0, file)


    # Entry for the path, mouse left click bound to onclickSelect
    path_entry = tk.Entry(inputFrame, width="32")
    path_entry.insert(tk.END, Path.cwd()/"source" if (Path.cwd()/"source").is_dir()  else Path.cwd())
    path_entry.pack(padx=4, pady=8, side=tk.LEFT)
    path_entry.bind('<Button>', onclickSelect)

    search_btn = tk.Button(inputFrame, text = 'Search', command = lambda: searchFile(path_entry))
    search_btn.pack(padx=4, pady=8, side=tk.RIGHT)



    ### Message frame ###

    messageText = tk.StringVar()
    messageText.set("Thanks for using my program!")

    message = tk.Label(messageFrame, textvariable=messageText, anchor=tk.CENTER)
    message.pack()



    ### Submit frame ###

    # Main function for deleting files
    def deleteFiles(messageText:tk.StringVar) -> None:

        # Function to delete file
        def deleteFile(file:Path, perma:bool) -> None:
            if perma:
                file.unlink()
            else:
                if (deleteDir/file.name).exists():
                    sleep(.05)
                    (deleteDir/file.name).rename(deleteDir/ str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f_") + file.name))
                file.rename(deleteDir/file.name)

        mainDir = Path()

        filePath = Path(path_entry.get())
        fileDir = filePath.parent

        siblingDir = Path()
        siblingDirStr = ""
        
        # check if file is in private or public, and assign siblingDir to the opposite directory
        if fileDir.name.lower() == "private":
            siblingDirStr = str(Path(fileDir.parent/"public").resolve())
        elif "/private/" in str(fileDir).lower():
            siblingDirStr = str(fileDir.resolve()).lower().rsplit("/private/", 1)
            siblingDirStr.insert(1, "/publilc/")
            siblingDirStr = str().join(siblingDirStr)
        elif "\\private\\" in str(fileDir).lower():
            siblingDirStr = str(fileDir.resolve()).lower().rsplit("\\private\\", 1)
            siblingDirStr.insert(1, "\\public\\")
            siblingDirStr = str().join(siblingDirStr)
        
        elif fileDir.name.lower() == "public":
            siblingDirStr = str(Path(fileDir.parent/"private").resolve())
        elif "/public/" in str(fileDir).lower():
            siblingDirStr = str(fileDir.resolve()).lower().rsplit("/public/", 1)
            siblingDirStr.insert(1, "/private/")
            siblingDirStr = str().join(siblingDirStr)
        elif "\\public\\" in str(fileDir).lower():
            siblingDirStr = str(fileDir.resolve()).lower().rsplit("\\public\\", 1)
            siblingDirStr.insert(1, "\\private\\")
            siblingDirStr = str().join(siblingDirStr)
        else:
            messageText.set("File not following the private or public structure")
            return
        
        siblingDir = Path(siblingDirStr)


        # initial checks
        if not siblingDir.exists():
            messageText.set("Simmetrical sibling does not exist! (in public/ or private/)")
            return
        
        if filePath.is_dir():
            messageText.set("The selected path is a directory\nPlease select a file")
            return
        
        if filePath.suffix not in [".cpp", ".h", ".hpp"]:
            messageText.set("File not associated with C++")
            return
        
        # look for parent that has the expected structure of main project directory
        for parent in filePath.parents:
            if (parent/"source").is_dir() and any(parent.glob('*.uproject')):
                mainDir = parent
                break
        else:
            messageText.set("File structure not found!\nNo parent directory includes *.uproject and source/")
            return

        messageText.set(f"Main directory found!\n{mainDir}")


        if not permaDelete_var.get():
            deleteDir = mainDir/"UE5Utils_deleted"
            deleteDir.mkdir(parents=False, exist_ok=True)

        # delete sibling files
        for path in siblingDir.iterdir():
            if path.suffix.lower() in [".cpp", ".h", ".hpp"] and path.stem == filePath.stem:
                deleteFile(path, permaDelete_var.get())

        # delete files with the same name in same directory
        for path in fileDir.iterdir():
            if path.suffix.lower() in [".cpp", ".h", ".hpp"] and path.stem == filePath.stem:
                deleteFile(path, permaDelete_var.get())

        # delete files that will be regenerated
        rmtree(mainDir/"intermediate", ignore_errors=True)

        for path in mainDir.glob('*.sln'):
            path.unlink() if permaDelete_var.get() else path.replace(deleteDir/path.name)

        messageText.set(messageText.get() + f"\nFiles {"deleted" if permaDelete_var.get() else f"moved to {deleteDir.name}/"}!")

        root.after(5000, root.destroy)


    permaDelete_var = tk.BooleanVar(value=tk.FALSE)
    permaDelete_chk = tk.Checkbutton(submitFrame, text="Permanently delete?", variable=permaDelete_var, onvalue=True, offvalue=False)
    permaDelete_chk.pack(padx=4, pady=8, side=tk.LEFT)

    delete_btn = tk.Button(submitFrame, text = 'DELETE', command = lambda: deleteFiles(messageText))
    delete_btn.pack(padx=4, pady=8, side=tk.RIGHT)


    root.mainloop()
