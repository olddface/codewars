def hex_string_to_RGB(hex_string):
    jon1,jon2, jon3  = hex_string[1:3] ,  hex_string[3:5],hex_string[5:]
    jon = {'r':int(jon1, 16), 'g':int(jon2, 16), 'b':int(jon3, 16)}
    return jon
print(hex_string_to_RGB("#FF9933"))