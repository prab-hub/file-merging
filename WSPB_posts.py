import re, pyperclip, codecs, shutil, os

for folder_name, subfolder_name, file_name in os.walk('C:\\Users\\Lenovo\\Downloads\\Telegram Desktop\\WSPB\\wallstreetplayboys.com'):
    for sub in subfolder_name:
        if folder_name == 'C:\\Users\\Lenovo\\Downloads\\Telegram Desktop\\WSPB\\wallstreetplayboys.com':
            file1 = codecs.open(folder_name + '\\' + sub + '\\' + 'index.html', 'r', 'utf-8')
            text = file1.read()
            file1.close()
            try:
                htmlRegEx = re.compile(r'\<h1 class="entry-title" itemprop="headline"\>(?s)(.*)\<div class="addtoany_share_save_container addtoany_content addtoany_content_bottom"\>')
                htmlExtracted = htmlRegEx.search(text)
                file2 = codecs.open('wsp2_ex.html', 'a', 'utf-8')
                file2.write(htmlExtracted.group())
                file2.write("****************************************************")
            except AttributeError:
                print(sub)

file2.close()