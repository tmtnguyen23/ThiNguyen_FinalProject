from controller import *

def main() -> None:
    """
    Function to run the volume calculator app
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
