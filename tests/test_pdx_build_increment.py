import unittest
from source.pdx_build_increment import PDXFile, read_pdx_file, write_pdx_file

class TestPDXFile(unittest.TestCase):
    def test_pdx_file_init(self):
        pdx_file = PDXFile()
        self.assertIsInstance(pdx_file, PDXFile)

    def test_pdx_file_attributes(self):
        pdx_file = PDXFile()
    
        self.assertIsInstance(pdx_file.name, str)
        self.assertIsInstance(pdx_file.author, str)
        self.assertIsInstance(pdx_file.description, str)
        self.assertIsInstance(pdx_file.bundleID, str)
        self.assertIsInstance(pdx_file.version, str)
        self.assertIsInstance(pdx_file.buildNumber, int)
        self.assertIsInstance(pdx_file.imagePath, str)
        self.assertIsInstance(pdx_file.launchSoundPath, str)


class TestReadPDXFile(unittest.TestCase):
    def test_read_pdx_file(self):
        # Create a test PDX file
        with open("test.pdx", "w") as file:
            file.write("name=Test\n")
            file.write("author=Author\n")
            file.write("description=Description\n")
            file.write("bundleID=com.example\n")
            file.write("version=1.0\n")
            file.write("buildNumber=1\n")
            file.write("imagePath=image.png\n")
            file.write("launchSoundPath=sound.wav\n")

        pdx_file = read_pdx_file("test.pdx")
        self.assertIsInstance(pdx_file, PDXFile)
        self.assertEqual(pdx_file.name, "Test")
        self.assertEqual(pdx_file.author, "Author")
        self.assertEqual(pdx_file.description, "Description")
        self.assertEqual(pdx_file.bundleID, "com.example")
        self.assertEqual(pdx_file.version, "1.0")
        self.assertEqual(pdx_file.buildNumber, 1)
        self.assertEqual(pdx_file.imagePath, "image.png")
        self.assertEqual(pdx_file.launchSoundPath, "sound.wav")

        # Clean up
        import os
        os.remove("test.pdx")

class TestWritePDXFile(unittest.TestCase):
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
            self.assertEqual(lines[0].strip(), "name=Test")
            self.assertEqual(lines[1].strip(), "author=Author")
            self.assertEqual(lines[2].strip(), "description=Description")
            self.assertEqual(lines[3].strip(), "bundleID=com.example")
            self.assertEqual(lines[4].strip(), "version=1.0")
            self.assertEqual(lines[5].strip(), "buildNumber=1")
            self.assertEqual(lines[6].strip(), "imagePath=image.png")
            self.assertEqual(lines[7].strip(), "launchSoundPath=sound.wav")

        # Clean up
        import os
        os.remove("test.pdx")

if __name__ == "__main__":
    unittest.main()