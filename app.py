from flask import Flask, render_template, request

app = Flask(__name__)

# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        shift = int(request.form.get("shift"))
        action = request.form.get("action")
        
        if action == "Encrypt":
            result = caesar_cipher(text, shift)
        else:
            result = caesar_cipher(text, shift, decrypt=True)
        
        return render_template("index.html", result=result, text=text, shift=shift)
    
    return render_template("index.html", result="", text="", shift=0)

if __name__ == "__main__":
    app.run(debug=True)
