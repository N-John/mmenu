
'''
#MIT License

Copyright (c) 2024 N-John

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import os
import msvcrt
import shutil

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # For Unix/Linux/MacOS
        print('\033c', end='')

# Call this function to clear the terminal screen
clear_terminal()

class menu:
    def run(title:str,menus:list):
        men_sel=0
        while 1:
            if men_sel >=len(menus):
                men_sel=0
            menu.menu(men_sel,menus,title)
            char = msvcrt.getch()
            if char==b'\xe0':
                men_sel=men_sel+1
            elif char==b'\r':
                break
        return men_sel

    def menu(n:int,menus:list,title:str):
        try:
            clear_terminal()
            terminal_width, _ = shutil.get_terminal_size()
            menu_length=int(terminal_width/2)
            mnu=['\033[7m'+str(menus[n])+'\033[0m' if idx == n else str(item) for idx, item in enumerate(menus)]
            print('     '+'+'+'-'*menu_length+'+',flush=True)            
            padd_left=" " * int((int(menu_length-len(title))/2))
            padd_right=' ' * int(menu_length-len(padd_left+title))
            print(f"     |{padd_left}\033[4m{title}\033[0m{padd_right}|")
            c=0
            for mn in mnu:
                gp=(menu_length-5)-len(str(menus[c]))
                c=c+1

                print(f'     | ({c}) {mn}'+' '*gp+'|',flush=True)
            print('     '+'+'+'-'*menu_length+'+',flush=True)
        except Exception as e:
            print(str(e))                  

#To run the menu, provide it with a list and a title
#The code will output the list index selected from the menu
#EXAMPLE USE 
phone_brands = ["Apple", "Samsung", "Huawei", "Xiaomi", "Google", "OnePlus", "Sony", "LG"]
index=menu.run("WHICH PHONE BRAND DO YOU LIKE?",phone_brands)
print(f'Wow. I ALSO LIKE {phone_brands[index]}.')

