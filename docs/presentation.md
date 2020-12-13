# Presentation Objects

The ```Presentation``` object is used to collect all of your slides together and allow you to export your content.

## Basic usage

The most basic usage requires 3 parameters to be passed:
1. The presentation title
2. The presentation description
3. The canonical URL of the presentation (The URL the presentation will be hosted at)

This can be done like so:

```python
from ezprez.core import Presentation

title = "This is the presentation title"

description = "This is a description of the URL"

url = "https://kieranwood.ca/ezprez-example" # The URL the presentation will be hosted at

prez = Presentation(title, description, url)
```

From here you can [add slides](/slide#basic-usage) then [export the presentation](#export-content).

## Configuration options

There are several optional keyword arguments you can provide to make the ```Presentation``` object behave the way you want.

### Overwriting which slides are used

By default the ```Presentation``` object will use the ```Slide.all``` attribute to include all generated slides in the ```Presentation```. If for some reason you want to override this behaviour, you can pass in the ```slides``` keyword argument to the constructor:

```python
from ezprez.core import Presentation, Slide

s1 = Slide("This is a slide", "wowwee")

s2 = Slide("This is also a slide", "wowowee")

s3 = Slide("So is this", "But I don't want to include it for some reason")

slides = [s1, s2]

prez = Presentation(title, description, url, slides=slides)
```

### Setting the default slide background color

If no background color is explicitly set on a ```Slide``` then the ```Presentation.background``` attribute is used. You can modiy this on presentation instantiation:

```python
from ezprez.core import Presentation, Slide

Slide("This is a slide", "It will be white no matter what", background="White")

Slide("This is also a slide", "but it will be the Presentation.background color (black)")

Slide("So is this", "and it will also be the Presentation.background color (black)")

prez = Presentation(title, description, url, background="black")
```

### Background/opengraph image

If you want to use an image as the background of the intro slide, and as the opengraph (sharing preview) image you can set the ```Presentation.image``` attribute to an ```Image``` component:

```python
from ezprez.core import Presentation
from ezprez.components import Image

bg_image = Image("This is a background image", "/path/to/image")

prez = Presentation(title, description, url, image=bg_image)
```


### Intro slide generation

By default an intro ```Slide``` is generated with the ```Presentation.title``` and ```Presentation.description``` in it. If you don't want this then set ```Presentation.intro``` to ```False```:

```python
from ezprez.core import Presentation

prez = Presentation(title, description, url, intro=False)
```

### Customizing favicon

If you want to modify the favicon (icon that appears in web browser tab), then pass an ```Image``` component to ```Presentation.favicon```:

```python
from ezprez.core import Presentation
from ezprez.components import Image

favicon = Image("This is a favicon", "/path/to/favicon")

prez = Presentation(title, description, url, favicon=favicon)
```

### Making Presentation vertical

By default presentations are navigatable horizontally (like a traditional slideshow), but you are also able to set the ```Presentation``` to be vertically navigatable by making ```Presentation.vertical``` be ```True```:

```python
from ezprez.core import Presentation

prez = Presentation(title, description, url, vertical=True)
```

### Adding a Presentation Navbar

You can add a ```Navbar``` component to a ```Presentation``` by setting ```Presentation.navbar```:

```python
from ezprez.core import Presentation
from ezprez.components import Navbar

nav = Navbar('Presentation title', [SocialLink.github.link("https://github.com/Descent098/ezprez-example")])

Presentation(title, description, url, navbar=nav)
```

### Adding a Presentation Footer

You can add a ```Footer``` component to a ```Presentation``` by setting ```Presentation.footer```:

```python
from ezprez.core import Presentation
from ezprez.components import Footer

foot = Footer([SocialLink.github.link("https://github.com/Descent098/ezprez-example")])

Presentation(title, description, url, footer=foot)
```


### Endcard generation

By default at the end of every presentation an endcard is generated to say thanks and mention that the presentation is generated using ezprez and webslides. If you want to disable this, you can set ```Presentation.endcard``` to ```False``` (though I would appreciate the shoutout :D ):

```python
from ezprez.core import Presentation

prez = Presentation(title, description, url, endcard=False)
```

## Export content

To export content use the ```Presentation.export()``` method. the only required parameter is the directory you want to export to (use "." for current directory). For example:

```python
from ezprez.core import Presentation
prez = Presentation(title, description, url)

prez.export(".") # Exports in current directory at /<Presentation.title>
```

By default the ```folder_name``` will default to ```Presentation.title``` so files will export to ```<file_path>/<Presentation.title>```, and will only export if the folder **DOES NOT YET EXIST** (see below to change that behaviour).

If you haven't run ezprez before it will download and extract webslides and then copy it to ```<file_path>/<folder_name>```, and replace ```index.html``` with your created content.

### Customizing output folder name

To change the output folder name modify the keyword argument ```folder_name```:

```python
from ezprez.core import Presentation
prez = Presentation(title, description, url)

prez.export(".", folder_name="Presentation") # Exports in current directory at /Presentation
```

### Force exporting of files
If you are going to be exporting multiple times, it is a good idea to set the ```force``` flag on ```Presentation.export()``` since by default the export will error out if a folder already exists at the export directory. For example:

```python
from ezprez.core import Presentation
prez = Presentation(title, description, url)

prez.export(".", force=True) # Force exports in current directory at /<Presentation.title>
```
