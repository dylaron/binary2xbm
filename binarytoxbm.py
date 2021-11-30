def rev_n_0b(to_rev):
    return "0b" + to_rev[::-1]

def covert_line(str_in):
    str_out = ""
    if len(str_in) == 16:
        l_out = rev_n_0b(str_in[0:8])
        r_out = rev_n_0b(str_in[8:16])
        line_out = l_out + ", " + r_out + ", "
        line_out += "// " + str_in.replace("0"," ").replace("1","#")
    return line_out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    f = open('output.xbm', 'w')
    f.write("#define icon_width 16\n")
    f.write("#define icon_height {}\n".format(len(lines)))
    f.write("static unsigned char icon_bits[] = {\n")
    for line in lines:
        print(covert_line(line))
        f.write(covert_line(line) + "\n")
    f.write("}\n")
    f.close()
