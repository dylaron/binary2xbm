def rev_n_0b(to_rev):
    return "0b" + to_rev[::-1]


def covert_line(str_in):
    line_out = ""
    if len(str_in) % 8 == 0:
        for i in range(int(len(str_in) / 8)):
            line_out += rev_n_0b(str_in[i * 8:i * 8 + 8]) + ", "
        line_out += "// " + str_in.replace("0", " ").replace("1", "#")
    return line_out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    f = open('output.xbm', 'w')
    f.write("#define icon_width {}\n".format(len(lines[0])))
    f.write("#define icon_height {}\n".format(len(lines)))
    f.write("static unsigned char icon_bits[] = {\n")
    for line in lines:
        print(covert_line(line))
        f.write(covert_line(line) + "\n")
    f.write("}\n")
    f.close()
