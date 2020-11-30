import enum
from dataclasses import dataclass

from abc import ABC
from typing import List

class Component(ABC):
    def __html__(self):
        raise NotImplementedError("Components require a __html__() method to be defined")

class SocialLinks(enum.Enum):
    youtube = 0
    github = 1
    twitter = 2
    linkedin = 3
    twitch = 4

    def __html__(self, url: str):
        return f"""\n\t\t\t\t\t<a href='{url}' target='_blank' rel='external'>
                        <i class='fab fa-{self.name} fa-3x'></i>
                    </a>\n"""

@dataclass
class Footer(Component):
    links: str

    def __html__(self):
        result =f"""
        <footer>
        """

        for link in self.links:
            if type(link[0]) != SocialLinks:
                result += f"\n\t\t\t\t\t<a href={link[1]} target='_blank' rel='external' title={link[0]}>{link[0]}</a>\n"
            else:
                result += link[0].__html__(link[1])

        result += """
        </footer>\n
        """
        return result

@dataclass
class Navbar(Component):
    title: str
    links: List[list]


    def __html__(self):
        result =f"""
        <header role="banner">
            <nav role="navigation">
                <p class="logo"><a href="/" target="_blank" title="{self.title}">{self.title}</a></p>
                <ul>
        """

        for link in self.links:
            if type(link[0]) != SocialLinks:
                result += f"\n\t\t\t\t\t<li><a href={link[1]} target='_blank' rel='external' title={link[0]}>{link[0]}</a></li>\n"
            else:
                result += link[0].__html__(link[1])

        result += """
                </ul>
            </nav>
        </header>
        """

        return result