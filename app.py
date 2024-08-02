import zipfile
with zipfile.ZipFile('./pExcel.zip', 'r') as zip_ref:
    zip_ref.extractall('./')