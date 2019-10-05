from TCPClient import TCPClient
import Constants


def read_cmd_code():
    try:
        return int(input('Execute: '))
    except ValueError:
        print("ERROR: Not a number")
        print("Example: 1")
        return read_cmd_code()


if __name__ == '__main__':
    client = TCPClient("localhost", 5001)
    if client.fail:
        print("Contolla il server")
        exit(1)
    cmd = ""
    while True:
        print("Available actions")
        cn = 1
        for cmd in Constants.actions:
            print(cn.__str__() + " - " + cmd)
            cn += 1
        cmd = read_cmd_code() - 1
        client.send_message(Constants.actions[cmd])
        if Constants.actions[cmd] == "exit":
            break
    client.close_socket()
    exit(0)
