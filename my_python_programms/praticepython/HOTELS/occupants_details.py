



def occupantInfo(rom_no, ocpt_name, ocpt_phoneno):
    room = "ROOM"+rom_no+"/ocupant_info"
    file = open(room, 'w+')
    gash = 'name : '+ocpt_name+"\n"
    phno = "phone number : "+ocpt_phoneno+"\n"
    task = file.writelines([gash, phno])
    file.close()
