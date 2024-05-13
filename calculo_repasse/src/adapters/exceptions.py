class FileExtractError(Exception):
    def __init__(self, excepetion: Exception, path: str) -> None:
        print(
            f'Error extracting file from {path}. Original error: {excepetion}')


class FileUploadError(Exception):
    def __init__(self, excepetion: Exception, dest: str) -> None:
        print(
            f'Error uploading file to {dest}. Original error: {excepetion}')
