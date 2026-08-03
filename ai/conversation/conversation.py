from datetime import datetime

from ai.conversation.message import Message


class Conversation:

    def __init__(self, conversation_id: str):

        self.id = conversation_id

        self.messages = []

    def add(self, role: str, content: str):

        self.messages.append(

            Message(
                role=role,
                content=content,
                timestamp=datetime.now()
            )

        )

    def history(self):

        return self.messages

    def clear(self):

        self.messages.clear()