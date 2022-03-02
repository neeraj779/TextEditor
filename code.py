import tkinter
from tkinter import Button, Scrollbar, Tk, ttk
from tkinter import messagebox, font, colorchooser, filedialog
import os


root = Tk()
root.geometry("1000x600")
root.title("Notepad")
root.wm_iconbitmap("assets/notepad.ico")
main_menu = tkinter.Menu()

####### File #####
file = tkinter.Menu(main_menu, tearoff=False)

# file icon
new_icon = tkinter.PhotoImage(file="assets/new.png")
open_icon = tkinter.PhotoImage(file="assets/open.png")
save_icon = tkinter.PhotoImage(file="assets/save.png")
save_as_icon = tkinter.PhotoImage(file="assets/save_as.png")
exit_icon = tkinter.PhotoImage(file="assets/exit.png")


###### edit #######
edit = tkinter.Menu(main_menu, tearoff=False)

# edit icons
copy_icon = tkinter.PhotoImage(file="assets/copy.png")
paste_icon = tkinter.PhotoImage(file="assets/paste.png")
cut_icon = tkinter.PhotoImage(file="assets/cut.png")
clear_all_icon = tkinter.PhotoImage(file="assets/clear_all.png")
find_icon = tkinter.PhotoImage(file="assets/find.png")


############# View ##############
view = tkinter.Menu(main_menu, tearoff=False)

# view icon
staus_bar_icon = tkinter.PhotoImage(file="assets/status_bar.png")
tool_bar_icon = tkinter.PhotoImage(file="assets/tool_bar.png")


################ color theme ##############

color_theme = tkinter.Menu(main_menu, tearoff=False)
theme_selection = tkinter.StringVar()

# color theme icon

light_default_icon = tkinter.PhotoImage(file="assets/light_default.png")
light_plus_icon = tkinter.PhotoImage(file="assets/light_plus.png")
dark_icon = tkinter.PhotoImage(file="assets/dark.png")
red_icon = tkinter.PhotoImage(file="assets/red.png")
monokai_icon = tkinter.PhotoImage(file="assets/monokai.png")
night_blue_icon = tkinter.PhotoImage(file="assets/night_blue.png")

# cascadin menu bars
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)


tool_bar = ttk.Label(root)
tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)

# font box
font_tuple = font.families()
font_selection = tkinter.StringVar()
font_box = ttk.Combobox(
    tool_bar, width=30, textvariable=font_selection, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(padx=7)

# size box
font_size_selection = tkinter.IntVar()
font_size = ttk.Combobox(
    tool_bar, width=14, textvariable=font_size_selection, state="readonly")
font_size["values"] = tuple(range(4, 100, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=7)

# bold button
bold_icon = tkinter.PhotoImage(file="assets/bold.png")
bold_button = Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=2)

# italic button
italic_icon = tkinter.PhotoImage(file="assets/italic.png")
italic_button = Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=2)

# underline button
underline_icon = tkinter.PhotoImage(file="assets/underline.png")
under_line_button = Button(tool_bar, image=underline_icon)
under_line_button.grid(row=0, column=4, padx=2)

# font color Button
font_color_icon = tkinter.PhotoImage(file="assets/font_color.png")
font_color_button = Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=2)

# align left
align_left_icon = tkinter.PhotoImage(file="assets/align_left.png")
align_left_button = Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=6, padx=2)

# align center
align_center_icon = tkinter.PhotoImage(file="assets/align_center.png")
align_center_button = Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=7, padx=2)

# align right
align_right_icon = tkinter.PhotoImage(file="assets/align_right.png")
align_right_button = Button(tool_bar, image=align_left_icon)
align_right_button.grid(row=0, column=8, padx=2)


text_editor = tkinter.Text(root)
text_editor.config(wrap="word", relief=tkinter.SUNKEN)
text_editor.focus_set()
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text_editor.pack(expand=1, fill=tkinter.BOTH)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.configure(font=("Arial", 12))

# font implementation
current_font_family = "Arial"
current_font_size = 12


def change_font(event=None):
    global current_font_family
    current_font_family = font_selection.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(event=None):
    global current_font_size
    current_font_size = font_size_selection.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)

# button implementation


def change_bold():
    text_property = tkinter.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(
            font=(current_font_size, current_font_size, "bold"))

    elif text_property.actual()["weight"] == "bold":
        text_editor.configure(
            font=(current_font_size, current_font_size, "normal"))


bold_button.configure(command=change_bold)


# italic implementation
def change_italic():
    text_property = tkinter.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(
            font=(current_font_size, current_font_size, "italic"))

    elif text_property.actual()["slant"] == "italic":
        text_editor.configure(
            font=(current_font_size, current_font_size, "roman"))


italic_button.configure(command=change_italic)


# underline implementation
def change_underline():
    text_property = tkinter.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(
            font=(current_font_size, current_font_size, "underline"))

    elif text_property.actual()["underline"] == 1:
        text_editor.configure(font=(current_font_size, current_font_size))


under_line_button.configure(command=change_underline)


# chnage font color
def font_color_picker():
    color_var = colorchooser.askcolor()
    text_editor.configure(foreground=color_var[1])


font_color_button.configure(command=font_color_picker)

# align functionality


def align_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tkinter.LEFT)
    text_editor.delete(1.0, tkinter.END)
    text_editor.insert(tkinter.INSERT, text_content, "left")


align_left_button.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tkinter.CENTER)
    text_editor.delete(1.0, tkinter.END)
    text_editor.insert(tkinter.INSERT, text_content, "center")


align_center_button.configure(command=align_center)


def align_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tkinter.RIGHT)
    text_editor.delete(1.0, tkinter.END)
    text_editor.insert(tkinter.INSERT, text_content, "right")


align_right_button.configure(command=align_right)


def about():
    window = tkinter.Toplevel()
    window.title("About Notepad")
    window.geometry("600x250")
    window.minsize(530, 220)
    window.maxsize(700, 300)
    ttk.Label(window, text="Notepad By Neeraj\n" ,font=("cascadiacode",
              20, "bold",)).grid(row=0, column=0, padx=150)
    ttk.Label(window, text="GNU General Public License", font=(
        "cascadiacode", 12, "bold")).grid(row=1, column=0, padx=100)
    ttk.Label(window, text="This program is free software; you can redistributeit and/or\nmodify it under the terms of the GNU General Public License\n",
              font=("cascadiacode", 12, "bold")).grid(row=2, column=0, padx=50)
    ttk.Label(window, text=" : Devloper Social media hadles : ", font=("Arial",10, "bold")).grid(row=4, column=0, sticky=tkinter.W)
    ttk.Label(window, text="github : github.com/neeraj779").grid(row=5, column=0, sticky=tkinter.W)
    ttk.Label(window, text="Twitter : twitter.com/neeraj9271").grid(row=6, column=0,sticky=tkinter.W)
    window.mainloop()


main_menu.add_command(label="About", command=about)

status_bar = ttk.Label(root, text="Status Bar")
status_bar.pack(side=tkinter.BOTTOM)


text_changed = False


def status(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        chracters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(
            text=f"Characters : {chracters} Words {words} | Windows(CR LF) | UTF-8")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", status)

#### file toolbar functions ####

url = ""

# new


def new_file(event=None):
    text_editor.delete(1.0, tkinter.END)

# open


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="Select file", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    try:
        with open(url, "r") as user_file:
            text_editor.delete(1.0, tkinter.END)
            text_editor.insert(1.0, user_file.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))

# save file


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tkinter.END))
            with open(url, "w", encoding="utf-8") as user_file:
                user_file.write(content)
        else:
            url = filedialog.asksaveasfile(
                mode="w", defaultextension="*.txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
            content2 = text_editor.get(1.0, tkinter.END)
            url.write(content2)
            url.close()
    except:
        return

# save as


def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tkinter.END)
        url = filedialog.asksaveasfile(
            mode="w", defaultextension="*.txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        url.write(content)
        url.close()
    except:
        return

# exit


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                "Warning", "Do you want to save this file?")
            if mbox is True:
                if url:
                    content = str(text_editor.get(1.0, tkinter.END))
                    with open(url, "w", encoding="utf-8") as user_file:
                        user_file.write(content)
                        root.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tkinter.END))
                    url = filedialog.asksaveasfile(
                        mode="w", defaultextension="*.txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


# file commands
file.add_command(label="New", image=new_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+N", command=new_file)
file.add_command(label="Open", image=open_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+O", command=open_file)
file.add_command(label="Save", image=save_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+S", command=save_file)
file.add_command(label="Save As", image=save_as_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+SHIFT+S", command=save_as)
file.add_command(label="Exit", image=exit_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+Q", command=exit_func)

# edit toolbar find functions


def find(event=None):
    def find_child():
        word = find_entry.get()
        text_editor.tag_remove("match", "1.0", tkinter.END)
        matches = 0
        start_pos = 1.0
        if word:
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tkinter.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    "match", foreground="red", background="yellow")

    def replace_child():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0, tkinter.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tkinter.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tkinter.Toplevel()
    find_dialogue.geometry("450x250")
    find_dialogue.title("Find")
    find_dialogue.resizable(0, 0)

    find_frame = ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text="Find : ")
    text_replace_label = ttk.Label(find_frame, text="Replace : ")

    find_entry = ttk.Entry(find_frame, width=30)
    replace_entry = ttk.Entry(find_frame, width=30)

    find_button = tkinter.Button(find_frame, text="Find", command=find_child)
    replace_button = tkinter.Button(
        find_frame, text="Replace", command=replace_child)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_entry.grid(row=0, column=1, padx=4, pady=4)
    replace_entry.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


# edit commands
edit.add_command(label="Copy", image=copy_icon, compound=tkinter.LEFT,
                 accelerator="CTRL+C", command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tkinter.LEFT,
                 accelerator="CTRL+V", command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tkinter.LEFT,
                 accelerator="CTRL+X", command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tkinter.LEFT,
                 accelerator="CTRL+ALT+X", command=lambda: text_editor.delete(1.0, tkinter.END))
edit.add_command(label="Find", image=find_icon,
                 compound=tkinter.LEFT, accelerator="CTRL+F", command=find)

show_statusbar = tkinter.BooleanVar()
show_statusbar.set(True)
show_toolbar = tkinter.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)
        text_editor.pack(fill=tkinter.BOTH, expand=True)
        status_bar.pack(side=tkinter.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tkinter.BOTTOM)
        show_statusbar = True


# view commands
view.add_checkbutton(label="Tool Bar", image=tool_bar_icon, compound=tkinter.LEFT,
                     onvalue=True, offvalue=False, variable=show_toolbar, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", image=staus_bar_icon, compound=tkinter.LEFT,
                     onvalue=True, offvalue=False, variable=show_statusbar, command=hide_statusbar)

# color function

color_dict = {
    "Light Default": ("#000000", "#ffffff"),
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Red": ('#2d2d2"', "#ffe8e8"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2")
}


def change_theme():
    user_color = theme_selection.get()
    color_tuple = color_dict.get(user_color)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, foreground=fg_color)


# color commands
color_theme.add_radiobutton(label="Light Default", image=light_default_icon,
                            compound=tkinter.LEFT, variable=theme_selection, command=change_theme)
color_theme.add_radiobutton(label="Light Plus", image=light_plus_icon,
                            compound=tkinter.LEFT, variable=theme_selection, command=change_theme)
color_theme.add_radiobutton(label="Dark", image=dark_icon,
                            compound=tkinter.LEFT, variable=theme_selection, command=change_theme)
color_theme.add_radiobutton(label="Red", image=red_icon, compound=tkinter.LEFT,
                            variable=theme_selection, command=change_theme)
color_theme.add_radiobutton(label="Monokai", image=monokai_icon,
                            compound=tkinter.LEFT, variable=theme_selection, command=change_theme)
color_theme.add_radiobutton(label="Night Blue", image=night_blue_icon,
                            compound=tkinter.LEFT, variable=theme_selection, command=change_theme)

root.config(menu=main_menu)

# bind shortcut key
root.bind("<Control-n>", new_file) and root.bind("<Control-N>", new_file)
root.bind("<Control-o>", open_file) and root.bind("<Control-O>", open_file)
root.bind("<Control-s>", save_file) and root.bind("<Control-S>", save_file)
root.bind("<Control-Alt-s>", save_as) and root.bind("<Control-Alt-S>", save_as)
root.bind("<Control-q>", exit_func) and root.bind("<Control-Q>", exit_func)
root.bind("<Control-f>", find) and root.bind("<Control-F>", find)
root.mainloop()
