import eel
import encode_DES
eel.init('web')


@eel.expose
def main(text, key, category):
    if len(text) != 0:
        encode_DES.begin(text, key, category)


eel.start('main.html', size=(900, 900), port=9999)
