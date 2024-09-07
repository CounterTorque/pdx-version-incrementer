import pytest
from source.pdx_build_increment import PDXFile, read_pdx_file, write_pdx_file

class TestPDXFile:
    def test_pdx_file_init(self):
        pdx_file = PDXFile()
        assert isinstance(pdx_file, PDXFile)

    def test_pdx_file_attributes(self):
        pdx_file = PDXFile()
        # Add assertions for pdx_file attributes here

    def test_write_pdx_file(self):
        pdx_file = PDXFile()
        pdx_file.name = "Test"
        pdx_file.author = "Author"
        pdx_file.description = "Description"
        pdx_file.bundleID = "com.example"
        pdx_file.version = "1.0"
        pdx_file.buildNumber = 1
        pdx_file.imagePath = "image.png"
        pdx_file.launchSoundPath = "sound.wav"

        write_pdx_file("test.pdx", pdx_file)

        # Check the written file
        with open("test.pdx", "r") as file:
            lines = file.readlines()
            assert lines[0].strip() == "name=Test"
            assert lines[1].strip() == "author=Author"
            assert lines[2].strip() == "description=Description"
            assert lines[3].strip() == "bundleID=com.example"
            assert lines[4].strip() == "version=1.0"
            assert lines[5].strip() == "buildNumber=1"
            assert lines[6].strip() == "imagePath=image.png"
            assert lines[7].strip() == "launchSoundPath=sound.wav"

        # Clean up
        import os
        os.remove("test.pdx")