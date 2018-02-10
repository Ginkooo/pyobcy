from obcy import Obcy


def main():
    with Obcy() as obcy:
        chat = obcy.get_chat()
        while True:
            msg = chat.get_last_msg()
            if msg:
                print(str(msg))


if __name__ == '__main__':
    main()
