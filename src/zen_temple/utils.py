from typing import Optional


class Version:
    def __init__(self, version_string: str):
        sub_versions: list[int] = [int(i) for i in version_string.split(".")]
        self.versions = sub_versions
        self.major = sub_versions[0]
        self.minor = sub_versions[1]
        self.patch = sub_versions[2]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented

        for i in range(len(self.versions)):
            if self.versions[i] != other.versions[i]:
                return False

        return True

    def __gt__(self, other: "Version") -> bool:
        for i in range(len(self.versions)):
            if self.versions[i] != other.versions[i]:
                return self.versions[i] > other.versions[i]
        return False

    def __repr__(self) -> str:
        return ".".join([str(i) for i in self.versions])


variable_versions = {
    "0.0.0": {},
    "1.9.0": {
        "capex_yearly": "cost_capex_yearly",
        "opex_yearly": "cost_opex_yearly",
        "cost_opex_total": "cost_opex_yearly_total",
        "cost_opex": "cost_opex_variable",
        "cost_capex_total": "cost_capex_yearly_total",
        "cost_capex": "cost_capex_overnight",
    },
}


def get_variable_name(variable: str, version_string: Optional[str] = None) -> str:
    if version_string is None:
        version_string = "0.0.0"

    results_version = Version(version_string)
    relevant_version_string = "0.0.0"

    for defined_version_string in variable_versions:
        defined_version = Version(defined_version_string)

        if defined_version > results_version:
            break
        relevant_version_string = defined_version_string

    if variable in variable_versions[relevant_version_string]:
        return variable_versions[relevant_version_string][variable]

    return variable
