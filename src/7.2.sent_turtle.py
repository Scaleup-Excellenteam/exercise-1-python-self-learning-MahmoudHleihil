"""
This module contains a PostOffice class that allows users to send, read, and search for messages in their inboxes.
"""


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False  # Added a 'read' flag to track message status
        }

        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)

        return self.message_id

    def read_inbox(self, username, count=None):
        """Retrieve and mark messages as read from a user's inbox.

        :param str username: The username of the inbox owner.
        :param int count: The number of messages to retrieve.
        :return: A list of messages retrieved.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found")

        inbox = self.boxes[username]
        messages_to_return = inbox[:count] if count else inbox[:]

        # Mark messages as read and remove them from the inbox
        self.boxes[username] = inbox[len(messages_to_return):]

        for message in messages_to_return:
            message['read'] = True

        return messages_to_return

    def search_inbox(self, username, query):
        """Search for messages in a user's inbox containing a specific query.

        :param str username: The username of the inbox owner.
        :param str query: The search string.
        :return: A list of messages containing the query.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found")

        return [message for message in self.boxes[username]
                if query.lower() in message['body'].lower() or query.lower() in message['sender'].lower()]


if __name__ == '__main__':
    # Example usage
    po = PostOffice(["alice", "bob"])
    po.send_message("alice", "bob", "Hello Bob!")
    po.send_message("bob", "alice", "Hey Alice! How are you?", urgent=True)
    po.send_message("alice", "bob", "Reminder: Meeting at 5 PM")

    print("Bob's inbox before reading:", po.boxes["bob"])
    print("Bob reads messages:", po.read_inbox("bob", 2))
    print("Bob's inbox after reading:", po.boxes["bob"])
    print("Searching Alice's inbox for 'Hey':", po.search_inbox("alice", "Hey"))
