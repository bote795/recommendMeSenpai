# recommendMeSenpai

[Main Files](https://drive.google.com/drive/folders/0B5N8stIumL_FMGVrTllNajAydUU?usp=sharing):
* [anime.json](link)
 * contains all the anime/Manga from animelist at the time we obtained data
* [users.json.zip](link)
  * contains users and what they rated different animes/Mangas

  To be able to obtain our [data](https://drive.google.com/drive/folders/0B5N8stIumL_FcmFNUE8wU181bVU?usp=sharing):
  	* anime-min.json
  		* a filtered version of anime.json containing only anime
  	* labels-min.json
  		* runing all pictures from anime-min.json through i2v and retrieved labels for each pic
  	* labels2-min.json
  		* runing all pictures from test-2.json through i2v and retrieved labels for each pic
  	*  test-2.json
  		* crawled extra pics
  	* users-200.min.json
  		* extract 200 records from users.json.zip
  	* users-1000.min.json
  		* extract 1000 records from users.json.zip

First run the preProcessData.py 
python preProcessData.py

that will create anime-min.json

In order to execute the retrievePicTags.py
You must first clone [i2v](https://github.com/rezoo/illustration2vec) and install dependencies
and download the following files: 
* tag_list.json 
* illust2vec_tag_ver200.caffemodel 

Runing retrievePicTag.py will generate labels-min.json
in notebooks/retrieve labels round 2.ipynb
if all run will generate labels2-min.json

runing readUser.py will generate the users files but you have to change the number of users you want 200/1000