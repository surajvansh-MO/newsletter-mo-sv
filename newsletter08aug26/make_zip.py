import zipfile

with zipfile.ZipFile('c:/Users/Admin/Desktop/newsletter/newsletter08aug26/newsletter_package.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('c:/Users/Admin/Desktop/newsletter/newsletter08aug26/index.html', 'index.html')

print("Created newsletter_package.zip successfully!")
