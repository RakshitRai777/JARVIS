from datetime import datetime

from ai.conversation.entities.entity_memory import EntityMemory
from ai.conversation.message import Message


class Conversation:
    """
    Represents one conversation.

    Stores:

    - Messages
    - Entity Memory
    """

    ##########################################################

    def __init__(self, conversation_id: str):

        self.id = conversation_id

        self.messages = []

        ######################################################
        # Conversation Entity Memory
        ######################################################

        self.entity_memory = EntityMemory()

    ##########################################################

    def add(
        self,
        role: str,
        content: str,
    ):

        self.messages.append(

            Message(

                role=role,

                content=content,

                timestamp=datetime.now(),

            )

        )

    ##########################################################

    def history(self):

        return self.messages

    ##########################################################

    def last_message(self):

        if not self.messages:

            return None

        return self.messages[-1]

    ##########################################################

    def clear(self):

        self.messages.clear()

        self.entity_memory.clear()