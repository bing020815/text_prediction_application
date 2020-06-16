# Github Filing Rules
This is the filing tutorial for the __text_prediction_application__ project. To make sure the reproducibility, files need to be saved in the certain folder and following the naming rules.
 

## Table of Contents
* <a href="#structure">Repo Structure</a>
* <a href="#filename">File Name</a>
* <a href="#path">Path</a>


## <span id="structure">Repo Structure</span>

```
.
├── readme.md
├── data
│   └── aclImdb
│   └── movie_data	
│   └── reviews	
├── models
├── img
├── sentiment
├── text
└── others
```


* Folder purpose:
	- __application__: application relative, ex: anvil code
	- __data__:  all data relative
	- __models__: trained model for production 
	- __img__: image relative
	- __sentiment__: developing programs for sentiment prediction
	- __text__: developing programs for text prediction
	- __others__: other files


## <span id="filename">File Name</span>
Unless programs are ready for the production, every developing program file should follow the naming rule:  

```
initial_programfilename.extention
ex: BJW_this_is_file_name.py
```

## <span id="path">Path</span>
To make sure the reproducibility, data should be loaded through either `url` or `relative path`. 

Let's say we have two folders, `data` and `program`, under the `repo` folder. A data file, `data.csv`, is stored in the `data` folder and a program is located in the `program` folder. To get the data loaded in the program, we can use relative path:

```
'../data/data.csv'
```

The `../` refers to the parent directory of the current directory. In the example, `../data/data.csv`, the parent directory here is the `repo`folder.   

To get the url of the data:

```
Click the data file -> Click on 'View raw' -> copy the url showing on the browser
```

When saving a model, use the `relative path` approach to save the model into the `models` folder

```
'../models/model.p'
```


[<p align='center'>Top</p>](#github-filing-rules)
