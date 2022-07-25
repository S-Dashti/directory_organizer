import sys
from pathlib import Path
import shutil

if len(sys.argv) < 2:
    print('Give destination path as input argument')
else:
    path_dir = Path(sys.argv[1])

    file_group = {
        '.jpg' : 'images',
        '.png' : 'images',
        '.jpeg' : 'images',
        '.pdf' : 'documents',
        '.docx' : 'documents',
        '.doc' : 'documents',
        '.txt' : 'documents',
        '.zip' : 'compressed',
        '.rar' : 'compressed',
        '.csv' : 'data',
        '.xls' : 'data',
        '.xlsx' : 'data',
        
    }

    for item in path_dir.iterdir():
        if item.is_dir():
            continue
        if item.name.startswith('.'):
            continue
        if item.suffix in file_group:
            dest = path_dir / file_group[item.suffix] 
        else:
            dest = path_dir / 'others'
            
        dest.mkdir(exist_ok=True)
        shutil.move(str(item), str(dest))
        