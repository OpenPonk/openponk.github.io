# Installation

* 1\. Download latest Pharo 5\.0 image \(or Moose 6\.0\)



* 2\. Clone all required git repositories

For read\-write access make sure it's `git@github` and not `https://`

```bash
    git clone git@github.com:dynacase/dynacase.git dynacase
    git clone git@github.com:dynacase/dynacase-model.git dynacase-model
```



* 3\. Inside image \(in Playground\) load GitFileTree and project

**Point Metacello to `repository` subfolder of the repo\.**

The script will complain about conflicts, allow them\.

I strongly suggest adding this to a startup script — e\.g\. when your new image contains
"DynaCASE" in it's name it will automatically download and setup everything\.


&nbsp;


```smalltalk
    "install GitFileTree"
    Gofer new
        url: 'http://smalltalkhub.com/mc/Pharo/MetaRepoForPharo50/main';
        configurationOf: 'GitFileTree';
        loadDevelopment.
    
    "load DynaCASE-Model"
    Metacello new
        baseline: 'DynaCASEModel';
        repository: 'gitfiletree:///my_path_to_dynacase_model/repository';
        lock.
    
    "load DynaCASE"
    Metacello new
        baseline: 'DynaCASE';
        repository: 'gitfiletree:///my_path_to_dynacase/repository';
        onConflict: [ :ex | ex allow ];
        load.
    
    "adding BORM"
    
    "BORM Model"
    Metacello new
    	baseline: 'BormModel';
    	repository: 'gitfiletree:///my_path_to_borm_model/repository';
    	lock.
    
    "BORM Editor"
    Metacello new
    	baseline: 'BormEditor';
    	repository: 'gitfiletree:///my_path_to_borm_editor/repository';
    	onConflict: [ :ex | ex allow ];
    	load.
```

**Windows note:** Use forward slashes \(/\) even on Windows\. For example


&nbsp;



    repository: 'gitfiletree:///C:/Users/Username/Pharo/dynacase/repository';
