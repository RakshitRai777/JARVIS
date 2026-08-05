from ai.conversation.entities.entity import ConversationEntity
from ai.conversation.entities.entity_type import EntityType


class EntityMemory:
    """
    Stores important entities mentioned during
    a conversation.

    Instead of remembering only the last noun,
    we remember the last PERSON, COMPANY,
    PROGRAMMING_LANGUAGE, etc.
    """

    ##########################################################

    def __init__(self):

        self.entities = []

        self.last_person = None

        self.last_company = None

        self.last_organization = None

        self.last_language = None

        self.last_product = None

        self.last_place = None

        self.last_event = None

    ##########################################################

    def add(self, entity: ConversationEntity):

        """
        Adds or updates an entity.
        """

        ######################################################
        # Already exists?
        ######################################################

        for existing in self.entities:

            if (
                existing.name.lower()
                == entity.name.lower()
            ):

                existing.mentions += 1

                existing.last_turn = entity.last_turn

                if(
                    existing.entity_type == EntityType.UNKNOWN
                    and entity.entity_type != EntityType.UNKNOWN
                ):
                    existing.entity_type = entity.entity_type

                entity = existing

                break

        else:

            self.entities.append(entity)

        ######################################################
        # Update shortcuts
        ######################################################

        if entity.entity_type == EntityType.PERSON:

            self.last_person = entity

        elif entity.entity_type == EntityType.COMPANY:

            self.last_company = entity

        elif entity.entity_type == EntityType.ORGANIZATION:

            self.last_organization = entity

        elif entity.entity_type == EntityType.PROGRAMMING_LANGUAGE:

            self.last_language = entity

        elif entity.entity_type == EntityType.PRODUCT:

            self.last_product = entity

        elif entity.entity_type in (

            EntityType.CITY,

            EntityType.COUNTRY,

            EntityType.PLACE,

        ):

            self.last_place = entity

        elif entity.entity_type == EntityType.EVENT:

            self.last_event = entity

    ##########################################################

    def resolve_pronoun(self, pronoun: str):

        """
        Returns the most likely entity for
        a pronoun.
        """

        pronoun = pronoun.lower()

        ######################################################

        if pronoun in (

            "he",

            "him",

            "his",

        ):

            return self.last_person

        ######################################################

        if pronoun in (

            "she",

            "her",

        ):

            return self.last_person

        ######################################################

        if pronoun == "it":

            for candidate in (

                self.last_product,

                self.last_language,

                self.last_company,

                self.last_organization,

                self.last_place,

            ):

                if candidate is not None:

                    return candidate

        ######################################################

        if pronoun == "they":

            return self.last_company

        ######################################################

        return None

    ##########################################################

    def clear(self):

        self.entities.clear()

        self.last_person = None

        self.last_company = None

        self.last_organization = None

        self.last_language = None

        self.last_product = None

        self.last_place = None

        self.last_event = None