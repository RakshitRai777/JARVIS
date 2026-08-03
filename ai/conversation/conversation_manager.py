from ai.conversation.conversation import Conversation


class ConversationManager:

    def __init__(self):

        self._conversations = {}

    def get(self, conversation_id="default"):

        if conversation_id not in self._conversations:

            self._conversations[conversation_id] = Conversation(
                conversation_id
            )

        return self._conversations[conversation_id]

    def clear(self, conversation_id="default"):

        if conversation_id in self._conversations:

            self._conversations[conversation_id].clear()