
# Internal Dependencies
import enum
from abc import ABC
from typing import List, Union
from dataclasses import dataclass


class _Component(ABC):
    """Base class used for type checking, and inheritance on all components"""
    def __html__(self):
        raise NotImplementedError("Components require a __html__() method to be defined")


class SocialLink(enum.Enum):
    """Can be used to create a social media link icon, or just the icon

    Notes 
    -----
    - If you don't call the object's link function, it will just return the social media icon

    Examples
    -------
    ### Adding an icon link to someone's github in a navbar
    ```
    from ezprez.core import Presentation
    from ezprez.components import SocialLink, Navbar

    header = Navbar('Basic web technologies', [SocialLink.github.link("https://github.com/descent098")])
    Presentation(title, url, content, navbar=header)
    ```

    ### Adding an icon with no link to a Slide
    ```
    from ezprez.core import Slide
    from ezprez.components import SocialLink

    Slide('This is a youtube icon with no link', SocialLink.youtube)
    ```
    """
    url:str
    youtube = 0
    github = 1
    twitter = 2
    linkedin = 3
    twitch = 4


    def link(self, link):
        """Function used to asign URL parameter to the link

        Parameters
        ----------
        link : (str)
            The url you want to link to

        Returns
        -------
        The instance called from
        """
        self.url = link
        return self


    def __html__(self, header:bool = True):
        if self.url: 
            if header:
                return f"""\n\t\t\t\t\t<a href='{self.url}' target='_blank' rel='external' style='background-color:#fff; color:#141414;'>
                                    <i class='fab fa-{self.name} fa-3x'></i>
                                </a>\n"""
            else:
                return f"""\n\t\t\t\t\t<a href='{self.url}' target='_blank' rel='external'>
                                    <i class='fab fa-{self.name} fa-3x'></i>
                                </a>\n"""
        else:
            if header:
                return f"""\n\t\t\t\t\t<i class='fab fa-{self.name} fa-3x' style='background-color:#fff; color:#141414;'></i>\n"""
            else:
                return f"""\n\t\t\t\t\t<i class='fab fa-{self.name} fa-3x'></i>\n"""


@dataclass
class Link(_Component):
    """A component for generating web links

    Attributes
    ----------
    label : (str)
        The text shown that the link is applied to

    link : (str)
        The link to tie the label to

    Examples
    -------
    ### Add a link to google to a slide
    ```
    from ezprez.core import Slide
    from ezprez.components import Link

    Slide('This is a link to Google', Link('Click this to go to google', 'https://google.ca'))
    ```
    """
    label: str
    link: str


    def __html__(self, header:bool = False):
        if not header:
            return f"""\n\t\t\t\t\t<a href={self.link} target='_blank' rel='external'>{self.label}</a>\n"""
        else:
            return f"""\n\t\t\t\t\t<a href={self.link} target='_blank' rel='external' style='background-color:#fff; color:#141414;'>{self.label}</a>\n"""


@dataclass
class Code(_Component):
    """A component for adding code demos with syntax highlighting

    Attributes
    ----------
    language: (str)
        The programming language (Supports all the common languages listed on https://highlightjs.org/download/ )

    content: (str)
        The code to show off

    Notes
    -----
    - Uses highlightJS for syntax highlighting: https://highlightjs.org/download/

    Examples
    --------
    ### Add some html example code to a slide
    ```
    from ezprez.core import Slide
    from ezprez.components import Code

    Slide("Here is some example html", Code("html", "<p>This is some example code</p>"))
    ```
    """
    language: str
    content: str


    def _escape(self) -> str:
        """Escapes self.content so it's HTML safe

        Returns
        -------
        str
            The escaped string of content
        """
        self.content = self.content.replace("<", "&lt").replace(">", "&gt").replace("&", "&amp").replace('"', "&quot").replace("'", "&apos")
        return self.content


    def __html__(self):
        return f"""\t\t\t\t\t<pre><code class='language-{self.language.lower()}'>{self._escape()}</code></pre>\n"""


@dataclass
class Icon(_Component):
    """A component that generates an icon

    Parameters
    ----------
    label: (str)
        The icon name i.e. 'fa-heart' (details at https://fontawesome.com/)

    size: (str), optional;
        The size of icon, i.e. 60px, defaults to 48px

    Examples
    -------
    ### Put a heart icon in the middle of a slide
    ```
    from ezprez.core import Slide
    from ezprez.components import Icon

    Slide("This is a heart icon", Icon("fa-heart"))
    ```
    """
    label:str
    size:str = "48px"


    def __html__(self):
        return f"""\t\t\t\t\t<svg class='{self.label}' style='width:{self.size};height:{self.size};'><use xlink:href='#{self.label}'></use></svg>\n"""


@dataclass
class Footer(_Component):
    links: str


    def __html__(self):
        result =f"""
        <footer>
        """

        for link in self.links:
            if type(link) == Link or type(link) == SocialLink:
                result += f"\n\t\t\t{link.__html__(header=True)}\n"
            else:
                raise ValueError(f"Navbar arguments must be of type ezprez.components.Link or ezprez.components.SocialLink, got type {type(link)}")

        result += """
        </footer>\n
        """
        return result


@dataclass
class Navbar(_Component):
    title: str
    links: List[Union[Link, SocialLink]]


    def __html__(self):
        result =f"""
        <header role="banner">
            <nav role="navigation">
                <p class="logo"><a href="" target="_blank" title="{self.title}">{self.title}</a></p>
                <ul>
        """

        for link in self.links:
            if type(link) == Link or type(link) == SocialLink:
                result += f"\n\t\t\t\t\t<li>{link.__html__(header=True)}</li>\n"
            else:
                raise ValueError(f"Navbar arguments must be of type ezprez.components.Link or ezprez.components.SocialLink, got type {type(link)}")
        result += """
                </ul>
            </nav>
        </header>
        """

        return result


@dataclass
class Raw(_Component):
    """A component that dumps provided raw html

    Attributes
    ----------
    content: str 
        The HTML content to generate

    Examples
    -------
    ### Add a manual paragraph tag to a Slide
    ```
    from ezprez.core import Slide
    from ezprez.components import Raw

    content = '<p>This is some text</p'

    Slide('This is some raw content', Raw(content))
    ```
    """
    content:str


    def __html__(self):
        return self.content


class TableOfContents(_Component):
    """A component used to generate table of contents for a presentation

    Attributes
    ----------
    sections: dict
        A dictionary of {label:slide_number}'s to generate the table of contents with

    Examples
    ----------
    ### Create a table of contents Slide for a presentation
    ```
    from ezprez.core import Slide
    from ezprez.components import TableOfContents

    # The argument is a dictionary where each key is the label in the table
    # and each value is the slide number
    sections = {'Intro':2, 'End': 5}

    Slide('Table of contents', TableOfContents(sections))
    ```
    """
    def __init__(self, sections):
        self.sections = sections


    def __html__(self):
        result = "\n\t\t<hr>\n\t\t<div class='toc'>\n\t\t\t<ol>"
        for section_title in self.sections:
            result += f"\n\t\t\t\t<li>\n\t\t\t\t\t<a href='#slide={self.sections[section_title]}' title='Go to {section_title}'>\n\t\t\t\t\t<span class='chapter'>{section_title}</span>\n\t\t\t\t\t<span class='toc-page'>{self.sections[section_title]}</span>\n\t\t\t\t</a></li>"
        result += "\n\t\t\t</ol>\n\t\t</div>\n"
        return result 
