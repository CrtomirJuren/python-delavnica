from pathlib import Path

folder_dir = Path(r'C:\python\python-delavnica.git\theory\file-io')
print(folder_dir)

filename = 'test.txt'

filepath = folder_dir / filename

# 1st way
# odpre datoteko

f = open(filepath, mode = 'w')
# # vpiše
f.write('1\n2\n3\n4\n')
# # zapre
f.close
