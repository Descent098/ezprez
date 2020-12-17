# Slide Objects

In ```ezprez.core``` the most basic class that is necessary is the ```Slide``` Class. This class is what you use to create the content for the presentation.

## Basic usage

The most basic usage is to instantiate a ```Slide``` object and feed it some string, or list content. For example:

```python
from ezprez.core import Slide

Slide("This is the slide title", "This is the content")
```

You can add an arbitrary number of arguments to a ```Slide``` to act as the content:

```python
from ezprez.core import Slide

title = "This is the slide title"

Slide(title, "This is multiple content", ["You can add", "as many", "arguments as you want"])

Slide(title, "you", "can", "get", "as", "ridiculous", "as", "you", "want", "with", "this")
```

You can also use any [components](/components) as a ```Slide``` content:

```python
from ezprez.core import Slide
from ezprez.components import Video

Slide("This is a slide with a video", Video("wSVljLh1VmI"))
```

## Configuring slides

There are several options you have to configure slides as you want

### Configuring the background color of a Slide

By default slides use whatever the ```Presentation``` object is set to (default is 'white'). But this can be overridden on a per-```Slide``` basis. For example setting the background color of a ```Slide``` to black:

```python
from ezprez.core import Slide

Slide("This is a black slide", "...and this is the content", background="black")
```

Background colors available can be found at https://webslides.tv/demos/components#slide=27; just make sure to remove 'bg', so for example 'bg-black' becomes 'black'.

### Configuring the content alignment

You have two forms of control over content alignment, horizontal, and vertical alignment control. Since they are independent you can mix and match them as you see fit. Each are strings with the following options:

**Horizontal**

- "center": The default, and aligns content to the center
- "left":   Aligns content to the left of the screen
- "right":  Aligns content to the right of the screen

**Vertical**

- "center": The default, and aligns content to the center
- "top":    Aligns content to the top of the screen
- "bottom":  Aligns content to the bottom of the screen

**Usage**

```python
from ezprez.core import Slide

Slide(title, content, vertical_alignment="bottom", horizontal_alignment="left")
```

### Configuring a background image for a slide

Outside of just having a background color, you can also set an image to the ```Slide``` background using the ```Slide.image``` attribute. For example:

```python
from ezprez.core import Slide
from ezprez.components import Image

background_image = Image("/path/to/image", "image description")

Slide("This has a background image", "Check it out", image=background_image)
```

### Configuring the animation of a slide

By default each slide animates it's transition as a fade in, but this can be configured to one of these five options:

- fadeIn
- fadeInUp
- zoomIn
- slideInLeft
- slideInRight

Additionally you can make the animation move slowly by adding 'slow' to the end of the animation i.e. 'zoomIn slow'

**Usage**

You can modify the animation using the ```Slide.animation``` attribute

```python
from ezprez.core import Slide

Slide("You can also change the animation", "Like this one (which is 'zoomIn slow')", animation="zoomIn slow")
```
