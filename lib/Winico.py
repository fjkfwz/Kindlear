""" System tray extension for windows, supports 2.x/3.x
Demo:
import tkinter, Winico

root = tkinter.Tk()
def your_callback1(icon_id, message_specifier):
    if message_specifier == "WM_LBUTTONDBLCLK":
        print("WM_LBUTTONDBLCLK")

# %m message specifier, %i icon_id
cmd = (root.register(your_callback1), '%i', '%m')

icon = Winico.Winico()
icon_id = icon.createfrom("tkchat.ico")
icon.taskbar_add(icon_id, callback=cmd, text="Sample text!")
root.mainloop()"""

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
class Winico:
    def __init__(self):
        master = tkinter._default_root
        if not master:
            raise RuntimeError('Too early to create icon')
        self.WinicoVersion = master.tk.call('package', 'require', 'Winico')
        self.tk = master.tk

    def createfrom(self, filename):
        return self.tk.call('winico', 'createfrom', filename)

    def delete(self, id_):
        self.tk.call('winico', 'delete', id_)

    def load(self, resourcename, filename=None):
        return self.tk.call('winico', 'load', resourcename, filename)

    def info(self, id_=None):
        # the output should of course be formatted somehow
        return self.tk.call('winico', 'info', id_)

    def setwindow(self, size='big', pos=None):
        return self.tk.call('winico', 'setwindow', size, pos)

    def taskbar_add(self, id_, callback=None, pos=None, text=None):
        args = ()
        if callback:
            args += ('-callback', callback)
        if pos:
            args += ('-pos', pos)
        if text:
            args += ('-text', text)
        return self.tk.call('winico', 'taskbar', 'add', id_, *args)

    def taskbar_modify(self, id_, callback=None, pos=None, text=None):
        args = ()
        if callback:
            args += ('-callback', callback)
        if pos:
            args += ('-pos', pos)
        if text:
            args += ('-text', text)
        return self.tk.call('winico', 'taskbar', 'modify', id_, *args)

    def taskbar_delete(self, id_):
        return self.tk.call('winico', 'taskbar', 'delete', id_)
