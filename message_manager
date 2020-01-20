import datetime

class MessageManager():
      def __init__(self):
            self.SaveMsg("*********Starting New Session*********")

      def SaveMsg(self, msg):
            with open("messagesLog.txt", "a") as f:
                  f.write(f"{datetime.datetime.now()} {msg}\n")
