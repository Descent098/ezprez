# Quick Start

## Installation

### From PyPi

1. Run ```pip install ezprez```

### From source

1. Clone this repo: (put github/source code link here)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory

## Usage

For just plain text slides the easiest way to get started is just using the ```Slide``` and ```Presentation``` objects:

```python
from ezprez.core import Slide, Presentation

# Create a slide object (don't need to assign it to a variable or anything it's added to presentation on instantiation)
Slide("This is the slide title", "this is some content")

# Setup the actual presentation settings
presentation_url = "https://kieranwood.ca/ezprez-example" # The URL the presentation will be hosted at
prez = Presentation("This is the presentation title", "This is the presentation description", presentation_url)

# Export the presentation in the current directory at /Presentation
prez.export(".", folder_name="Presentation")
```

There will then be a folder called ```Presentation```, and inside the ```index.html``` file will contain your presentation. Just put that up on a static hosting service and you're good to go.

## Where to go from here

I would recommend looking at the [Slide object documentation](https://ezprez.readthedocs.io/en/latest/slide), and the [Presentation object documentation](https://ezprez.readthedocs.io/en/latest/presentation). 

**You can also check out some of these external resources:**

[Template repository for bootstrapping projects](https://github.com/QU-UP/ezprez)

Example presentation: [Live demo](https://kieranwood.ca/ezprez-example), [Source Code](https://github.com/Descent098/ezprez-example)
