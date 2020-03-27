import os
from os import listdir
from os.path import isfile, join

LOCATION = input("Please input the directory path of the files you want to convert:\n>")

while not os.path.isdir(LOCATION):
    LOCATION = input("That path is incorrect.\nPlease re-enter the directory path.")

files = [f for f in listdir(LOCATION) if isfile(join(LOCATION, f))]
print(files)
PATH = LOCATION + '/output.tex'
print(PATH)
f = open(PATH, 'w')
text = '''\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}\n'''

for i in files:
    if i[-4:] == '.png':
        text += '\\begin{figure}\n  \\includegraphics[width=\\linewidth]{' + i + '}\n\\end{figure}\n\\newpage\n'

os.chdir(LOCATION)
text += '\n\\end{document}'
f.write(text)
f.close()
os.system(f'pdflatex output.tex')
