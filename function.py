from logic import LogicCoding


class Settings:
    def __init__(self, interface):
        self.interface = interface
        self.data = {}
        self.logic_code = LogicCoding

    def change_process(self):
        self.process = self.interface.var_process.get()
        return self.process

    def change_lang(self):
        self.lang = self.interface.var_lang.get()
        self.set_length(self.lang)
        return self.lang

    def set_length(self, lang):
        if lang == 'en':
            self.interface.slider.config(from_=-26, to=26)
        if lang == 'ru':
            self.interface.slider.config(from_=-32, to=32)

    def get_slider_value(self, new_val):
        self.value_slider = round(float(self.interface.slider.get()))
        self.interface.label_slider['text'] = self.value_slider
        return self.value_slider

    def get_text(self):
        self.text_input = self.interface.textbox_input.get('1.0', 'end-1c').rstrip()
        return self.text_input

    def set_text(self, text):
        self.interface.textbox_output.delete('1.0', 'end-1c')
        self.interface.textbox_output.insert('1.0', text)

    def save_text(self):
        text = self.interface.textbox_output.get('1.0', 'end-1c')
        path = self.interface.get_file_dialog()

        with open(path, 'w') as file:
            file.write(text)

    def collect_params(self):
        self.data['process'] = self.change_process()
        self.data['lang'] = self.change_lang()
        self.data['step'] = self.get_slider_value(self.interface.slider)
        self.data['text'] = self.get_text()

    def get_result(self):
        self.collect_params()
        result = self.logic_code(self.data)
        self.set_text(result.run_process())
