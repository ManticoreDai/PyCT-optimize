def read_str_from_file(a, b):
    with open('/root/py-conbyte-official/test/feature/textfile.txt', 'r') as f:
        generated = f.read() # generated = 'abc%sabc%sabc'
    generated %= (a, b)
    if '<script>' in generated:
        return 'dangerous'
    else:
        return 'safe'