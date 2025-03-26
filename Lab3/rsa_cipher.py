import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Gen_btn.clicked.connect(self.call_api_gen_keys) 
        self.ui.En_btn.clicked.connect(self.call_api_encrypt)
        self.ui.De_btn.clicked.connect(self.call_api_decrypt)
        self.ui.Sign_btn.clicked.connect(self.call_api_sign)
        self.ui.Verify_btn.clicked.connect(self.call_api_verify)
        
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.PlainText_txt.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.CipherText_txt.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successful")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "cipher_text": self.ui.CipherText_txt.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.PlainText_txt.setPlainText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.Infor_txt.toPlainText(),
        }
        try:
            resposne = requests.post(url, json=payload)
            if resposne.status_code == 200:
                data = resposne.json()
                self.ui.Sig_txt.setPlainText(data["signature"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sign Successful")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.Infor_txt.toPlainText(),
            "signature": self.ui.Sig_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if (data["is_verified"]):  
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verify Successful")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verify Failed")
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())