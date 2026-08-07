from datetime import datetime

from ai.project.milestone import Milestone
from ai.project.project import Project
from ai.project.project_status import ProjectStatus
from ai.project.task import Task
from ai.project.task_selector import TaskSelector

class ProjectManager:
    """
    Manages long-running AI projects.
    """

    ############################################################

    def __init__(self):

        self._projects: list[Project] = []

        self.task_selector = TaskSelector()

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

        self._projects.append(

            project,

        )

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

        project.milestones.append(

            milestone,

        )

        ########################################################
        # Update project progress
        ########################################################

        self.update_progress(

            project,

        )

    ############################################################

    def get_milestones(
        self,
        project: Project,
    ) -> list[Milestone]:

        return project.milestones

    ############################################################

    def get_milestone_count(
        self,
        project: Project,
    ) -> int:

        return len(

            project.milestones,

        )

    ############################################################

    def get_active_milestone(
        self,
        project: Project,
    ) -> Milestone | None:

        for milestone in project.milestones:

            if not milestone.completed:

                return milestone

        return None


    ############################################################
    
    def get_active_task(
        self,
        project: Project,
    ) -> Task | None:
        milestone = self.get_active_milestone(
            project,
        )
        if milestone is None:
            return None
        return self.task_selector.select(
            [milestone],
        )

    ############################################################

    def update_progress(
        self,
        project: Project,
    ) -> None:

        if not project.milestones:

            project.progress = 0.0

            return

        project.progress = (

            sum(

                milestone.progress

                for milestone in project.milestones

            )

            /

            len(project.milestones)

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