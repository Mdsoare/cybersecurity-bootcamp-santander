# -*- coding: utf-8 -*-
'''
File: openBrowser.py
Author: Marcelo Soares
Description: Script para abrir páginas web pelo navegador
Requirement: pip install webbrowser tkinter
'''
import webbrowser
import tkinter as tk

def open_google():
    webbrowser.open('https://www.google.com')

def open_yahoo():
    webbrowser.open('https://www.yahoo.com')

def open_custom_url():
    custom_url = custom_url_entry.get()
    webbrowser.open(custom_url)

root = tk.Tk()
root.title('Abrir Navegador')
root.geometry('300x200')

google_button = tk.Button(root, text='Abrir Google', command=open_google)
google_button.pack(pady=10)

yahoo_button = tk.Button(root, text='Abrir Yahoo', command=open_yahoo)
yahoo_button.pack(pady=10)

custom_url_label = tk.Label(root, text='Digite uma URL personalizada:')
custom_url_label.pack()
custom_url_entry = tk.Entry(root)
custom_url_entry.pack()
custom_url_button = tk.Button(root, text='Abrir URL Personalizada', command=open_custom_url)
custom_url_button.pack(pady=10)

root.mainloop()
