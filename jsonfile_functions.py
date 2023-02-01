import json
import pyperclip


def write_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_encrypt_txt(text, shift, save_button):
    encrypt_data = {"text": text, "shift_value": shift}
    try:
        with open("encrypt_texts.json", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        encrypt_json = { 
            'phrases': [encrypt_data] 
        }
        write_json(encrypt_json, "encrypt_texts.json")
    else:
        temp = data["phrases"]
        temp.append(encrypt_data)
        write_json(data, "encrypt_texts.json")
    save_button.setText("SAVED!")

    
def copy_encrypt_text(text, copy_button):
    pyperclip.copy(text)
    copy_button.setText("COPIED!")
    
