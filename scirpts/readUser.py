import zipfile
user_zip="./users.json.zip" 
users_file="users.json"
output_file="users-200-min.json"
number_of_records=200
with zipfile.ZipFile(user_zip) as z:
    with z.open(users_file) as f:
    	with open(output_file, "a") as out_file:
	    	i=0
	        for line in f:
				out_file.write(line)
				if i >= number_of_records:
					break
				i+=1