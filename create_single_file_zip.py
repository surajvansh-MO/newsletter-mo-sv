import zipfile

zip_name = 'newsletter_share.zip'
files_to_zip = ['index.html']

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        zipf.write(file)

print(f"Created {zip_name} containing only index.html successfully!")
