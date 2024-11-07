def get_mime_type(file_name):
    mime_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    
    file_name = file_name.strip()
    file_ext = file_name[file_name.rfind('.'):].lower() if '.' in file_name else None

    return mime_types.get(file_ext, 'application/octet-stream')

def main():

    file_name = input("Enter the file name (with extension): ")
    mime_type = get_mime_type(file_name)
    print(mime_type)


if __name__ == "__main__":
    main()
