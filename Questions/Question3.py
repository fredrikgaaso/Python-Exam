def main():
    class Message:

        def __init__(self, sender, recipient):
            self._senderName = sender
            self._recipientName = recipient
            self._message = ""

        def get_sender(self):
            return self._senderName

        def get_recipient(self):
            return self._recipientName

        def append(self, message):
            self._message += message

        def toString(self):
            print("From:", self.get_sender(), "\nTo:", self.get_recipient(), "\nMessage:", self._message)

    new_message = Message("Harry Morgan", "Rudolf Reindeer")
    new_message.append("Hello! ")
    new_message.append("How are you?")
    new_message.toString()


main()
