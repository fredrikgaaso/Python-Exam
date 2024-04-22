def main() :

    class Message():

        def __init__(self, sender, recipient):
            self._sname = sender
            self._rname = recipient
            self._message = ""

        def get_sender(self):
            return self._sname

        def get_recipient(self):
            return self._rname

        def append(self, message):
            self._message += message

        def toString(self):
            print("From: " + self.get_sender() + "\nTo: " + self.get_recipient() + "\nMessage: " + self._message)

    new_message = Message("Me", "You")
    new_message.append("Hello! ")
    new_message.append("How are you?")
    new_message.toString()

main()