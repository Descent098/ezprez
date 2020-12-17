# Components

Inside the ```ezprez.components``` module there are a number of components that can be used to achieve two primary tasks:

- Used as ```Slide``` contents arguments to create content beyond just text and lists
- Used as ```Presentation``` and ```Slide``` attributes to customize the look and behaviour of each respective class

## SocialLink

Can be used to create a social media link icon, or just the icon. Can be used in a ```Slide```, or also in a ```Navbar``` or ```Footer```. 

**Usage**

*Creating a ```SocialLink``` with a link to a github account*

```python
from ezprez.core import Slide
from ezprez.components import SocialLink

Slide("Title", SocialLink("github", "https://github.com/descent098"))
```

*Creating a ```SocialLink``` that is just the youtube icon*

```python
from ezprez.core import Slide
from ezprez.components import SocialLink

Slide("Title", SocialLink("youtube"))
```

*Adding an ```SocialLink``` to a github account in a navbar*

```
from ezprez.core import Presentation
from ezprez.components import SocialLink, Navbar

header = Navbar('Basic web technologies', [SocialLink("github", "https://github.com/descent098")])
Presentation(title, url, content, navbar=header)
```

*Creating a ```SocialLink``` that is green*

```python
from ezprez.core import Slide
from ezprez.components import SocialLink

Slide("Title", SocialLink("github", "https://github.com/descent098", "green"))
```


## Link

A component for generating text web links. Can be used in a ```Slide```, or also in a ```Navbar``` or ```Footer```.

```python
from ezprez.core import Slide
from ezprez.components import Link

Slide("Title", Link("my website", "https://kieranwood.ca"))
```

*Adding a ```Link``` to a ```Slide``` that is green*
```python
from ezprez.core import Slide
from ezprez.components import Link

Slide("Title", Link("my website", "https://kieranwood.ca", color="green"))
```

*Adding an ```Link``` to a ```Navbar```*

```
from ezprez.core import Presentation
from ezprez.components import Link, Navbar

header = Navbar('Basic web technologies', [Link("my website", "https://kieranwood.ca")])
Presentation(title, url, content, navbar=header)
```

## Code

A component for adding code demos with syntax highlighting. All "Common" languages are supported from [highlightjs](https://highlightjs.org/download/).

**Usage**

*Creating a ```Slide``` with some demo python code*

```python
from ezprez.core import Slide
from ezprez.components import Code

language = "python"
content = "from ezprez.core import Slide\n\nSlide('this is getting meta', 'wowee')"

Slide("Here is some demo python code", Code(language, content))
```

## Icon

A component that generates an icon. Uses [fontawesome icons](https://fontawesome.com/icons) (Note not all are included). To get a particular icon identifier, look at the code it spits out (i.e. ```<i class="fa-heart"></i>```) and copy just the class (in this case 'fa-heart').

**Usage**

*Creating a ```Slide``` with the [heart icon](https://fontawesome.com/icons/heart)*

```python
from ezprez.core import Slide
from ezprez.components import Icon

Slide("Here is an icon", Icon("fa-heart"))
```

*Creating a ```Slide``` with the [heart icon](https://fontawesome.com/icons/heart) and increasing the size to 60px*

```python
from ezprez.core import Slide
from ezprez.components import Icon

Slide("Here is an icon", Icon("fa-heart", size="60px"))
```

*Creating a ```Slide``` with the [heart icon](https://fontawesome.com/icons/heart) that is red and increasing the size to 60px*

```python
from ezprez.core import Slide
from ezprez.components import Icon

Slide("Here is an icon", Icon("fa-heart", size="60px", color="red"))
```

## F‎ooter

Allows you to add a footer to the presentation. It takes in a list of an arbitrary number of ```Link``` or ```SocialLink``` objects.

**Usage**

*Adding a ```Footer``` with a github ```SocialLink``` to a ```Presentation```*

```python
from ezprez.core import Presentation
from ezprez.components import Footer

foot = Footer([SocialLink("github", "https://github.com/Descent098/ezprez-example")])
Presentation(title, description, url, footer=foot)
```

*Adding a ```Footer``` with a regular ```Link``` to a ```Presentation```*

```python
from ezprez.core import Presentation
from ezprez.components import Footer

foot = Footer([Link("my website", "https://kieranwood.ca")])
Presentation(title, description, url, footer=foot)
```

## Navbar

Allows you to add a navbar to the presentation. It takes in a list of an arbitrary number of ```Link``` or ```SocialLink``` objects.

**Usage**

*Adding a ```Navbar``` with a github ```SocialLink``` to a ```Presentation```*

```python
from ezprez.core import Presentation
from ezprez.components import Footer

foot = Footer([SocialLink("github", "https://github.com/Descent098/ezprez-example")])
Presentation(title, description, url, footer=foot)
```

*Adding a ```Navbar``` with a regular ```Link``` to a ```Presentation```*

```python
from ezprez.core import Presentation
from ezprez.components import Footer

foot = Footer([Link("my website", "https://kieranwood.ca")])
Presentation(title, description, url, footer=foot)
```

## Button

A component that allows you to add html buttons. There are two required arguments (```label``` and ```url```), and several optional attributes:

- ghost: (boolean) if set to True button will be an outline with no color filled, defaults to False. Note that if this is True then ```Button.color``` and ```Button.text_color``` are ignored
- rounding: (boolean) if set to True button will rounded instead of square, defaults to True
- color: (str) a string of what color the button should be; takes any valid html color string (i.e. #f0f0f0, blue, rgba(255, 255, 255, 0.9)), if set to False the default color is used ("#44d")
- text_color: (str) a string of what color the button text should be; takes any valid html color string (i.e. #f0f0f0, blue, rgba(255, 255, 255, 0.9)), if set to False the default color is used ("white")
- icon: (Icon) you can provide an icon component if you want it to be used in a button, defaults to False to indicate no icon should be used


**Usage**

*Adding a basic ```Button``` to a ```Slide```*
```python
from ezprez.core import Slide
from ezprez.components import Button

Slide("Here's a button", Button("click me", "https://kieranwood.ca"))
```

*Adding a ```Button``` with every custom parameter to a ```Slide```*
```python
from ezprez.core import Slide
from ezprez.components import Button, Icon

heart = Icon("fa-heart")

Slide("Here's a button", Button("click me", "https://kieranwood.ca", ghost=False, rounding=False, color="#141414", text_color="#f0f0f0", icon=heart))
```

## Raw

A component that dumps provided raw html into a ```Slide```.

**Usage**

*Adding some text that is emphasised and bolded to a ```Slide```*
```python
from ezprez.core import Slide
from ezprez.components import Raw

content = '<strong><em><p>This is some text</p></em></strong>'

Slide('This is some raw content', Raw(content))
```

## TableOfContents

A component used to generate table of contents for a ```Presentation```. 

**Usage**

Takes in a dict where each key is the label for the section, and each value is the slide number to link to.

*Create a ```TableOfContents``` ```Slide``` for a ```Presentation```*

```python
from ezprez.core import Slide
from ezprez.components import TableOfContents

sections = {'This section starts on Slide 2':2, 'This section starts on Slide 5': 5}

Slide('Table of contents', TableOfContents(sections))
```

## Video

A component that allows you to embed a youtube video. You will need to get the video ID. To get the video id from a video grab the end of the URL (i.e. for ```youtube.com/watch?v=wSVljLh1VmI``` then the id is 'wSVljLh1VmI').

**Usage**

*Adding a youtube video to a Slide*

```python
from ezprez.core import Slide
from ezprez.components import Video

Slide('Here is a video', Video('wSVljLh1VmI'))
```

## Grid
A component that allows you to evenly space multiple peices of content

**Usage**

*Add a ```Grid``` with  a few peices content*
```
from ezprez.core import Slide
from ezprez.components import Grid

Slide("You can also have grids", Grid("With", "Lots", "of", "content"))
```

*Add a ```Slide``` of a ```Grid``` of lists*
```
from ezprez.core import Slide
from ezprez.components import Grid

Slide("Like, alot of content...", Grid(["You can stack content within grids", ["like this", "and this", "and even this"]], ["This is getting too much now", ["way", "way way", "too much"]]))
```

## Image

A component to include images. 

There are several optional fields:
- width (int): if you want to override the default image width
- height (int): if you want to override the default image height
- browser (bool): if ```True``` will add a "browser window" boarder to an image i.e. https://webslides.tv/demos/components#slide=114

**Usage**

Image files must be kept in the same directory as the presentation file under ```/img``` or ```/images```

*Add an ```Image``` to a ```Slide```*
```python
from ezprez.core import Slide
from ezprez.components import Image

Slide("This is an image", Image("low poly ice caps", "kieran-wood-lp-ice-caps-4k-w-peng.jpg"))
```

*Add a background ```Image``` to a ```Slide```*
```python
from ezprez.core import Slide
from ezprez.components import Image

Slide("This is a background image", image=Image("low poly ice caps", "kieran-wood-abstract-landscape.jpg"), background="black")
```
