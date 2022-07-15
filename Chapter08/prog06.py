import microfs as ufs

print(ufs.ls())

try:
    ufs.get('mylib.py')
    print("File is copied to the local computer successfully!")
except Exception:
    print("No such file exists on the connected micro:bit device!")

try:
    ufs.put('prog06.py')
    print("File is copied to the micro:bit successfully!")
except Exception:
    print("No such file exists on the local computer!")

print(ufs.ls())

try:
    ufs.rm('prog06.py')
    print("File is deleted from the micro:bit successfully!")
except Exception:
    print("No such file exists on the connected micro:bit device!")

print(ufs.ls())
