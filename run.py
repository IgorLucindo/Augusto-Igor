from . import bughunter

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    bughunter.run(debug=True)