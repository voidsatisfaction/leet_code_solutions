from typing import List
from abc import ABC, abstractmethod

class AFile(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def subfile_names(self) -> List[str]:
        pass

class TextFile(AFile):
    def __init__(self, name: str):
        super().__init__(name)
        self.text = ''

    def subfile_names(self) -> List[str]:
        return [self.name]

    def append_text(self, text: str) -> None:
        self.text += text

    def get_text(self) -> str:
        return self.text

class DirectoryFile(AFile):
    def __init__(self, name: str):
        super().__init__(name)
        self.sub_files = {}

    def append(self, file: AFile) -> None:
        self.sub_files[file.name] = file

    def get_subfile_by_name(self, name: str) -> AFile:
        return self.sub_files[name]

    def has_subfile(self, name: str) -> bool:
        return (name in self.sub_files)

    def subfile_names(self) -> List[str]:
        return list(sorted(self.sub_files.keys()))

class FileSystem:
    def __init__(self):
        self._entry_point = DirectoryFile('')
        self._entry_point.append(DirectoryFile('/'))

    def ls(self, path: str) -> List[str]:
        target_file = self._find_while_creating(path)
        return target_file.subfile_names()

    def mkdir(self, path: str) -> None:
        self._find_while_creating(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        target_file: TextFile = self._find_while_creating(filePath, is_text_file=True)
        target_file.append_text(content)

    def readContentFromFile(self, filePath: str) -> str:
        target_file: TextFile = self._find_while_creating(filePath, is_text_file=True)
        return target_file.get_text()

    def _find_while_creating(self, path: str, is_text_file=False) -> AFile:
        if path == '/':
            return self._entry_point.get_subfile_by_name('/')

        file_name_list = path.split('/')
        file_name_list[0] = '/'

        target = self._entry_point
        for name in file_name_list:
            if not target.has_subfile(name):
                file_to_add = TextFile(name) if is_text_file else DirectoryFile(name)
                target.append(file_to_add)
            target = target.get_subfile_by_name(name)

        return target
        

if __name__ == '__main__':
    fs = FileSystem()
    assert fs.ls('/') == []

    fs.mkdir('/a/b/c')

    fs.addContentToFile('/a/b/c/d', 'hello')

    assert fs.ls('/') == ['a']

    assert fs.readContentFromFile('/a/b/c/d') == 'hello'



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)