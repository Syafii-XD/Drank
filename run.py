import os

if __name__ == "__main__":

   try:

       os.system("git pull")
       os.system("clear")

       __import__("drank").login()

   except Exception as e:

       exit(str(e))
