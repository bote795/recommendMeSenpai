import json
json_data_path='anime.json'
#only contain the following fields
fields = ["image","title"]
output_path='anime-min.json'
anime_dic = {}

with open(json_data_path,'r') as anime_file:
    for anime in anime_file:
        anime=json.loads(anime)
       	#filter only get anime not manga
        if anime["_id"]["t"] == "TV":
        	#make sure no repeat ids
        	if anime["_id"]["i"] in anime_dic:
        		print anime["_id"]["i"] + " this key is already there" 
        	else:
        		temp_anime ={}
        		for field in fields:
        			temp_anime[field] = anime[field]
        		anime_dic[anime["_id"]["i"]] = temp_anime

#write to minfy file
with open(output_path, 'w+') as f: # overwrite if file exists
	f.write(json.dumps(anime_dic))