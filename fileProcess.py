if __name__ == "__main__":
    file = open("all.txt", "r")
    res_file = open("res.txt", "a")
    res_file.write("\n")
    for line in file:
        res_file.write(line)
