from aTrain import app
import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app.start()
