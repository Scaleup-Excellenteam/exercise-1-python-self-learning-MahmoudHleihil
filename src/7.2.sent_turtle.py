"""
This module contains a PostOffice class that allows users to send, read, and search for messages in their inboxes.
"""

class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient."""
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,  # Add title
            'body': message_body,
            'sender': sender,
            'read': False  # Use 'read' flag to mark whether the message has been read
        }

        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)

        return self.message_id

    def read_inbox(self, username, count=None):
        """Retrieve and mark messages as read from a user's inbox."""
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found")

        inbox = self.boxes[username]
        messages_to_return = inbox[:count] if count else inbox[:]

        # Mark messages as read without removing them
        for message in messages_to_return:
            message['read'] = True  # Mark the message as read

        return messages_to_return

    def search_inbox(self, username, query):
        """Search for messages in a user's inbox containing a specific query."""
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found")

        return [
            message for message in self.boxes[username]
            if query.lower() in message['title'].lower()  # Search by title
            or query.lower() in message['body'].lower()
            or query.lower() in message['sender'].lower()
        ]


if __name__ == '__main__':
    # Example usage
    po = PostOffice(["alice", "bob"])
    po.send_message("alice", "bob", "Greeting", "Hello Bob!")
    po.send_message("bob", "alice", "Check-in", "Hey Alice! How are you?", urgent=True)
    po.send_message("alice", "bob", "Meeting Reminder", "Reminder: Meeting at 5 PM")

    print("Bob's inbox before reading:", po.boxes["bob"])
    print("Bob reads messages:", po.read_inbox("bob", 2))
    print("Bob's inbox after reading:", po.boxes["bob"])
    print("Searching Alice's inbox for 'Hey':", po.search_inbox("alice", "Hey"))
