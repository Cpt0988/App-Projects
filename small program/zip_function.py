import zipfile
import pathlib

def make_archive(filepaths, dest_dir,label1):
    dest_path = pathlib.Path(dest_dir,label1)
    with zipfile.ZipFile(dest_path,'w') as archive:
        
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
            
            
# test function
if __name__ == '__main__':
    make_archive(filepaths=["RPS.py","mad-libs.py"], dest_dir= "test_zone",label1='tester.zip')