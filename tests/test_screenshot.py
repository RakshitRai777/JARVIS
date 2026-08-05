from ai.desktop.screenshot import Screenshot


def main():

    screenshot = Screenshot()

    path = screenshot.capture()

    print()

    print("Saved to:")

    print(path)


if __name__ == "__main__":

    main()