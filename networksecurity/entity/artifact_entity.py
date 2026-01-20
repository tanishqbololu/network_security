from dataclasses import dataclass
## @dataclass is used to automatically create boilerplate code for classes that mainly store data.

@dataclass
class DataIngestionArtifcat:
    trained_file_path:str
    test_file_path:str