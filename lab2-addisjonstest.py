
def roman_addition(rom_num1, rom_num2):
    rom_num1 = convert(rom_num1)
    rom_num2 = convert(rom_num2)
    
    rom_num_temp = rom_num1 + rom_num2
    rom_num_result = []
    rom_num_list = "MDCLXVI"
    for char in rom_num_list:
        for item in rom_num_temp:
            if item == char:
                rom_num_result.append(item)
                
    return(revert("".join(rom_num_result)))
    
    print rom_num1
    print rom_num2
    
    
def convert(rom_num):
    
    rom_num = rom_num.replace("CM", "DCCCC")
    rom_num = rom_num.replace("CD", "CCCC")
    rom_num = rom_num.replace("XC", "LXXXX")
    rom_num = rom_num.replace("XL", "XXXX")
    rom_num = rom_num.replace("IX", "VIIII")
    rom_num = rom_num.replace("IV", "IIII")
    
    return rom_num
    
def revert(rom_num):
    
	rom_num = rom_num.replace("IIIII", "V")
	rom_num = rom_num.replace("IIII", "IV")
	rom_num = rom_num.replace("VIIIII", "X")
	rom_num = rom_num.replace("VIIII", "IX")
	rom_num = rom_num.replace("VV", "X")
	rom_num = rom_num.replace("XXXXX", "L")
	rom_num = rom_num.replace("XXXX", "XL")
	rom_num = rom_num.replace("LXXXXX", "C")
	rom_num = rom_num.replace("LXXXX", "XC")
	rom_num = rom_num.replace("CCCCC", "D")
	rom_num = rom_num.replace("CCCC", "CD")
	rom_num = rom_num.replace("DCCCCC", "M")
	rom_num = rom_num.replace("DCCCC", "CM")
	rom_num = rom_num.replace("DD", "M")
	
	return rom_num
    
rom1 = raw_input("Input the first roman number:")
rom2 = raw_input("Input the second roman number:")

print roman_addition(rom1, rom2)
rom_test = raw_input("test")
print revert(rom_test )