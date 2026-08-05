from pathlib import Path
import shutil


class FileManager:
    """
    Central manager for all filesystem operations.

    Responsibilities
    ----------------
    • Create folders
    • Create files
    • Delete files/folders
    • Rename files/folders
    • Copy files/folders
    • Move files/folders
    • Query filesystem
    """

    ############################################################

    def create_folder(
        self,
        path: str,
    ) -> bool:

        try:

            Path(path).mkdir(

                parents=True,

                exist_ok=True,

            )

            return True

        except Exception:

            return False

    ############################################################

    def create_file(
        self,
        path: str,
    ) -> bool:

        try:

            file = Path(path)

            file.parent.mkdir(

                parents=True,

                exist_ok=True,

            )

            file.touch(

                exist_ok=True,

            )

            return True

        except Exception:

            return False

    ############################################################

    def delete(
        self,
        path: str,
    ) -> bool:

        try:

            target = Path(path)

            if target.is_dir():

                shutil.rmtree(target)

            elif target.exists():

                target.unlink()

            else:

                return False

            return True

        except Exception:

            return False

    ############################################################

    def rename(
        self,
        source: str,
        destination: str,
    ) -> bool:

        try:

            Path(source).rename(destination)

            return True

        except Exception:

            return False

    ############################################################

    def exists(
        self,
        path: str,
    ) -> bool:

        return Path(path).exists()

    ############################################################

    def is_file(
        self,
        path: str,
    ) -> bool:

        return Path(path).is_file()

    ############################################################

    def is_directory(
        self,
        path: str,
    ) -> bool:

        return Path(path).is_dir()

    ############################################################

    def list_directory(
        self,
        path: str,
    ) -> list[str]:

        try:

            return [

                item.name

                for item in Path(path).iterdir()

            ]

        except Exception:

            return []

    ############################################################

    def copy(
        self,
        source: str,
        destination: str,
    ) -> bool:

        try:

            source_path = Path(source)

            destination_path = Path(destination)

            if source_path.is_dir():

                shutil.copytree(

                    source_path,

                    destination_path,

                    dirs_exist_ok=True,

                )

            else:

                shutil.copy2(

                    source_path,

                    destination_path,

                )

            return True

        except Exception:

            return False

    ############################################################

    def move(
        self,
        source: str,
        destination: str,
    ) -> bool:

        try:

            shutil.move(

                source,

                destination,

            )

            return True

        except Exception:

            return False