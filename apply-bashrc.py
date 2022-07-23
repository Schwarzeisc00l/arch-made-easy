import os
from os.path import exists
str1 = 'echo "alias "'
str2 = '="'
str3 = '"'
# alias update='yay -Syu'
def echo(shortcut,command):
    os.system(str1 + shortcut + '='  + "\'" + command + "\'" + '>> ~/.bashrc')



echo('update','"yay -Syu"')
echo('remove','"yay -Rsu"')
echo('install','"yay -S"')
echo('clear','"sudo pacman -Scc"')
echo('root','"sudo"')
echo('switch-root','"su root"')
echo('test-connection','"ping wikipedia.org"')
echo('stop','"killall"')
echo('kernel','"uname -r"')
echo('edit','"nano"')
echo('search-packet','"yay"')
echo('clone','"git clone"')
echo('shutdown','"shutdown now"')
echo('copy','"cp"')
echo('copy_folder','"cp -R"')
echo('move','"mv"')
echo('create-folder','"mkdir"')
echo('create-file','"touch"')
echo('delete','"rm -rf"')
file_exists = exists('/usr/bin/neofetch')
if file_exists == True:
    echo('info','"neofetch"')
if file_exists == False:
    os.system('yay -S neofetch')
    echo('info','"neofetch"')

print('The process is complete!')
print('You can exit now!')
