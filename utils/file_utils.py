import tempfile

def save_temp_files(uploaded_files):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(uploaded_files.read())
        return tmp.name