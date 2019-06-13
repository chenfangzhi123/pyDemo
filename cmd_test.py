import subprocess

if __name__ == '__main__':
    print(
        subprocess.Popen("type 2415_phone.msg|protoc --encode=RTB.Request tx_rtb_for_dsp.proto", stdout=subprocess.PIPE,
                         shell=True).stdout.read())

    # print(subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True).stdout.read().decode())
    # print(os.popen("mvn -v").read())

# print(line.read())
# import subprocess
# out_bytes = subprocess.check_output(['mvn -v'])
# out_text = out_bytes.decode('utf-8')
# print(out_text)
