class Project:
    def __init__(self, name, description, dependencies, dev_dependencies,lisenssi,authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.lisenssi = lisenssi
        self.authors = authors
    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.lisenssi or '-'}"
            f"\n\nAuthors:\n"+ "\n".join(f"- {i}" for i in self.authors) +

            f"\n\nDependencies:\n"+ "\n".join(f"- {i}" for i in self.dependencies) +
            f"\n\nDevelopment dependencies:\n"+ "\n".join(f"- {i}" for i in self.dev_dependencies)
        )
