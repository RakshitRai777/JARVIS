from datetime import datetime

from ai.project.project import Project
from ai.project.project_status import ProjectStatus
from ai.project.milestone import Milestone


class ProjectManager:
    """
    Manages long-running AI projects.
    """

    ############################################################

    def __init__(self):

        self._projects: list[Project] = []

        self._milestones: dict[str, list[Milestone]] = {}

    ############################################################

    def create_project(
        self,
        name: str,
        description: str = "",
    ) -> Project:

        project = Project(

            name=name,

            description=description,

        )

        self._projects.append(project)

        self._milestones[name] = []

        return project

    ############################################################

    def get_projects(
        self,
    ) -> list[Project]:

        return self._projects

    ############################################################

    def find_project(
        self,
        name: str,
    ) -> Project | None:

        for project in self._projects:

            if project.name.lower() == name.lower():

                return project

        return None

    ############################################################

    def get_active_project(
        self,
    ) -> Project | None:

        for project in self._projects:

            if project.status == ProjectStatus.ACTIVE:

                return project

        return None

    ############################################################

    def add_milestone(
        self,
        project: Project,
        milestone: Milestone,
    ) -> None:

        self._milestones.setdefault(

            project.name,

            [],

        ).append(

            milestone,

        )

        ########################################################
        # Automatically update project progress
        ########################################################

        milestones = self._milestones[project.name]

        if milestones:

            project.progress = (

                sum(

                    m.progress

                    for m in milestones

                )

                /

                len(milestones)

            )

    ############################################################

    def get_milestones(
        self,
        project: Project,
    ) -> list[Milestone]:

        return self._milestones.get(

            project.name,

            [],

        )

    ############################################################

    def activate(
        self,
        project: Project,
    ) -> None:

        project.status = ProjectStatus.ACTIVE

    ############################################################

    def pause(
        self,
        project: Project,
    ) -> None:

        project.status = ProjectStatus.PAUSED

    ############################################################

    def complete(
        self,
        project: Project,
    ) -> None:

        project.status = ProjectStatus.COMPLETED

        project.progress = 100.0

        project.completed_at = datetime.now()

    ############################################################

    def archive(
        self,
        project: Project,
    ) -> None:

        project.status = ProjectStatus.ARCHIVED