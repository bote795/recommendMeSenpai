import urllib, cStringIO, json, traceback
from PIL import Image
import time                                                
import i2v
import sys

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))


        print(endTime - startTime,'ms')
        return result


    return wrapper


@timeme
def getTags(key, illust2vec, img, file):
	labels = illust2vec.estimate_plausible_tags([img], threshold=0.07)
	temp = {}
	temp["id"]=key
	temp["labels"]=labels
	file.write(json.dumps(temp) + "\n")
	return labels


json_data_path='./anime-min.json'
image_labels_path = 'labels-min.json'
image_error_labels_path = 'labels-error-min.json'
anime_dict={}
labels_dict = {}
illust2vec = i2v.make_i2v_with_chainer(
    "illust2vec_tag_ver200.caffemodel", "tag_list.json")
with open(json_data_path,'r') as anime_dict_json:
	anime_dict = json.load(anime_dict_json)
	#if there is data in file read it then add to dict

	try: 
		print "reading info from: "+image_labels_path
		with open(image_labels_path, "r") as f:
			for pic in f:
				pic_labels = json.loads(pic)
				labels_dict[pic_labels["id"]] = pic_labels["labels"]
	except IOError as e:
		print "Error reading in"
		print (e.errno)
		pass
	#go through file and try to get labels
	#if anime already in file don't try to get labels again
	print "starting to write data to: "+ image_labels_path
	with open(image_labels_path, "a") as f:
		for key, value in anime_dict.iteritems():

			if not labels_dict.has_key(key):
				try:
					URL= value["image"]
					#retrieve pic from url convert to data
					file = cStringIO.StringIO(urllib.urlopen(URL).read())
					#open image
					img = Image.open(file)
					print value["title"].encode('utf-8')
					getTags(key, illust2vec,img, f)
					#break;
				except:
					e = sys.exc_info()[0]
					with open(image_error_labels_path, "a") as eror_file:
						temp = {}
						temp["id"]=key
						temp["image"] = value["image"]
						temp["title"] = value["title"]
						callstack = ''.join(traceback.format_exc())
						temp["tracestack"]= callstack
						eror_file.write(json.dumps(temp) + "\n")
					print e
					pass

print "done"