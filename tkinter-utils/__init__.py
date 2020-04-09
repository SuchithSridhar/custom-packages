

def imports():
    import os
    cur = os.getcwd()
    os.chdir(r'C:\Users\LENOVO\AppData\Local\Programs\Python\Python37\Lib\custom_packages')

    x = os.listdir()
    for item in x:
        if "_" != item[0]:
            print(item)
    os.chdir(cur)
