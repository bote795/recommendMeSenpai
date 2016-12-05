# recommendMeSenpai
##Website
 * [website](http://nicolasbotello.com/recommendMeSenpai/)     
 * [video](link)

##PreProcessing 
[Main Files](https://drive.google.com/drive/folders/0B5N8stIumL_FMGVrTllNajAydUU?usp=sharing):
* [anime.json](link)
 * contains all the anime/Manga from animelist at the time we obtained data
 * 42k records of anime/manga
* [users.json.zip](link)
  * contains users and what they rated different animes/Mangas
  * 200 million records

  To be able to obtain our [data](/data):
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
    
###How to generate our data
#####******* NOTE: All directory paths must be change to fit your setup *******

First run the preProcessData.py 
```bash
python preProcessData.py 
```
that will create anime-min.json

In order to execute the retrievePicTags.py
You must first clone [i2v](https://github.com/rezoo/illustration2vec)  
install dependencies  
```bash
pip install scikit-image
pip install numpy
pip install scipy
pip install Pillow
pip install chainer
```
and download the following files from [website](http://illustration2vec.net/): 
* tag_list.json 
* illust2vec_tag_ver200.caffemodel 
You will then have to move "retrievePicTag.py" into the inside of the cloned Repo
Runing retrievePicTag.py will generate labels-min.json
```bash
python retrievePicTag.py
```
The command above will take different amounts of time depending on your CPU:   
 * i5: 5min per picture
 * i7: 500ms per picture
 
We must then retireve all the extra pictures we downloaded using [scrapy](https://scrapy.org/)
#####install  
```bash 
pip install scrapy 
```
#####Execute 
This will take about ~8 hrs 
```bash
cd myAnimeList 
scrapy crawl myAnimeList --set DOWNLOAD_DELAY=8 -o test-2.json
```
You will need the data from the step above to do the step below   
If you execute all cells in "notebooks/retrieve labels round 2.ipynb"    
it will generate labels2-min.json      
