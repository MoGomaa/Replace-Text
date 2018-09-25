import sys

args = sys.argv[1:]

index = args.index('--')
files = args[index+1:]
From = args[index-2]
To = args[index-1]

for arg in args[:index] :
    if arg == '-b' :
        for f in files :
            from shutil import copyfile
            index = f.index('.')
            f_new = f[:index] + '_backup.txt'
            copyfile(f, f_new)
    elif arg == '-f' :
        for f in files :
            fileObj = open(f , "r")
            Text = fileObj.read()
            fileObj.close()
            Text = Text.replace(From , To , 1)
            fileObj = open(f , "w")
            fileObj.write(Text)
            fileObj.close()
    elif arg == '-l' :
        From = From[::-1]
        To = To[::-1]
        for f in files :
            fileObj = open(f , "r+")
            Text = fileObj.read()
            fileObj.close()
            Text = Text[::-1]
            Text = Text.replace(From , To , 1)
            Text = Text[::-1]
            fileObj = open(f , "w")
            fileObj.write(Text)
            fileObj.close()
        From = From[::-1]
        To = To[::-1]
    elif arg == '-i' :
        for f in files :
            fileObj = open(f , "r")
            Text = fileObj.read()
            fileObj.close()
            Text = Text.split("\n")
            new_text = ''
            for line in Text :
                l = line.split()
                for word in l :
                    if word.lower() == From.lower() :
                        new_text += To
                    else :
                        new_text += word
                    new_text += ' '                 ##Adding space after eachi word
                new_text += '\n'                    ##Adding newline at the end of every line
            fileObj = open(f , "w")
            fileObj.write(new_text)
            fileObj.close()
                


