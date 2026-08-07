from ai.project.project import Project
from ai.project.project_status import ProjectStatus


def main():

    ########################################################

    print("=" * 60)
    print("DEFAULT PROJECT")
    print("=" * 60)

    project = Project()

    print(project)

    ########################################################

    print()

    print("=" * 60)
    print("CUSTOM PROJECT")
    print("=" * 60)

    project = Project(

        name="FitOS",

        description="AI Operating System",

        status=ProjectStatus.ACTIVE,

        progress=35.0,

    )

    print("Name        :", project.name)

    print("Description :", project.description)

    print("Status      :", project.status.name)

    print("Progress    :", project.progress)

    print("Created     :", project.created_at)

    print("Completed   :", project.completed_at)


if __name__ == "__main__":

    main()