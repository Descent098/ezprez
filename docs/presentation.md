# Presentation Objects

The ```Presentation``` object is used to collect all of your slides together and allow you to export your content.

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
