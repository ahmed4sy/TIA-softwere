import txt2img
import json
import os
import time
import clear
def main():
    with open('tabels.json', 'r') as f:
        tabels = json.loads(f.read())
    tabelnum = 1
    listfont = []
    for lis in range(21):
        listfont.append(f'fonts/{lis+1}.ttf')
    listfont[0] = "fonts/1.otf"
    listfont.append("fonts/22.otf")
    for font in listfont:
        for tabel in tabels:
            if font == "fonts/22.otf":
                text_color = (255, 255, 255)
                outline_color = (0, 0, 0)
                sizeborder = 2
            else:
                text_color = (0, 0, 0)
                outline_color = (0, 0, 0)
                sizeborder = 0
            txt2img.create_image_with_border(tabel, font, 32, text_color, outline_color, sizeborder, (1200, 250), f'tesstrain/data/manga/eng_{tabelnum}.tif')
            os.system(f"tesseract tesstrain/data/manga/eng_{tabelnum}.tif tesstrain/data/manga/eng_{tabelnum} lstm.train")
            os.system(f"echo '{tabel}' > tesstrain/data/manga/eng_{tabelnum}.gt.txt")
            tabelnum += 1
    clear.delete_files_without_lstm("tesstrain/data/manga")
    os.system("mv tesstrain/data/manga/*.lstmf tesstrain/data/manga-ground-truth/")
    os.system("mv tesstrain/data/manga/*.gt.txt tesstrain/data/manga-ground-truth/")
    clear.remove_whitespace_entries_from_box_files("tesstrain/data/manga")
    print("Done")
    pass

main()