class FileExtractError(Exception):
    def __init__(self, excepetion: Exception, path: str) -> None:
        print(
            f'Error extracting file from {path}. Original error: {excepetion}')


class FileUploadError(Exception):
    def __init__(self, excepetion: Exception, dest: str) -> None:
        print(
            f'Error uploading file to {dest}. Original error: {excepetion}')


class FetchDataError(Exception):
    def __init__(self, excepetion: Exception, table: str) -> None:
        print(f"""Error fetching data from table {table}.
              Original error: {excepetion}""")


class SanitizeDataError(Exception):
    def __init__(self, excepetion: Exception, table: str) -> None:
        print(f"""Error sanitizing data from table {table}.
              Original error: {excepetion}""")


class DeserializeDataError(Exception):
    def __init__(self, excepetion: Exception, value: str) -> None:
        print(f"""Error deserializing value {value}.
              Original error: {excepetion}""")
