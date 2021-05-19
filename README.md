# Project Idea
The idea of this project is to securely protect data against stealing by preventing anyone to access the data saved in a certain file (image, text, Docx, pdf, etc..)
Our service will be provided on a web application where the user uploads a file with an optional password and then downloads from the website an encrypted copy of the file. The user could also upload an encrypted copy with the appropriate password, if the user fails to submit the right password to the decrypter, an invalid request page will be shown.

*Note: This program is designed to work on both Windows and Unix-based operating systems and is also designed to encrypt files or any byte object*
# How is it Different?
The project is not different from other encryption services except that it is very simple and easy to use and very lightweight, it doesn't take a lot of time to encrypt or decrypt and it provides the user with instant results.

# Details of Implementation

## Tools
We are using python as a programing language and Cryptography library to perform the encryption and decryption of any byte object. 
For hosting and handling user requests, we are using the python library 
Flask and simple HTML  and CSS for the user interface.

# How is the Encryption working?

The Cryptography library *Fernet* was built on top of the AES algorithm which means that it will be using symmetric encryption indicating that it will be using the same key for encryption and decryption.
The program derives a key from the password entered by the user and uses it for encryption. To generate the key, the program adds salt to the passphrase and hashes it using SHA256 on 1000 iterations, and then returns the 32-bits key.
The salt is a constant array byte and the use is to prevent attackers to decrypt the file using other tools.
The generated key is a fernet key used to *encrypt*  and decrypt the files. Each key is formed using two other smaller keys, a 128-bit AES encryption key and a 128-bit SHA256 HMAC signing key.


# How To?

## Requirments

* [python3](https://www.python.org)
* [pip3](https://pypi.org/project/pip/)
* [git](https://git-scm.com) (to install the project)

## Installation Steps

1. Start by cloning this repository by typing the following command in your terminal
`git clone github.com/Husseinelghoul/file-encryption-system`
2. Then navigate to the project directory and run the following commands to install the required python libraries
`pip install -r requirements.txt`
3. Now you can run the project using the following command
`python3 app.py`

## Testing the program
### A. Encrypt

First, start by uploading a file by clicking on the **choose file** button under the **Encrypt** label, and add your custom secret code in the text box and hit enter *(if you do not enter any secret code the empty string will be used as a secret code instead)*. Afterward, you should be prompted to download the encrypted file


### B. Examine

If you examine the downloaded encrypted file you can see that either you cannot open it (if it's not a text file) or that the data cannot be shown or the data shown will have no meaning (in the case of test files).

### C. Decrypt

The description process is similar to the encryption process, you just have to upload the encrypted file by using the **choose file** button under the **Decrypt** label, and when you add the right password and hit submit you will be prompted to download the decrypted file.
If you enter another password, you will be redirected to an **Invalid request** Page.
If you compare the encrypted file and the original file you will notice that they are the same file.

# Video Demonstration

This [Youtube link](https://www.youtube.com) presents a walkthrough of the project capabilities and how to use them.
