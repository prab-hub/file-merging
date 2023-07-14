Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... # Importing modules
... 
... import re, pyperclip, codecs, shutil, os
... 
... # Looping over individual files in a folder.  
... 
... for folder_name, subfolder_name, file_name in os.walk('C:\\Users\\Lenovo\\Downloads\\Telegram Desktop\\WSPB\\wallstreetplayboys.com'):
...     for sub in subfolder_name:
...         if folder_name == 'C:\\Users\\Lenovo\\Downloads\\Telegram Desktop\\WSPB\\wallstreetplayboys.com':
...             file1 = codecs.open(folder_name + '\\' + sub + '\\' + 'index.html', 'r', 'utf-8')
...             text = file1.read()                     # Read all the text from file
...             file1.close()                           
...             try:
...                 htmlRegEx = re.compile(r'\<h1 class="entry-title" itemprop="headline"\>(?s)(.*)\<div class="addtoany_share_save_container addtoany_content addtoany_content_bottom"\>')  
...                 htmlExtracted = htmlRegEx.search(text)                      # Using RegEx copy body text
...                 file2 = codecs.open('wsp2_ex.html', 'a', 'utf-8')           
...                 file2.write(htmlExtracted.group())                          # Saving etxt to master file
...                 file2.write("****************************************************")
...             except AttributeError:
...                 print(sub)
... 
