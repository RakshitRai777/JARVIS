from pathlib import Path


class PathUtils:
    """
    Helper methods for working with filesystem paths.

    This class centralizes path parsing and normalization
    so every filesystem tool behaves consistently.
    """

    ############################################################

    @staticmethod
    def normalize(
        path: str,
    ) -> str:
        """
        Expand user symbols and return an absolute path.
        """

        return str(

            Path(path)

            .expanduser()

            .resolve()

        )

    ############################################################

    @staticmethod
    def is_absolute(
        path: str,
    ) -> bool:

        return Path(path).is_absolute()

    ############################################################

    @staticmethod
    def current_directory() -> str:

        return str(

            Path.cwd()

        )

    ############################################################

    @staticmethod
    def to_absolute(
        path: str,
    ) -> str:

        if Path(path).is_absolute():

            return PathUtils.normalize(path)

        return PathUtils.normalize(

            str(

                Path.cwd() / path

            )

        )

    ############################################################

    @staticmethod
    def filename(
        path: str,
    ) -> str:

        return Path(path).name

    ############################################################

    @staticmethod
    def parent(
        path: str,
    ) -> str:

        return str(

            Path(path).parent

        )

    ############################################################

    @staticmethod
    def extension(
        path: str,
    ) -> str:

        return Path(path).suffix