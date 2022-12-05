text = 'This is good'
with open("document.bin", "wb") as f:
    f.write(text.encode('ascii'))
