import tkinter as tk
from tkinter import ttk, filedialog
from function import Settings


class BuildInterface:
    def init_frames(self):
        self.root = tk.Tk()
        self.root.geometry('800x400')
        self.root.minsize(800, 400)

        self.frame_top = ttk.Frame(self.root)
        self.frame_mid_top = ttk.Frame(self.root)
        self.frame_mid_bot = ttk.Frame(self.root)
        self.frame_bot = ttk.Frame(self.root)

        self.frame_settings = ttk.LabelFrame(self.frame_top, text='Process:')
        self.frame_lang = ttk.LabelFrame(self.frame_top, text='Language:')
        self.frame_shift = ttk.LabelFrame(self.frame_mid_top, text='Shift step:')
        self.frame_text_input = ttk.LabelFrame(self.frame_mid_bot, text='Text:')
        self.frame_text_output = ttk.LabelFrame(self.frame_mid_bot, text='Result:')
        self.frame_buttons = ttk.Frame(self.frame_bot)

        self.settings = Settings(self)

    def get_file_dialog(self):
        self.path = filedialog.asksaveasfilename(filetypes=[('Text files', '*.txt')])
        return self.path

    def init_radio_buttons(self):
        self.var_process = tk.StringVar()
        self.var_process.set('encode')
        self.var_lang = tk.StringVar()
        self.var_lang.set('en')

        self.rad_encode = ttk.Radiobutton(self.frame_settings,
                                          text='Encode',
                                          variable=self.var_process,
                                          value='encode',
                                          command=self.settings.change_process)
        self.rad_decode = ttk.Radiobutton(self.frame_settings,
                                          text='Decode',
                                          variable=self.var_process,
                                          value='decode',
                                          command=self.settings.change_process)
        self.rad_ru = ttk.Radiobutton(self.frame_lang,
                                      text='English',
                                      variable=self.var_lang,
                                      value='en',
                                      command=self.settings.change_lang)
        self.rad_en = ttk.Radiobutton(self.frame_lang,
                                      text='Russian',
                                      variable=self.var_lang,
                                      value='ru',
                                      command=self.settings.change_lang)

    def init_slider(self):
        self.label_slider = ttk.Label(self.frame_shift, text='0')
        self.slider = ttk.Scale(self.frame_shift,
                                from_=-26, to=26,
                                orient='horizontal',
                                command=self.settings.get_slider_value)

    def init_textbox_input(self):
        self.textbox_input = tk.Text(self.frame_text_input, width=1, height=1, wrap='word')
        self.scroll_in = ttk.Scrollbar(self.frame_text_input, command=self.textbox_input.yview)
        self.textbox_input.config(yscrollcommand=self.scroll_in.set)

    def init_textbox_output(self):
        self.textbox_output = tk.Text(self.frame_text_output, width=1, height=1, wrap='word')
        self.scroll_out = ttk.Scrollbar(self.frame_text_output, command=self.textbox_output.yview)
        self.textbox_output.config(yscrollcommand=self.scroll_out.set)

    def init_buttons(self):
        self.btn_run = ttk.Button(self.frame_buttons, text='Run', command=self.settings.get_result)
        self.btn_save = ttk.Button(self.frame_buttons, text='Save', command=self.settings.save_text)

    def packing_widgets(self):
        self.frame_top.pack(fill='x')
        self.frame_mid_top.pack(fill='x')
        self.frame_mid_bot.pack(fill='both', expand=True)
        self.frame_bot.pack(side='left', fill='x', expand=True)

        self.frame_settings.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.frame_lang.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.frame_shift.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.frame_text_input.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        self.frame_text_output.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        self.frame_buttons.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        self.rad_encode.pack(anchor='w', padx=10, pady=5)
        self.rad_decode.pack(anchor='w', padx=10, pady=5)
        self.rad_ru.pack(anchor='w', padx=10, pady=5)
        self.rad_en.pack(anchor='w', padx=10, pady=5)

        self.slider.pack(fill='x', padx=20, pady=5)
        self.label_slider.pack(pady=10)

        self.textbox_input.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        self.scroll_in.pack(side='left', fill='y', expand=False)
        self.textbox_output.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        self.scroll_out.pack(side='left', fill='y', expand=False)

        self.btn_run.pack(side='left', padx=5, pady=5, fill='x', expand=True)
        self.btn_save.pack(side='left', padx=5, pady=5, fill='x', expand=True)

    def run_building(self):
        self.init_frames()
        self.init_radio_buttons()
        self.init_slider()
        self.init_textbox_input()
        self.init_textbox_output()
        self.init_buttons()
        self.packing_widgets()
        self.root.mainloop()
