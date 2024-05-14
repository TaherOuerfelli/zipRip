# ZipRip.py
A python script to bruteforce (Zip, Rar, 7z) password protected archives.

### Install requirements
```
pip install -r requirements.txt
```
### Run python file
```
python ziprip.py
```
*or*
```
py ziprip.py
```

>[!IMPORTANT]
> - Uses `unrar` or `7z` from the command line to extract archives.
> - Make sure to download [Winrar](https://www.rarlab.com/rar_add.htm) (command line or free version) and [7z](https://www.7-zip.org).
> - Add `UnRar.exe` and `7z.exe` to PATH for Windows
> - (check that `'unrar -v'` and `'7z -h'` are working in cmd)

> * Uses **patoolib** in case *unrar / 7z* are not installed **(but runs much slower)**
