# Standard lib dependencies
import os
from shutil import copytree, copyfile, rmtree
from datetime import datetime
from typing import Union, List
from dataclasses import dataclass, field

# Internal dependencies
from ezprez.components import *

# External Dependencies
from elevate import elevate
from pystall.core import ZIPResource, build


class Slide:
    def __init__(self, heading:str, *contents:Union[str, list, tuple, Component], background:Union[bool,str] = False, horizontal_alignment="center", vertical_alignment="center", image="" ):
        self.contents = contents
        self.heading = heading # The slide's title/heading
        self.background = background # i.e. brown, generates <section class='bg-<background>'>
        self.image = image
        self.horizontal_alignment = horizontal_alignment # Can be left, right or center
        self.vertical_alignment = vertical_alignment # can be top, bottom or center
        


    def _generate_content(self):
        result = f"\n\t\t\t<section class='bg-{self.background} slide-{self.vertical_alignment}'>"
        
        if self.image:
            result += f"\n\t\t\t\t<span class='background' style='background-image:url(\"{self.image}\")'></span>"
        result += f"\n\t\t\t\t<div class='wrap'>\n\t\t\t\t\t<div class='content-{self.horizontal_alignment}'>\n\t\t\t\t\t<h2>{self.heading}</h2>\n"
        
        for content in self.contents:
            if type(content) == str:
                result += f"\t\t\t\t\t<p>{content}</p>\n"

            elif type(content) == list or type(content) == tuple:
                result += f"\t\t\t\t\t<div class='grid {'content-' + self.horizontal_alignment if not self.horizontal_alignment == 'right' else ''}'>\n\t\t\t\t\t\t\t<ul style='text-align:justify;'>\n"
                for bullet_point in content:
                    result += f"\t\t\t\t\t\t\t\t<li>{bullet_point}</li>\n"
                result += "\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</ul>\n"
            elif isinstance(content, Component):
                result += content.__html__()
        result += "\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</section>\n"

        yield result


    def __html__(self):
        """Generates the markup for each slide"""
        result = ""
        for content in self._generate_content():
            result+= content
        return result

@dataclass
class Presentation:
    title: str # The title of the presentation
    description: str # The description of the presentation
    url: str # The canonical URL the presentation will be deployed at
    slides: List[Slide]
    background: str = "white" # What color the intro slide should be
    image: str = "" # Path to image to use for og tags
    endcard: bool = True # Whether to add the endcard
    generate_intro: bool = True # Generate an introduction slide with the background image and whatnot
    favicon: Union[bool, str] =  False # Path to favicon
    vertical: bool = False # Whether the slideshow should be vertical or not
    navbar: Union[bool, Navbar] = False # The navbar for the site
    footer: Union[bool, Footer] = False # The footer for the site


    def _generate_favicon_markup(self):
        if self.favicon: # TODO: COPY FAVICON
            return f'''<!-- FAVICONS -->
            <link rel="apple-touch-icon icon" sizes="76x76" href="{self.favicon}">'''
        else:
            return f'''<!-- FAVICONS -->
            <link rel="apple-touch-icon icon" sizes="76x76" href="static/images/favicons/favicon-152.png">'''


    def _generate_intro_slide(self):
        if self.generate_intro:
            if self.image:
                return f"""\t\t\t<section class='bg-{self.background}'>
                <span class='background' style='background-image:url("{self.image}")'></span>
                    <div class='wrap aligncenter'>
                        <h1><strong>{self.title}</strong></h1>
                        <p class='text-intro'>{self.description}</p>
                    </div>
            </section>"""
            else:
                return f"""\t\t\t<section class='bg-{self.background}'>
                    <div class='wrap aligncenter'>
                        <h1><strong>{self.title}</strong></h1>
                        <p class='text-intro'>{self.description}</p>
                    </div>
            </section>"""


    def _generate_endcard(self):
        if self.endcard:
            return f"""\t\t\t<section class='bg-{self.background}'>
                    <div class='wrap aligncenter'>
                        <h2><strong>Thank you for listening</strong></h2>
                        <h4 class='text-intro'>This presentation was made with the help of</h4>
                        <h4>
                            <strong><em><a href='https://webslides.tv' target='_blank'>WebSlides</a></em></strong> 
                        </h4>
                        <h4>
                            <strong><em><a href='https://github.com/Descent098/ezprez' target='_blank'>ezprez</a></em></strong>
                        </h4>
                    </div>
            </section>"""
        else:
            return ""


    def __len__(self):
        return len(self.slides)


    def __html__(self):
        """Generates the base html"""
        slides_html = ""
        for slide in self.slides:
            slides_html += slide.__html__()
        
        #TODO; copy specfied image

        result = f'''<!doctype html>
<html lang="en" prefix="og: http://ogp.me/ns#">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- SEO -->
        <title>Basic Web Technologies</title>
        <meta name="description" content="{self.description}">

        <!-- URL CANONICAL -->
        <link rel="canonical" href="{self.url}">

        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,700,700i%7CMaitree:200,300,400,600,700&amp;subset=latin-ext" rel="stylesheet">

        <!-- CSS WebSlides -->
        <link rel="stylesheet" type='text/css' media='all' href="static/css/webslides.css">

        <!-- Optional - CSS SVG Icons (Font Awesome) -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />

        <!-- SOCIAL CARDS (ADD YOUR INFO) -->

        <!-- FACEBOOK -->
        <meta property="og:url" content="{self.url}">
        <meta property="og:type" content="article">
        <meta property="og:title" content="{self.title}"> 
        <meta property="og:description" content="{self.description}">
        <meta property="og:updated_time" content="{datetime.today()}">
        <meta property="og:image" content="{self.image if self.image else "static/images/share-webslides.jpg"}">

        <!-- TWITTER -->
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="{self.title}"> 
        <meta name="twitter:description" content="{self.description}"> 
        <meta name="twitter:image" content="{self.image if self.image else "static/images/share-webslides.jpg"}">

        {self._generate_favicon_markup()}

        <!-- Android -->
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="theme-color" content="#f0f0f0">

        <!-- Code highlighting -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.4.0/styles/default.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.4.0/highlight.min.js"></script>
        <script>hljs.initHighlightingOnLoad();</script>

    </head>
    {self.navbar.__html__() if self.navbar else ""}
    <body>

    <main role='main'>
        <article id='webslides' {'class="vertical"' if self.vertical else ""}>
{self._generate_intro_slide()}
{slides_html}
{self._generate_endcard()}

        </article>
        <!-- end article -->
    </main>
    <!-- end main -->

    <!-- Required -->
    <script src='static/js/webslides.js'></script>
    <script>
        window.ws = new WebSlides();
    </script>

    <!-- OPTIONAL - svg-icons.js (fontastic.me - Font Awesome as svg icons) -->
    <script defer src='static/js/svg-icons.js'></script>

    </body>
    {self.footer.__html__() if self.footer else ""}
</html>
        '''
        return result
        

    def export(self, file_path:str, force:bool = False):
        # check if webslides is downloaded, if it is use those files, if not download and extract it
        file_path = os.path.abspath(file_path)

        # finding downloads folder
        if os.name == "nt":
            DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
        else: # PORT: Assuming variable is there for MacOS and Linux installs
            DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads" 
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "webslides")):
            try:
                build(ZIPResource("webslides", "https://webslides.tv/webslides-latest.zip", overwrite_agreement=True))
                copytree(os.path.join(DOWNLOAD_FOLDER, "webslides"), os.path.join(os.path.dirname(__file__), "webslides"))
            except PermissionError:
                elevate()
                copytree(os.path.join(DOWNLOAD_FOLDER, "webslides"), os.path.join(os.path.dirname(__file__), "webslides"))
        try:
            copytree(os.path.join(os.path.dirname(__file__), "webslides"), os.path.join(file_path, self.title))
        except FileExistsError:
            if force:
                rmtree(os.path.join(file_path, self.title))
                copytree(os.path.join(os.path.dirname(__file__), "webslides"), os.path.join(file_path, self.title))
            else:
                raise FileExistsError(f"The file path {os.path.join(file_path, self.title)} exists, to replace use Presentation.export({file_path}, force=True)")

        # replace index.html with generated html
        with open(os.path.join(file_path, self.title, "index.html"), "w+") as presentation_file:
            presentation_file.write(self.__html__())


if __name__ == "__main__":

    # header = Navbar("Basic web technologies", [[SocialLinks.github,"https://kieranwood.ca"], ["canadian coding", "https://canadiancoding.ca"]])
    # foot = Footer([[SocialLinks.github,"https://kieranwood.ca"], ["canadian coding", "https://canadiancoding.ca"]])
    slide_1 = Slide("H T M L", "Any nouns on a webpage are typically html", ["that block of text", "that image", "etc."], background="black")
    slide_2 = Slide("J S", "Hello my dude", background="white")
    slide_3 = Slide("TITLe", "CONTENT", background="white")
    prez = Presentation("Basic web technologies", "Learn to code my dude", "", background="black-blue", slides=[slide_1, slide_2, slide_3])
    prez.export(".", force=True)