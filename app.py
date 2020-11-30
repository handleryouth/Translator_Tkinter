import tkinter as tk
import speech_recognition as sr
from tkinter import ttk, messagebox, Scrollbar
from DPI_AWARENESS import setting_dpi
from googletrans import Translator
from tkinter.filedialog import askopenfilename


language_code = {'af': 'Afrikaans','sq': 'Albanian','am': 'Amharic','ar': 'Arabic','hy': 'Armenian','az': 'Azerbaijani','eu': 'Basque','be': 'Belarusian',
    'bn': 'Bengali','bs': 'Bosnian','bg': 'Bulgarian','ca': 'Catalan','ceb': 'Cebuano','ny': 'Chichewa','zh-cn': 'Chinese (simplified)','zh-tw': 'Chinese (traditional)',
    'co': 'Corsican','hr': 'Croatian','cs': 'Czech','da': 'Danish','nl': 'Dutch','en': 'English','eo': 'Esperanto','et': 'Estonian','tl': 'Filipino','fi': 'Finnish','fr': 'French',
    'Fy': 'Frisian','gl': 'Galician','ka': 'Georgian','de': 'German','el': 'Greek','gu': 'Gujarati','ht': 'Haitian creole','ha': 'Hausa','haw': 'Hawaiian',
    'iw': 'Hebrew','he': 'Hebrew','hi': 'Hindi','hmn': 'Hmong','hu': 'Hungarian','is': 'Icelandic','ig': 'Igbo','id': 'Indonesian','ga': 'Irish','it': 'Italian',
    'ja': 'Japanese','jw': 'Javanese','kn': 'Kannada','kk': 'Kazakh','km': 'Khmer','ko': 'Korean','ku': 'Kurdish (kurmanji)','ky': 'Kyrgyz','lo': 'Lao',
    'la': 'Latin','lv': 'Latvian','lt': 'Lithuanian','lb': 'Luxembourgish','mk': 'Macedonian','mg': 'Malagasy','ms': 'Malay','ml': 'Malayalam','mt': 'Maltese',
    'mi': 'Maori','mr': 'Marathi','mn': 'Mongolian','my': 'Myanmar (burmese)','ne': 'Nepali','no': 'Norwegian','or': 'Odia','ps': 'Pashto','fa': 'Persian',
    'pl': 'Polish','pt': 'Portuguese','pa': 'Punjabi','ro': 'Romanian','ru': 'Russian','sm': 'Samoan','gd': 'Scots gaelic','sr': 'Serbian','st': 'Sesotho',
    'sn': 'Shona','sd': 'Sindhi','si': 'Sinhala','sk': 'Slovak','sl': 'Slovenian','so': 'Somali','es': 'Spanish','su': 'Sundanese','sw': 'Swahili','sv': 'Swedish','tg': 'Tajik',
    'ta': 'Tamil','te': 'Telugu','th': 'Thai','tr': 'Turkish','uk': 'Ukrainian','ur': 'Urdu','ug': 'Uyghur','uz': 'Uzbek','vi': 'Vietnamese','cy': 'Welsh',
    'xh': 'Xhosa','yi': 'Yiddish','yo': 'Yoruba','zu': 'Zulu'}

language_name = ('Afrikaans', 'Albanian', 'Amharic', 'Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian','Catalan','Cebuano',
    'Chichewa','Chinese (simplified)','Chinese (traditional)','Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian','Filipino','Finnish','French','Frisian','Galician','Georgian','German','Greek','Gujarati',
    'Haitian Creole','Hausa','Hawaiian','Hebrew','hebrew','Hindi','Hmong','Hungarian','Icelandic','Igbo','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer','Korean',
    'Kurdish (kurmanji)','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi',
    'Mongolian', 'Myanmar (burmese)','Nepali','Norwegian','Odia','Pashto','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Samoan',
    'Scots gaelic','Serbian','Sesotho','Shona','Sindhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil',
    'Telugu','Thai','Turkish','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu')



def askingpermission():
    messagebox.showwarning("Sorry", "Text-to-Speech only works in English languange. Sorry !")
    choosed_from.set("English")

def translate_command():
    code_name = {name: code for code, name in language_code.items()}
    to_language_box['state'] = 'normal'
    to_language_box.delete('1.0', "end-1c")
    fr_language = code_name[choosed_from.get()]
    to_languange = code_name[choosed_to.get()]
    translator = Translator()
    result = translator.translate(
        from_language_box.get("1.0", "end-1c"),
        src=fr_language,
        dest=to_languange
    )
    while result == False:
        result = translator.translate(
            from_language_box.get("1.0", "end-1c"),
            src=fr_language,
            dest=to_languange
        )
    to_language_box.insert("end", f"{result.text}")
    to_language_box['state'] = 'disabled'
    print(result.text)

def speech_recognition():
    if choosed_from.get() == "English":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print('talk')
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text)
                from_language_box.insert('end', text)
                print(text)
            except:
                from_language.insert("end", f"sorry, the sound could not recognise")
    else:
        askingpermission()


def add_sound():
    r = sr.Recognizer()
    filename = askopenfilename(title = "Add Sound File", filetypes=(("WAV file","*.wav"), ("AIFF file","*.AIFF"),
                                                                    ("AIFF-C file","*.AIFF-C"),("FLAC file","*.FLAC")))
    with sr.AudioFile(f'{filename}') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            from_language_box.insert(0, f"{text}")
            print(text)
        except:
            from_language.insert("end", f"Sorry. Please try again !")
            print('Sorry. Please try again !')

setting_dpi()

root = tk.Tk()
root.title("Translator")

upper = ttk.Frame(root)
upper.grid(row = 0)

right_left = ttk.Frame(root)
right_left.grid(row = 1)

big_title = ttk.Label(upper, text = "Welcome to the Translator")
big_title.grid(row = 0, pady = 30)



scrollbar = Scrollbar(root)
scrollbar.grid(row = 2, column = 1, ipady = 25)
from_language_box = tk.Text(root, height = 5, width = 52, yscrollcommand=scrollbar.set)
from_language_box.grid(row = 2, pady = 5)
scrollbar.config(command=from_language_box.yview)

scrollbar1 = Scrollbar(root)
scrollbar1.grid(row = 4, column = 1, ipady = 25)
to_language_box = tk.Text(root, height = 5, width = 52, cursor = 'arrow', yscrollcommand=scrollbar1.set)
to_language_box.ReadOnly = True
scrollbar1.config(command=to_language_box.yview)
to_language_box.grid(row = 4, pady = 5)

choosed_from = tk.StringVar(value="English")
from_language = ttk.Combobox(right_left, textvariable = choosed_from)
from_language['values'] = language_name
from_language.pack(side = "left", padx = 10, pady = (5,5))
from_language['state'] = 'readonly'

sound = ttk.Button(right_left, text = "Text-to-speech", command = speech_recognition)
sound.pack(side = "right", padx = 10, pady = (5,5))

adding_sound_file = ttk.Button(right_left, text = "Add Sound", command = add_sound)
adding_sound_file.pack(padx = 10, pady = (5,5))

choosed_to = tk.StringVar(value="English")
to_language = ttk.Combobox(root, textvariable = choosed_to)
to_language['values'] = language_name
to_language['state'] = 'readonly'
to_language.grid(row = 3, pady = (5, 5))

translate_button = ttk.Button(root, text = "Translate", command = translate_command, cursor = "hand2")
translate_button.grid(row = 5, pady = 10, padx = 10, ipadx = 20)

root.mainloop()