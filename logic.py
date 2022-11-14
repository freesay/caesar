class LogicCoding:
    def __init__(self, data):
        self.alphabet_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.alphabet_en = "abcdefghijklmnopqrstuvwxyz"
        self.data = data

        self.process = self.data['process']
        self.lang = self.data['lang']
        self.step = self.data['step']
        self.text = self.data['text']

    def run_process(self):
        result = ''
        if self.process == 'encode':
            if self.lang == 'en':
                result = self.encode(self.alphabet_en)
            elif self.lang == 'ru':
                result = self.encode(self.alphabet_ru)

        if self.process == 'decode':
            if self.lang == 'en':
                result = self.decode(self.alphabet_en)
            elif self.lang == 'ru':
                result = self.decode(self.alphabet_ru)

        if self.process == 'decode' and self.step == 0:
            if self.lang == 'en':
                result = self.hack(self.alphabet_en)
            elif self.lang == 'ru':
                result = self.hack(self.alphabet_ru)
        return result

    def encode(self, lang):
        encode_text = ''
        for c in self.text:
            if c.isupper():
                if c.lower() in lang:
                    encode_text += lang[(lang.index(c.lower()) + self.step) % len(lang)].upper()
                else:
                    encode_text += c
            else:
                if c in lang:
                    encode_text += lang[(lang.index(c) + self.step) % len(lang)]
                else:
                    encode_text += c
        return encode_text

    def decode(self, lang):
        decode_text = ''
        for c in self.text:
            if c.isupper():
                if c.lower() in lang:
                    decode_text += lang[(lang.index(c.lower()) - self.step) % len(lang)].upper()
                else:
                    decode_text += c
            else:
                if c in lang:
                    decode_text += lang[(lang.index(c) - self.step) % len(lang)]
                else:
                    decode_text += c
        return decode_text

    def hack(self, lang):
        hack_text = ''
        for i in range(len(lang)):
            for c in self.text:
                if c.isupper():
                    if c.lower() in lang:
                        hack_text += lang[(lang.index(c.lower()) + i) % len(lang)].upper()
                    else:
                        hack_text += c
                else:
                    if c in lang:
                        hack_text += lang[(lang.index(c) + i) % len(lang)]
                    else:
                        hack_text += c
            hack_text += '\n'
        return hack_text
