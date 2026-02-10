import pygetwindow as gw

def get_minecraft_window():
    for w in gw.getAllWindows():
        if "Minecraft" in w.title:
            return {
                "left": w.left,
                "top": w.top,
                "width": w.width,
                "height": w.height
            }
    return None
