import keyboard

class waitcode:
    def __init__(self, text):
        self.clicked = ''
        self._lastkey = ''
        self._text = text
    def wait(self):
        while 1:
            if self.part():
                return
    def part(self):
        key = keyboard.read_key()
        try:
            self._text[len(self.clicked)]
            if key != self._lastkey:
                if key == self._text[len(self.clicked)]:
                    self.clicked += key
                else:
                    self.clicked = ''
                self._lastkey = key
        except:
            self.clicked = ''
            self._lastkey = ''
            return True
        return False
